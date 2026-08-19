from collections import Counter
from dataclasses import dataclass
import pathlib
import sys
from typing import List, Set, Dict, Tuple

import ast
import re
import csv

root = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root))

from Items import (aptitudes, assists, costumes, currencies, equipments,
                   quests, keys, materials, passives, skills, spirits, stats,
                   tips, events)

id_to_item : Dict[str, str] = {}
for table in (aptitudes, assists, costumes, currencies, equipments, quests,
              keys, materials, passives, skills, spirits, stats, tips):
    for entry, name in table.rows.items():
        id_to_item[entry] = name
for event in events.values():
    id_to_item[event.key] = event.name


def load_macros(path: pathlib.Path) -> Tuple[Set[str], Dict[str, str]]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    names : Set[str] = set()
    aliases : Dict[str, str] = {}
    for stmt in tree.body:
        if isinstance(stmt, ast.Assign):
            targets = stmt.targets
        elif isinstance(stmt, ast.AnnAssign):
            targets = [stmt.target]
        else:
            continue
        for target in targets:
            if not isinstance(target, ast.Name) or target.id.startswith("_"):
                continue
            if target.id == "Aliases":
                aliases = ast.literal_eval(stmt.value)
            else:
                names.add(target.id)
    return names, aliases


macros, aliases = load_macros(root / "Macros.py")

for alias, target in sorted(aliases.items()):
    if alias in id_to_item or alias in macros:
        print(f"alias {alias!r} shadows an existing item or macro")
    if target not in id_to_item:
        print(f"alias {alias!r} points to unknown item {target!r}")


TOKEN_REGEX = re.compile(r'\s*([A-Za-z0-9_]+|\+|\||\(|\))')

def tokenize(text: str):
    tokens = []
    pos = 0
    for m in TOKEN_REGEX.finditer(text):
        if m.start() != pos:
            raise ValueError(f"unexpected character at {pos} in : {text}")
        tokens.append(m.group(1))
        pos = m.end()
    if pos != len(text.rstrip()):
        raise ValueError(f"unexpected character at {pos} in : {text}")
    if not tokens:
        raise ValueError(f"couldn't tokenize : {text}")
    return tokens

class Expr:
    pass

@dataclass(frozen=True)
class Symbol(Expr):
    name: str

    def __repr__(self) -> str:
        return f"{self.name}"

    def __str__(self) -> str:
        return f"{self.name}"

@dataclass(frozen=True)
class And(Expr):
    terms: List[Expr]
    def __repr__(self) -> str:
        return f"AND({len(self.terms)} {self.terms})"

@dataclass(frozen=True)
class Or(Expr):
    terms: List[Expr]
    def __repr__(self) -> str:
        return f"OR({len(self.terms)} {self.terms})"

class Parser:
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self):
        tok = self.peek()
        self.pos += 1
        return tok

    def parse(self):
        expr = self.parse_or()
        if self.peek() is not None:
            raise SyntaxError(f"unexpected token : {self.peek()}")
        return expr

    def parse_or(self):
        terms = [self.parse_and()]
        while self.peek() == '|':
            self.consume()
            terms.append(self.parse_and())
        return terms[0] if len(terms) == 1 else Or(terms)

    def parse_and(self):
        terms = [self.parse_term()]
        while self.peek() == '+':
            self.consume()
            terms.append(self.parse_term())
        return terms[0] if len(terms) == 1 else And(terms)

    def parse_term(self):
        tok : str = self.peek()

        if tok == '(':
            self.consume()
            expr = self.parse_or()
            if self.consume() != ')':
                raise SyntaxError(f"missing closing parenthesis")
            return expr

        if tok is None:
            raise SyntaxError("incomplete expression")

        self.consume()
        if tok.lower().endswith("_lever"):
            tok = tok.lower()
        return Symbol(aliases.get(tok, tok))

DNF = Set[frozenset[Symbol]]
def to_dnf(expr: Expr) -> DNF:
    if isinstance(expr, Symbol):
        return {frozenset({expr})}
    elif isinstance(expr, Or):
        return { clause for t in expr.terms for clause in to_dnf(t) }
    elif isinstance(expr, And):
        result: DNF = {frozenset()}
        for t in expr.terms:
            result = { frozenset(r | p) for r in result for p in to_dnf(t) }
        return result
    else:
        raise TypeError(f"Type inconnu: {type(expr)}")


def is_macro(symbol: str) -> bool:
    return symbol in macros

def item_arg(symbol: str) -> str:
    name = id_to_item.get(symbol, symbol)
    return repr(name)


def parse_csv(path: str, node_col: int, logic_col: int, error: list) -> Dict[str, DNF]:
    nodes : Dict[str, DNF] = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row_num, cols in enumerate(list(csv.reader(f))[1:], start=2):
            if len(cols) < max(node_col, logic_col) + 1:
                print("invalid line", len(cols), cols)
                continue
            node = cols[node_col]
            logic = cols[logic_col] or "None"
            try:
                nodes[node] = to_dnf(Parser(tokenize(logic)).parse())
            except (SyntaxError, ValueError) as e:
                error.append((node, f"error: {e} {row_num}:[{logic}]"))
                print(f"{row_num}:{logic}")
                print(f"error parsing {e}")
    return nodes


def count_symbols(nodes: Dict[str, DNF], known_nodes: Set[str]):
    used_symbols : Counter = Counter()
    for dnfs in nodes.values():
        for term in dnfs:
            for s in term:
                if s.name not in known_nodes and s.name != "None":
                    used_symbols[s.name] += 1
    used_items = {s: used_symbols[s] for s in sorted(used_symbols) if s in id_to_item}
    used_macros = {s: used_symbols[s] for s in sorted(used_symbols) if is_macro(s)}
    used_unknown = {s: used_symbols[s] for s in sorted(used_symbols)
                    if s not in id_to_item and not is_macro(s)}
    return used_items, used_macros, used_unknown


def sort_clauses(dnfs: DNF) -> List[frozenset]:
    return sorted(dnfs, key=lambda term: sorted(s.name for s in term))


def extract_rules(nodes: Dict[str, DNF], known_nodes: Set[str], error: list) -> Dict[Tuple[str, str], DNF]:
    node_to_node : Dict[Tuple[str, str], DNF] = {}
    multi_node_seen : Set[Tuple[str, str]] = set()
    for node, dnfs in nodes.items():
        for term in sort_clauses(dnfs):
            nodes_in_term = {s.name for s in term if s.name in known_nodes}
            items_in_term = frozenset({s for s in term if s.name not in known_nodes})
            if len(items_in_term) == 1 and list(items_in_term)[0].name == "None":
                continue
            if len(nodes_in_term) == 1:
                src = nodes_in_term.pop()
                node_to_node.setdefault((src, node), set()).add(items_in_term)
            elif len(nodes_in_term) == 0:
                items = ", ".join(sorted(s.name for s in items_in_term))
                print(f"{node} rule: no other nodes, only items {{{items}}}")
                error.append((node, f"missing a node in condition: {{{items}}}"))
                break
            elif len(nodes_in_term) > 1:
                names = ", ".join(sorted(nodes_in_term))
                msg = (node, f"multiple nodes in condition, added as True: {names}")
                if msg not in multi_node_seen:
                    multi_node_seen.add(msg)
                    print(f"{node} rule: multiple nodes {names}, added each as True")
                    error.append(msg)
                for src in sorted(nodes_in_term):
                    node_to_node.setdefault((src, node), set()).add(frozenset())
    return node_to_node


def find_redundant_rules(rules: Dict[Tuple[str, str], DNF], error: list):
    for key, clauses in rules.items():
        ordered = sort_clauses(clauses)
        for i, a in enumerate(ordered):
            for j, b in enumerate(ordered):
                if i == j:
                    continue
                if b.issubset(a):
                    plop1 = "+".join(sorted(str(s) for s in a))
                    plop2 = "+".join(sorted(str(s) for s in b))
                    print(f"{key[1]} as a useless rule: {key[0]} + {plop1} because it already has: {key[0]} + {plop2}")
                    error.append((key[1], f"redundant rule: {key[0]} + {plop1} (already in {key[0]} + {plop2})"))


def clause_expr(clause, macro_names: Set[str]) -> str:
    macros = sorted(s.name for s in clause if is_macro(s.name))
    names = sorted(item_arg(s.name) for s in clause if not is_macro(s.name))
    macro_names.update(macros)
    parts = list(macros)
    if len(names) == 1:
        parts.append(f"Has({names[0]})")
    elif len(names) > 1:
        parts.append("HasAll(" + ", ".join(names) + ")")
    if not parts:
        return "True_()"
    return " & ".join(parts)

def rule_expr(clauses, macro_names: Set[str]) -> str:
    if any(len(clause) == 0 for clause in clauses):
        return "True_()"
    return " | ".join(clause_expr(clause, macro_names) for clause in sort_clauses(clauses))


def build_rule_lines(logic: Dict[Tuple[str, str], DNF], macro_names: Set[str]) -> List[str]:
    rule_entries = []
    for (src, dst), rules in logic.items():
        rule_entries.append((f"{src!r},", f"{dst!r})", rule_expr(rules, macro_names)))
    src_width = max((len(src_repr) for src_repr, _, _ in rule_entries), default=0)
    key_width = max((len("(" + src_repr.ljust(src_width) + " " + dst_repr)
                     for src_repr, dst_repr, _ in rule_entries), default=0)
    lines = []
    for src_repr, dst_repr, expr in rule_entries:
        key = "(" + src_repr.ljust(src_width) + " " + dst_repr
        lines.append(f"\t{key.ljust(key_width)} : {expr},\n")
    return lines


def write_gen(path: str, used_items, used_macros, used_unknown, error: list, rule_lines: List[str], macro_names: Set[str]):
    with open(path, "w", encoding="utf-8") as f:
        f.write("from typing import Dict, Tuple\n")
        f.write("from rule_builder.rules import Has, HasAll, Rule, True_\n")
        if macro_names:
            f.write(f"from ..Macros import {', '.join(sorted(macro_names))}\n")
        f.write("\n")

        for name, table in (("items", used_items), ("macros", used_macros), ("unknown", used_unknown)):
            f.write(f"{name}: Dict[str, int] = {{\n")
            for sym, n in table.items():
                f.write(f"\t{sym!r} : {n},\n")
            f.write("}\n\n")

        f.write("errors: Dict[str, str] = {\n")
        error.sort()
        errors_by_node : Dict[str, List[str]] = {}
        for a, b in error:
            errors_by_node.setdefault(a, []).append(b)
        for a, msgs in errors_by_node.items():
            f.write(f"\t{a!r} : {' ; '.join(msgs)!r},\n")
        f.write("}\n\n")

        f.write("rules: Dict[Tuple[str, str], Rule] = {\n")
        for line in rule_lines:
            f.write(line)
        f.write("}\n")


def generate(csv_path: str, node_col: int, logic_col: int,
             out_path: str, known_nodes: Set[str] = None) -> Set[str]:
    error : List[Tuple[str, str]] = []
    nodes = parse_csv(csv_path, node_col, logic_col, error)
    own_nodes = set(nodes)
    own_nodes.add("Menu")
    resolve_against = own_nodes if known_nodes is None else (known_nodes | own_nodes)
    used_items, used_macros, used_unknown = count_symbols(nodes, resolve_against)
    for sym, count in used_unknown.items():
        print(f"{pathlib.Path(csv_path).name}: unknown symbol {sym!r} used {count} times")
    node_to_node = extract_rules(nodes, resolve_against, error)
    find_redundant_rules(node_to_node, error)
    macro_names : Set[str] = set()
    rule_lines = build_rule_lines(node_to_node, macro_names)
    write_gen(out_path, used_items, used_macros, used_unknown, error, rule_lines, macro_names)
    return own_nodes


transition_nodes = generate(
    f"{root}/data/magnolia rando - Transitions Logic.csv", node_col=1, logic_col=8,
    out_path=f"{root}/gen/TransitionsRules.py")

generate(
    f"{root}/data/magnolia rando - Locations Logic.csv", node_col=1, logic_col=9,
    out_path=f"{root}/gen/LocationsRules.py", known_nodes=transition_nodes)

generate(
    f"{root}/data/magnolia rando - Events Logic.csv", node_col=1, logic_col=8,
    out_path=f"{root}/gen/EventsRules.py", known_nodes=transition_nodes)


generate(
    f"{root}/data/magnolia rando - Future Transitions Logic.csv", node_col=1, logic_col=3,
    out_path=f"{root}/gen/TransitionsAdvancedRules.py")

generate(
    f"{root}/data/magnolia rando - Future Locations Logic.csv", node_col=1, logic_col=4,
    out_path=f"{root}/gen/LocationsAdvancedRules.py", known_nodes=transition_nodes)

generate(
    f"{root}/data/magnolia rando - Future Events Logic.csv", node_col=1, logic_col=3,
    out_path=f"{root}/gen/EventsAdvancedRules.py", known_nodes=transition_nodes)