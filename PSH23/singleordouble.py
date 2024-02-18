from pwn import *

def parenthesisValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack

def checkParentheses(challenges):
    results = []

    for challenge in challenges:
        result = parenthesisValid(challenge)
        results.append(result)

    return results

def connect_and_challenge():
    # Se connecter au serveur
    r = remote('37.59.31.202', 2000)

    # Recevoir les données du serveur
    data = r.recv().decode("utf-8")


    r.send(b"3\n")
    # Diviser les challenges en une liste
    
    data = r.recv().decode("utf-8")
    
    challenges = data.strip().split("\n")

    

    # Vérifier les parenthèses pour chaque challenge
    results = checkParentheses(challenges)

    # Afficher les résultats
    for i, result in enumerate(results):
        print(f"Challenge {i + 1}: {'True' if result else 'False'}")

if __name__ == "__main__":
    connect_and_challenge()
