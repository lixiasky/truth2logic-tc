from typing import List, Dict
from sympy import symbols, And, Or, Not, simplify_logic

def generate_expression(truth_table: List[Dict[str, int]]) -> str:
    # 检查输入
    if not truth_table:
        return "Empty truth table."

    # 提取变量名
    var_names = [k for k in truth_table[0] if k != "out"]
    vars_map = {name: symbols(name) for name in var_names}

    # 构造输出为 1 的最小项
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

    # 构造布尔表达式并化简为括号优先的形式
    expr = Or(*minterms)
    simplified = simplify_logic(expr, form='dnf')

    # 将符号表达式转为字符串（带括号 + 用and/or/not）
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

# 示例
if __name__ == "__main__":
    example_table = [
        {"A": 0, "B": 0, "C": 0, "out": 0},
        {"A": 1, "B": 0, "C": 0, "out": 1},
        {"A": 0, "B": 1, "C": 0, "out": 1},
        {"A": 1, "B": 1, "C": 1, "out": 0},
        {"A": 1, "B": 0, "C": 1, "out": 1},
    ]
    print(generate_expression(example_table))
