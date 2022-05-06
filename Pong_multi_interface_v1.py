from tkinter import *
from time import *
from socket import socket, AF_INET, SOCK_STREAM
import threading
import random
import re

global k

fenetre_pong = Tk()
hauteur_fenetre = 800
largeur_fenetre = 1500
fond = Canvas(fenetre_pong, width=largeur_fenetre, height= hauteur_fenetre, background = "black")


def commencement_jeu():
    global joueurs,balle,k,affichage_score,joueur_1_rectangle,joueur_2_rectangle,balle_x,balle_y,bouton_meme_ordinateur,deplacement_joueurs,direction_balle_x,direction_balle_y,fond,hauteur_fenetre,largeur_fenetre,liste_deplacement,liste_touches,score,thread
    
    joueur_1_rectangle = fond.create_rectangle(50,(hauteur_fenetre/2-100),70,(hauteur_fenetre/2+100), fill ="blue")
    joueur_2_rectangle = fond.create_rectangle(largeur_fenetre-100,hauteur_fenetre/2-100,largeur_fenetre-80,hauteur_fenetre/2+100, fill ="white")

    joueurs=[joueur_1_rectangle,joueur_2_rectangle]
    
    
    balle_x = 750
    balle_y = 400
    balle = fond.create_oval(balle_x,balle_y,balle_x+20,balle_y+20, fill='white')
    direction_balle_y = 7
    direction_balle_x = 7
    k=0
    fond.grid(column =0, row = 0)
    

    deplacement_joueurs = {'z':['-10','0'],'s':['10','0'],'o':['-10','1'],'l':['10','1']}  #dictionnaire des touches, de son déplacement et du joueur qu'elle déplace
    liste_touches = []  #les touches actuellement pressées
    liste_deplacement = ['z','s','o','l'] #les touches pouvant bouger les joueurs
    score = [0,0]
    affichage_score = fond.create_text(largeur_fenetre/2,50, text=(str(score[0]),":",str(score[1])), fill="white", font=("Raleway",30,"bold"))#affichage du score

    def key_down(e): #fonction qui regarde si la touche est déjà presséee, sinon l'ajoute dans liste_touches 
        if e.keysym not in liste_touches :
            if e.keysym in liste_deplacement:
                liste_touches.append(e.keysym)
                print(liste_touches)

    def key_up(e): #fonction qui regarde lorsqu'une touche est relachée si elle est dans liste_touche et si oui l'enlève de liste_touche
        if e.keysym in liste_touches:
            liste_touches.remove(e.keysym)


    def rebondissement_balle():        #gère les rebonds de la balle
        global balle_x,balle_y,direction_balle_x,direction_balle_y,score,k
        angle=random.uniform(0.5, 1.5)
        
        if mode==0 or typej == 1:
            if fond.coords(joueurs[0])[1]<=fond.coords(balle)[1]<=fond.coords(joueurs[0])[3] and fond.coords(balle)[0]<=fond.coords(joueurs[0])[2]: #lorsque la balle touche le joueur 1
                if fond.coords(balle)[1]<=(fond.coords(joueurs[0])[3] - fond.coords(joueurs[0])[1])/2 + fond.coords(joueurs[0])[1]:                 #lorsque la balle touche la partie haute du joueur 1
                    balle_x=fond.coords(joueurs[0])[2]
                    k+=0.5                                                                  #variable permettant d'augmenter ou diminuer la vitesse de la balle à chaque rebond sur le joueur 1                                
                    direction_balle_x = (-direction_balle_x+k)                              #renvoie la balle dans le sens opposé de l'arrivée
                    direction_balle_y = -abs((direction_balle_y+k)*angle)                   #renvoie la balle systématiquement vers le haut avec un angle aléatoire (l'angle est modifié en modifiant la composante y du vecteur vitesse de la balle)
                
                elif (fond.coords(joueurs[0])[3] - fond.coords(joueurs[0])[1])/2 + fond.coords(joueurs[0])[1] < fond.coords(balle)[1]: #lorsque la balle touche la partie basse du joueur 1
                    balle_x=fond.coords(joueurs[0])[2]
                    k+=0.5
                    direction_balle_x = (-direction_balle_x+k)
                    direction_balle_y = abs((direction_balle_y+k)*angle)                                                               #renvoie la balle systématiquement vers le bas avec un angle aléatoire

            
            elif fond.coords(joueurs[1])[1]<=fond.coords(balle)[1]<=fond.coords(joueurs[1])[3] and fond.coords(joueurs[1])[0]<=fond.coords(balle)[0]: #lorsque la balle touche le joueur 2
                if fond.coords(balle)[1] <= (fond.coords(joueurs[1])[3] - fond.coords(joueurs[1])[1])/2 + fond.coords(joueurs[1])[1]:                 #lorsque la balle touche la partie haute du joueur 2
                    balle_x=fond.coords(joueurs[1])[0]
                    k+=0.7  
                    direction_balle_x = (-direction_balle_x-k) 
                    direction_balle_y = -abs((direction_balle_y+k)*angle)
                
                elif fond.coords(balle)[1] > (fond.coords(joueurs[1])[3] - fond.coords(joueurs[1])[1])/2 + fond.coords(joueurs[1])[1]:                #lorsque la balle touche la partie basse du joueur 2
                    balle_x=fond.coords(joueurs[1])[0]
                    k+=0.7      
                    direction_balle_x = (-direction_balle_x-k)
                    direction_balle_y = abs((direction_balle_y+k)*angle)

            elif fond.coords(balle)[0] > (largeur_fenetre - 20): #si la balle dépasse le joueur 2 
                score[0] += 1
                balle_x = 750               #réinitialise les coordonnées de la balle
                balle_y = 400           
                direction_balle_x = -7      #réinitialise la composante x du vecteur vitesse de la balle
                direction_balle_y = 7       #                           y 
                k=0

            elif fond.coords(balle)[0]<20:  #si la balle dépasse le joueur 1
                balle_x = 750
                balle_y = 400
                direction_balle_x = 7
                direction_balle_y = 7
                score[1] += 1
                k=0

            elif fond.coords(balle)[1]>hauteur_fenetre-direction_balle_y:       #si la balle cogne le bas
                direction_balle_y = -direction_balle_y*random.uniform(0.3,1.1)  #renvoie la balle avec un angle aléatoire (angle tout de même limité)

            elif fond.coords(balle)[1]<0-direction_balle_y:                     #si la balle cogne le haut
                direction_balle_y = -direction_balle_y*random.uniform(0.3,1.1)  #renvoie la balle avec un angle aléatoire (angle tout de même limité)
    
    
        

    def mouvement_joueurs_et_balle(*args): 
        global balle_x,balle_y,affichage_score
        for touche in liste_touches:                                                                             #pour toutes le touches pressées actuellement, déplace les joueurs en fonction de la touche pressées
            if int(deplacement_joueurs[touche][0])<0 :                                                           #si on déplace la barre vers le haut
                if fond.coords(joueurs[int(deplacement_joueurs[touche][1])])[1]> 5:   
                    if mode == 1 and typej == 1 and int(deplacement_joueurs[touche][1]) == 0:                    #si la barre ne va pas en dehors de la fenetre et qu'on joue en local et que le joueur est le numéro 1
                        fond.move(joueurs[int(deplacement_joueurs[touche][1])],0,deplacement_joueurs[touche][0]) #déplace le joueur
                    elif mode == 1 and typej == 2 and int(deplacement_joueurs[touche][1]) == 1:
                        fond.move(joueurs[int(deplacement_joueurs[touche][1])],0,deplacement_joueurs[touche][0])
                    elif mode == 0:                                                                              #si on joue sur le même appareil
                        fond.move(joueurs[int(deplacement_joueurs[touche][1])],0,deplacement_joueurs[touche][0])
            
            elif fond.coords(joueurs[int(deplacement_joueurs[touche][1])])[3]<hauteur_fenetre:                   #même chose mais cette fois-ci, si on déplace la barre vers le bas
                if mode == 1 and typej == 1 and int(deplacement_joueurs[touche][1]) == 0 :
                    fond.move(joueurs[int(deplacement_joueurs[touche][1])],0,deplacement_joueurs[touche][0])

                elif mode == 1 and typej == 2 and int(deplacement_joueurs[touche][1]) == 1 :
                    fond.move(joueurs[int(deplacement_joueurs[touche][1])],0,deplacement_joueurs[touche][0])
                
                elif mode == 0 :
                    fond.move(joueurs[int(deplacement_joueurs[touche][1])],0,deplacement_joueurs[touche][0])  
        
        
        balle_y += direction_balle_y                                    #modifie la variable donnant les coordonnées de la balle
        balle_x += direction_balle_x
        fond.coords(balle,balle_x,balle_y,balle_x+20,balle_y+20)        #réactualise la position de la balle
        rebondissement_balle()
        
        if mode == 0 or typej == 1:
            fond.delete(affichage_score)                                    #supprime le score pour le remettre et éviter la superposition de deux score où l'absence d'actualisation
            affichage_score = fond.create_text(750,50, text=(str(score[0]),":",str(score[1])), fill="white", font=("Raleway",30,"bold"))
        fenetre_pong.after(10,mouvement_joueurs_et_balle)
        

    def multi():
        global ss, sc, balle_x, balle_y, direction_balle_x, direction_balle_y, fond, affichage_score, typej
        bouton_joueur_1.destroy()
        bouton_joueur_2.destroy()
        print("\n***********************************\n") 
        fin=True
        balle_x = 750           #initialise les coordonnées de la balle
        balle_y = 400
        direction_balle_y = 0   #initialise les coordonnées du vecteur vitesse de la balle
        direction_balle_x = 0
        mouvement_joueurs_et_balle()
        

        if typej == 1:                        #si le joueur est de numéro 1
            ss = socket(AF_INET,SOCK_STREAM)
            ss.bind(("localhost",50004))
            ss.listen(1)
            connexion=True
            

            while connexion:
                print("\n***********************************\n")
                print("\nEn attente d'un joueur...\n")
                client, adresse= ss.accept()       #établit la connexion avec l'appareil du joueur de numéro 2
                print("\n***********************************\n")
                print("Client {} connecté".format(adresse))
                print("\n***********************************\n")
        
                direction_balle_y = 7   #la balle bouge, la partie commence
                direction_balle_x = 7

                while fin:
                    client.send((str(fond.coords(joueurs[0]))+","+str(fond.coords(balle))+","+str(score)).encode("utf8"))    #envoie les coordonnées de la barre du joueur 1, de la balle et le score
                    reponsebrut = client.recv(1024).decode("utf8")                                                           #réception du message du joueur 2 en le décodant contenant les coordonnées de la barre ce dernier                                     
                    reponse = re.sub("\[|\]","",reponsebrut).split(", ")                                                     #nettoie le message
                
                    if len(reponse)==4:                                                                                      #si le message est de longueur 4 (il se peut que deux messages soient reçus en même temps, générant ainsi des problèmes)
                        fond.coords(joueurs[1], float(reponse[0]),float(reponse[1]),float(reponse[2]),float(reponse[3]))     #actualise les coordonnées de la barre du joueur 1   

                    fenetre_pong.update()
            
                

        if typej == 2:
            sc = socket(AF_INET,SOCK_STREAM)     
            sc.connect(("localhost",50004))
        
            direction_balle_y = 7                                           #la balle bouge, la partie commence
            direction_balle_x = 7                                           

            while fin:
                    sc.send(str(fond.coords(joueurs[1])).encode("utf8"))       #envoie les coordonnées de la barre du joueur 2      
                    reponsebrut=sc.recv(1024).decode("utf8").split(",")        #réception du message du joueur 1 en le décodant contenant les coordonnées de la barre ce dernier, celles de la balle et le score
                    
                    coords=[]
                    for coordsbrut in reponsebrut :                            #nettoie le message
                        coords.append(re.sub("\[|\]","",coordsbrut).split(","))


                    if len(coords)==10:                                        #si le message est de longueur 10 (il se peut que deux messages soient reçus en même temps, générant ainsi des problèmes)
                        fond.coords(joueurs[0], float(coords[0][0]), float(coords[1][0]), float(coords[2][0]), float(coords[3][0]))        #actualise les coordonnées de la barre du joueur 2
                        fond.coords(balle, float(coords[4][0]), float(coords[5][0]), float(coords[6][0]), float(coords[7][0]))             #actualise les coordonnées de la balle

                        if int(coords[8][0]) != score[0]  or int(coords[9][0]) != score[1]:                                                #si le score reçu est différent du score actuel, la suite du code va alors actualiser ce dernier
                            score[0], score[1] = int(coords[8][0]), int(coords[9][0])
                            fond.delete(affichage_score)
                            affichage_score = fond.create_text(750,50, text=(str(score[0]),":",str(score[1])), fill="white", font=("Raleway",30,"bold"))     #actualise le score

                    fenetre_pong.update()
        

    
    
    if mode == 1:
        thread = threading.Thread(target=multi)         
        thread.start()                              #démarre le thread afin que le processus de connexion tourne en parallèle et ne bloque pas le code
    else :
        mouvement_joueurs_et_balle()                #si les joueurs jouent sur le même appareil, la partie commence



    fenetre_pong.bind("<KeyPress>", key_down)  
    fenetre_pong.bind("<KeyRelease>",key_up) 

def selection_joueurs():
    global bouton_joueur_1,bouton_joueur_2
    bouton_meme_ordinateur.destroy()
    bouton_deux_ordinateur.destroy()
    bouton_joueur_1 = Button(fenetre_pong,width=50, height= 50, command = lambda:[joueur_un(),commencement_jeu()], bg='blue',text= 'joueur 1')
    bouton_joueur_2 = Button(fenetre_pong,width=50, height= 50, command = lambda:[joueur_deux(),commencement_jeu()], bg='red',text = 'joueur 2')
    bouton_joueur_1.grid(column = 0, row = 0)
    bouton_joueur_2.grid(column = 1, row = 0)

def meme_ordinateur():
    global mode
    mode = 0
    

def deux_ordinateur():
    global mode
    mode = 1
def joueur_un():
    global typej
    typej = 1
def joueur_deux():
    global typej
    typej = 2
def destruction():
    bouton_meme_ordinateur.destroy()
    bouton_deux_ordinateur.destroy()

bouton_meme_ordinateur = Button(fenetre_pong,width=50, height= 50, command = lambda:[destruction(),meme_ordinateur(),commencement_jeu()], bg='blue',text= 'même ordinateur')
bouton_deux_ordinateur = Button(fenetre_pong,width=50, height= 50, command = lambda:[deux_ordinateur(),selection_joueurs()], bg='red',text = 'local')
bouton_meme_ordinateur.grid(column = 0, row = 0)
bouton_deux_ordinateur.grid(column = 1, row = 0)
fenetre_pong.mainloop()