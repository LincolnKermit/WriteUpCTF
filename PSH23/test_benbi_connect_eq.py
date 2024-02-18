import socket

def evaluate_expression(expr):
    if expr[0] == '+':
        return evaluate_expression(expr[1]) + evaluate_expression(expr[2])
    elif expr[0] == '-':
        return evaluate_expression(expr[1]) - evaluate_expression(expr[2])
    elif expr[0] == '*':
        return evaluate_expression(expr[1]) * evaluate_expression(expr[2])
    else:
        return int(expr)

def solve_expressions(expressions):
    results = []
    for expr in expressions:
        result = evaluate_expression(expr)
        results.append(result)
    return results

def main():
    # Configurer le serveur
    host = '37.59.31.202'
    port = 2000

    # Créer le socket du serveur
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Serveur en attente sur {host}:{port}")

    # Attendre la connexion d'un client
    client_socket, client_address = server_socket.accept()
    print(f"Connexion établie depuis {client_address}")

    # Recevoir le nombre d'expressions
    num_expressions = int(client_socket.recv(1024).decode())
    print(f"Nombre d'expressions à recevoir : {num_expressions}")

    # Recevoir les expressions
    expressions = []
    for _ in range(num_expressions):
        expr = client_socket.recv(1024).decode()
        expressions.append(expr)

    # Résoudre les expressions
    results = solve_expressions(expressions)

    # Envoyer les résultats au client
    client_socket.send(str(results).encode())

    # Fermer les sockets
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()