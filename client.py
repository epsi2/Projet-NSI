from socket import socket, AF_INET, SOCK_STREAM

message=b"bonjour serveur je suis client"
hote="localhost"
port=50004

socket_client = socket(AF_INET,SOCK_STREAM)
socket_client.connect((hote,port))
print("Connexion au serveur")
socket_client.send(message)
print("Fermeture de la connexion")
socket_client.close()