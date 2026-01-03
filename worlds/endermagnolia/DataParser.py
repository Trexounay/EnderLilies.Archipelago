from dataclasses import dataclass
import pathlib
from typing import List, Set, Dict, Tuple, Optional

import re
import csv


TOKEN_REGEX = re.compile(r'\s*([A-Za-z0-9_]+|\+|\||\(|\))')

def tokenize(text: str):
    tokens = TOKEN_REGEX.findall(text)
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
        if tok.endswith("_Lever"):
            tok = tok.lower()
        return Symbol(tok)

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

root = pathlib.Path(__file__).parent.resolve()
nodes : Dict[str, DNF] = {}
with open(f"{root}/Data/Transitions Logic.csv", newline="", encoding="utf-8") as f:
    reader = list(csv.reader(f))
    for row_num, cols in enumerate(reader[1:], start=2):
        if len(cols) < 4:
            print("invalid line", len(cols), cols)
            continue
        node = cols[1]
        logic = cols[3]
        if not cols[3]:
            continue
        try:
            ast = Parser(tokenize(logic)).parse()
            dnf = to_dnf(ast)
            nodes[node] = dnf
        except SyntaxError as e:
            print(f"{row_num}:{logic}")
            print(f"error parsing {e}")

node_to_node : Dict[Tuple[str, str], DNF] = {}

ignored = (0,0)
# extracts node from DNF to create rules from node to node
for node, dnfs in nodes.items():
    for term in dnfs:
        nodes_in_term = {s.name for s in term if s.name in nodes}
        items_in_term = frozenset({s for s in term if s.name not in nodes})
        if len(items_in_term) == 1 and list(items_in_term)[0].name == "None":
            continue
        if len(nodes_in_term) == 1:
            src = nodes_in_term.pop()
            key = (src, node)
            if key not in node_to_node:
                node_to_node[key] = set()
            node_to_node[key].add(items_in_term)
        elif len(nodes_in_term) == 0:
            ignored = (ignored[0] + 1, ignored[1])
            print(f"{node} rule: no other nodes, only items {set(items_in_term)}")
            break
        elif len(nodes_in_term) > 1:
            ignored = (ignored[0], ignored[1] + 1)

def find_redundant_rules(rules: Dict[Tuple[str, str], DNF]):
    for key, clauses in rules.items():
        for i, a in enumerate(clauses):
            for j, b in enumerate(clauses):
                if i == j:
                    continue
                if b.issubset(a):
                    plop1 = "+".join([str(s) for s in a])
                    plop2 = "+".join([str(s) for s in b])
                    print(f"{key[1]} as a useless rule: {key[0]} + {plop1} because it already has: {key[0]} + {plop2}")

find_redundant_rules(node_to_node)


connections : Dict[str, Set[str]] = {}
logic : Dict[Tuple[str, str], DNF] = {}
count = (0, 0)
for (src, dst), rules in node_to_node.items():
    if src not in connections:
        connections[src] = set()
    connections[src].add(dst)
    logic[(src, dst)] = rules
    if len(list(rules)[0]) > 0:
        count = (count[0], count[1] + 1)
    else:
        count = (count[0] + 1, count[1])

with open(f"{root}/TransitionsRules.gen.py", "w", encoding="utf-8") as f:

#    f.write("def s(*items : str):\n")
#    f.write("\tfrozenset(items)\n\n")
    f.write("connections = {\n")
    for src, dsts in connections.items():
        f.write(f"\t'{src}' : {{")
        for dst in dsts:
            f.write(f"'{dst}',")
        f.write("},\n")
    f.write("},\n")

    f.write("rules = {\n")    
    for (src, dst), rules in logic.items():
        lambda_expr = 'None'
        if len(list(rules)[0]) > 0:
            lambda_expr = "{" + ",".join(
                "(" + ",".join(f"'{item.name}'" for item in clause) + ")"
                for clause in rules
            ) + "}"
        #lambda_expr = ",".join(",".join(f"'{item}'" for item in clause) for clause in rules)
        #lambda_expr = f"{{{[for x in clause for clause for clause in rules]}}}"
            
        #lambda_expr = " or ".join(" and ".join(f'has("{x}")' for x in clause) for clause in rules)
        #lambda_expr = f"lambda s : {lambda_expr}"
            f.write(f"\t'{src} to {dst}' : {lambda_expr},\n")
    f.write("}\n")

