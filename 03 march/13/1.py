def fix_parentheses(string: str) -> str:

    return "(" * (string.count("(") - string.count("()")) + string + ")" * (string.count(")") - string.count("()"))


# print(fix_parentheses("("))  # повертає "()"
# print(fix_parentheses(")"))  # повертає "()"
# print(fix_parentheses("()"))  # повертає "()"
print(fix_parentheses("))))(()("))  # повертає "(((())))(()())"
# print(fix_parentheses("((())()"), ' # Я б хотів  "((())())"')# а виводить ((())())