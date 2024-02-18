import socket

# Créer une socket
host = '37.59.31.202'
port = 2000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# Recevoir et afficher le message d'accueil
print("> " + s.recv(1024).decode('utf-8'))

# Sélectionner le challenge "3"
s.send(b"3\n")

# Recevoir et afficher la réponse du serveur au challenge
print("> " + s.recv(1024).decode('utf-8'))

def verify_v2(string):
    global s
    count_brace = 0
    count_bracket = 0
    count_par = 0

    for char in string:      
        if char == '{':
            count_brace += 1
        elif char == '}':
            count_brace -= 1
        elif char == '[':
            count_bracket += 1
        elif char == ']':
            count_bracket -= 1
        elif char == '(':
            count_par += 1
        elif char == ')':
            count_par -= 1
        if count_brace < 0 or count_par < 0 or count_bracket < 0:    
            print("BREAK")
            break  

    if count_brace == 0 and count_par == 0 and count_bracket == 0:
        s.send(b"True")
        print("True")
    else:
        print("False")
        s.send(b"False")

for i in range(25):
    string_c = s.recv(1024).decode('utf-8')
    print(string_c)
    verify_v2(string_c)

# Fermer la connexion
s.close()
