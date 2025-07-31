import json
import sys
from typing import List, Dict
from sympy import symbols, And, Or, Not, simplify_logic

def generate_expression(truth_table: List[Dict[str, int]]) -> str:
    if not truth_table:
        return "Empty truth table."

    var_names = [k for k in truth_table[0] if k != "out"]
    vars_map = {name: symbols(name) for name in var_names}

    minterms = []
    for row in truth_table:
        if row["out"] == 1:
            term = []
            for name in var_names:
                val = row[name]
                var = vars_map[name]
                term.append(var if val == 1 else Not(var))
            if term:
                minterms.append(And(*term))

    if not minterms:
        return "OUT = False"

    expr = Or(*minterms)
    simplified = simplify_logic(expr, form='dnf')

    def expr_to_str(e) -> str:
        if e.is_Symbol:
            return str(e)
        elif e.func == Not:
            return f"(not {expr_to_str(e.args[0])})"
        elif e.func == And:
            return "(" + " and ".join(expr_to_str(arg) for arg in e.args) + ")"
        elif e.func == Or:
            return "(" + " or ".join(expr_to_str(arg) for arg in e.args) + ")"
        else:
            return str(e)

    return "OUT = " + expr_to_str(simplified)

def main():
    if len(sys.argv) < 2:
        print("Usage: python logic_tool.py <truth_table.json>")
        return

    json_path = sys.argv[1]
    try:
        with open(json_path, "r") as f:
            truth_table = json.load(f)
    except Exception as e:
        print(f"Failed to load JSON: {e}")
        return

    result = generate_expression(truth_table)
    print(result)

if __name__ == "__main__":
    main()
