from pwn import *

r = remote('37.59.31.202', 2000)

print("> " + r.recv().decode('utf-8'))

r.send(b"2\n")

print("> " + r.recv().decode('utf-8'))
while True:
    # Recevoir et afficher l'expression
    # Répondre à 100 expressions
    for _ in range(100):
        expression = r.recv().decode('utf-8')
        print("Expression:", expression)
        print(expression.isdigit())
        try:
            if expression[0] == '+' and expression[2].isdigit():
                result = eval(expression)
                print("Result:", result)
                r.send(f"{result}\n".encode('utf-8'))
        except Exception as e:
            print(f"Error while evaluating the expression: {e}")
        print("Expression:", expression)
        print(expression.isdigit())
        try:
            if expression[0] == operator and expression[2].isdigit():
                print(eval(expression))

            

            # result = eval(result_final)
            # print("Résultat:", result)

            # Envoyer la réponse au serveur
            #r.send(f"{result}\n".encode('utf-8'))
        except Exception as e:
            print(f"Erreur lors du calcul de l'expression : {e}")
