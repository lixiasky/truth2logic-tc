from typing import List, Dict
from sympy import symbols, And, Or, Not, simplify_logic

def generate_expression(truth_table: List[Dict[str, int]]) -> str:
    if not truth_table:
        return "Empty truth table."

    # 提取变量名（去掉 'out'）
    var_names = sorted([key for key in truth_table[0] if key != "out"])
    vars = symbols(" ".join(var_names))
    var_map = {name: sym for name, sym in zip(var_names, vars)}

    # 构造最小项
    minterms = []
    for row in truth_table:
        if row.get("out", 0) == 1:
            term = []
            for name in var_names:
                value = row.get(name, 0)
                if value:
                    term.append(var_map[name])
                else:
                    term.append(Not(var_map[name]))
            if term:
                minterms.append(And(*term))

    if not minterms:
        return "OUT = False"

    expr = Or(*minterms)
    simplified = simplify_logic(expr, form='dnf')
    return f"OUT = {simplified}"


if __name__ == "__main__":
    # 示例：可支持任意数量变量与行数的真值表
    example_table = [
        {"A": 0, "B": 0, "C": 0, "out": 0},
        {"A": 1, "B": 0, "C": 0, "out": 0},
        {"A": 0, "B": 1, "C": 0, "out": 0},
        {"A": 1, "B": 1, "C": 0, "out": 0},
        {"A": 0, "B": 0, "C": 1, "out": 0},
        {"A": 1, "B": 0, "C": 1, "out": 0},
        {"A": 0, "B": 1, "C": 1, "out": 0},
        {"A": 1, "B": 1, "C": 1, "out": 1},
    ]

    result = generate_expression(example_table)
    print(result)