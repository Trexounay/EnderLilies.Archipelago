from dataclasses import dataclass
import pathlib
from typing import List, Set, Dict, Tuple

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
                raise SyntaxError("missing closing parenthesis")
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
    reader = csv.reader(f)
    for row_num, cols in enumerate(reader, start=1):
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
            print(f"{row_num}: error parsing {e}")

node_to_node : Dict[Tuple[str, str], DNF] = {}

# extracts node from DNF to create rules from node to node
for node, dnfs in nodes.items():
    for term in dnfs:
        nodes_in_term = {s.name for s in term if s.name in nodes}
        items_in_term = frozenset({s for s in term if s.name not in nodes})
        if len(nodes_in_term) == 1:
            src = nodes_in_term.pop()
            key = (src, node)
            if key not in node_to_node:
                node_to_node[key] = set()
            node_to_node[key].add(items_in_term)
        elif len(nodes_in_term) == 0:
            pass#print(f"{node} rule {i}: no other nodes, only items {r}")
        elif len(nodes_in_term) > 1:
            pass#print(f"{node} rule {i}: multiple nodes {r['nodes']}, items {r['items']}")

def find_redundant_rules(rules: Dict[Tuple[str, str], DNF]):
    for key, clauses in rules.items():
        for i, a in enumerate(clauses):
            for j, b in enumerate(clauses):
                if i == j:
                    continue
                if b.issubset(a):
                    print(f"{key} as a duplicate {a} {b}")
print("")

find_redundant_rules(node_to_node)

print("")
count = (0, 0)
for (src, dst), rules in node_to_node.items():
    for rule in rules:
        if len(rule) > 0:
            #print(f"'{src} to {dst}' : lambda s : {rules}")
            count = (count[0], count[1] + 1)
        else:
            count = (count[0] + 1, count[1])
        break
print(count)

with open(f"{root}/TransitionsRules.gen.py", "w", encoding="utf-8") as f:
    f.write("rules = {\n")
    for (src, dst), rules in node_to_node.items():
        lambda_expr = " or ".join(
            " and ".join(f'has("{x}", s)' for x in clause) if clause else "True"
            for clause in rules
        )
        f.write(f'    "{src} to {dst}": lambda s: {lambda_expr},\n')
    f.write("}\n")
