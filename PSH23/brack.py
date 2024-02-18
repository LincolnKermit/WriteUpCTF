import socket

def is_valid_parentheses(expression):
    stack = []
    parentheses_map = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in parentheses_map.values():
            stack.append(char)
        elif char in parentheses_map.keys():
            if not stack or stack.pop() != parentheses_map[char]:
                return False

    return not stack

def evaluate_strings(strings):
    results = []
    for s in strings:
        results.append(is_valid_parentheses(s))
    return results

# Exemple d'utilisation avec les chaînes fournies
expressions = ["{()[]}", "{[])(}"]
results = evaluate_strings(expressions)

for i, result in enumerate(results):
    print(f"Expression {i+1}: {result}")
