from socket import socket, AF_INET, SOCK_STREAM

message = """HTTP/1.1 200 OK
Content-Type: text/html \n
<!doctype html>
<html>
<body> 
<h1>hola</h1>
</body>
</html>"""
ss = socket(AF_INET,SOCK_STREAM)
ss.bind(("192.168.1.194",50004))
ss.listen(1)
connexion=True

while connexion:
    client, adresse= ss.accept()
    print("Client {} connecté".format(adresse))
    print("\n***********************************\n")
    reponse = client.recv(256)
    print(reponse)
    client.send(message.encode())
    
client.close()


print("Fermeture du serveur")
ss.close()    