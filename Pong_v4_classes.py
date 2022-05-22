from tkinter import *
from time import *
from socket import socket, AF_INET, SOCK_STREAM
import threading
import random
import re


class Pong():

    def __init__(self):

        self.fenetre_pong = Toplevel()

        self.bouton_meme_ordinateur = Button(self.fenetre_pong,width=50, height= 50, command = lambda:[self.destruction(),self.meme_ordinateur(),self.commencement_jeu(),self.mouvement_joueurs_et_balle()], bg='blue',text= 'même ordinateur')
        self.bouton_deux_ordinateur = Button(self.fenetre_pong,width=50, height= 50, command = lambda:[self.deux_ordinateur(),self.selection_joueurs()], bg='red',text = 'local')
        self.bouton_meme_ordinateur.grid(column = 0, row = 0)
        self.bouton_deux_ordinateur.grid(column = 1, row = 0)
        
        self.balle_x = 750
        self.balle_y = 400
        self.direction_balle_y = 4
        self.direction_balle_x = 4
        self.k=0

        if self.fenetre_pong.winfo_screenheight()>800:
            self.largeur_fenetre = 1500
            self.hauteur_fenetre = 800
        else:
            self.largeur_fenetre = 1200
            self.hauteur_fenetre = 650

        self.deplacement_joueurs = {'z':['-10','0'],'s':['10','0'],'o':['-10','1'],'l':['10','1']}  #dictionnaire des touches, de son déplacement et du joueur qu'elle déplace
        self.liste_touches = []  #les touches actuellement pressées
        self.score = [0,0]
        
        self.fenetre_pong.mainloop()


    def commencement_jeu(self):
        
        
        self.fond = Canvas(self.fenetre_pong, width=self.largeur_fenetre, height = self.hauteur_fenetre, background = "black")

        self.joueur_1_rectangle = self.fond.create_rectangle(50,(self.hauteur_fenetre/2-100),70,(self.hauteur_fenetre/2+100), fill ="blue")
        self.joueur_2_rectangle = self.fond.create_rectangle(self.largeur_fenetre-100,self.hauteur_fenetre/2-100,self.largeur_fenetre-80,self.hauteur_fenetre/2+100, fill ="white")
        self.balle = self.fond.create_oval(self.balle_x,self.balle_y,self.balle_x+20,self.balle_y+20, fill='white')
        self.joueurs=[self.joueur_1_rectangle,self.joueur_2_rectangle]
          
        self.fond.grid(column = 0, row = 0)
        self.affichage_score = self.fond.create_text(self.largeur_fenetre/2,50, text=(str(self.score[0]),":",str(self.score[1])), fill="white", font=("Raleway",30,"bold"))#affichage du score
        
        self.fenetre_pong.bind("<KeyPress>", self.key_down)  
        self.fenetre_pong.bind("<KeyRelease>", self.key_up)


    def key_down(self, e): #fonction qui regarde si la touche est déjà presséee, sinon l'ajoute dans liste_touches 
    
            if e.keysym not in self.liste_touches :
                if e.keysym in self.deplacement_joueurs:
                    self.liste_touches.append(e.keysym)
                    

    def key_up(self, e): #fonction qui regarde lorsqu'une touche est relachée si elle est dans liste_touche et si oui l'enlève de liste_touche
            if e.keysym in self.liste_touches:
                self.liste_touches.remove(e.keysym)


    def rebondissement_balle(self):        #gère les rebonds de la balle
           
            self.angle=random.uniform(0.5, 1.5)
            
            if self.mode == 0 or self.typej == 1:
                if self.fond.coords(self.joueurs[0])[1]<=self.fond.coords(self.balle)[1]<=self.fond.coords(self.joueurs[0])[3] and self.fond.coords(self.balle)[0]<=self.fond.coords(self.joueurs[0])[2]: #lorsque la balle touche le joueur 1
                    if self.fond.coords(self.balle)[1]<=(self.fond.coords(self.joueurs[0])[3] - self.fond.coords(self.joueurs[0])[1])/2 + self.fond.coords(self.joueurs[0])[1]:                 #lorsque la balle touche la partie haute du joueur 1
                        self.balle_x = self.fond.coords(self.joueurs[0])[2]
                        self.k+=0.1                                                                  #variable permettant d'augmenter ou diminuer la vitesse de la balle à chaque rebond sur le joueur 1                                
                        self.direction_balle_x = (-self.direction_balle_x+self.k)                              #renvoie la balle dans le sens opposé de l'arrivée
                        self.direction_balle_y = -abs((self.direction_balle_y+self.k)*self.angle)                   #renvoie la balle systématiquement vers le haut avec un angle aléatoire (l'angle est modifié en modifiant la composante y du vecteur vitesse de la balle)
                    
                    elif (self.fond.coords(self.joueurs[0])[3] - self.fond.coords(self.joueurs[0])[1])/2 + self.fond.coords(self.joueurs[0])[1] < self.fond.coords(self.balle)[1]: #lorsque la balle touche la partie basse du joueur 1
                        self.balle_x=self.fond.coords(self.joueurs[0])[2]
                        self.k+=0.1
                        self.direction_balle_x = (-self.direction_balle_x+self.k)
                        self.direction_balle_y = abs((self.direction_balle_y+self.k)*self.angle)                                                               #renvoie la balle systématiquement vers le bas avec un angle aléatoire

                
                elif self.fond.coords(self.joueurs[1])[1]<=self.fond.coords(self.balle)[1]<=self.fond.coords(self.joueurs[1])[3] and self.fond.coords(self.joueurs[1])[0]<=self.fond.coords(self.balle)[0]: #lorsque la balle touche le joueur 2
                    if self.fond.coords(self.balle)[1] <= (self.fond.coords(self.joueurs[1])[3] - self.fond.coords(self.joueurs[1])[1])/2 + self.fond.coords(self.joueurs[1])[1]:                 #lorsque la balle touche la partie haute du joueur 2
                        self.balle_x=self.fond.coords(self.joueurs[1])[0]
                        self.k+=0.2  
                        self.direction_balle_x = (-self.direction_balle_x-self.k) 
                        self.direction_balle_y = -abs((self.direction_balle_y+self.k)*self.angle)
                    
                    elif self.fond.coords(self.balle)[1] > (self.fond.coords(self.joueurs[1])[3] - self.fond.coords(self.joueurs[1])[1])/2 + self.fond.coords(self.joueurs[1])[1]:                #lorsque la balle touche la partie basse du joueur 2
                        self.balle_x=self.fond.coords(self.joueurs[1])[0]
                        self.k+=0.2     
                        self.direction_balle_x = (-self.direction_balle_x-self.k)
                        self.direction_balle_y = abs((self.direction_balle_y+self.k)*self.angle)

                elif self.fond.coords(self.balle)[0] > (self.largeur_fenetre - 20): #si la balle dépasse le joueur 2 
                   
                    self.score[0] += 1
                    self.balle_x = 750               #réinitialise les coordonnées de la balle
                    self.balle_y = 400           
                    self.direction_balle_x = -7      #réinitialise la composante x du vecteur vitesse de la balle
                    self.direction_balle_y = 7       #                           y 
                    self.k=0

                elif self.fond.coords(self.balle)[0]<20:  #si la balle dépasse le joueur 1
                    self.balle_x = 750
                    self.balle_y = 400
                    self.direction_balle_x = 7
                    self.direction_balle_y = 7
                    self.score[1] += 1
                    self.k=0

                elif self.fond.coords(self.balle)[1]>self.hauteur_fenetre-self.direction_balle_y:       #si la balle cogne le bas
                    self.direction_balle_y = -self.direction_balle_y*random.uniform(0.3,1.1)  #renvoie la balle avec un angle aléatoire (angle tout de même limité)

                elif self.fond.coords(self.balle)[1]<0-self.direction_balle_y:                     #si la balle cogne le haut
                    self.direction_balle_y = -self.direction_balle_y*random.uniform(0.3,1.1)  #renvoie la balle avec un angle aléatoire (angle tout de même limité)
                
            

    def mouvement_joueurs_et_balle(self, *args): 
   
        
            for self.touche in self.liste_touches:                                                                             #pour toutes le touches pressées actuellement, déplace les joueurs en fonction de la touche pressées
                if int(self.deplacement_joueurs[self.touche][0])<0 :                                                           #si on déplace la barre vers le haut
                    if self.fond.coords(self.joueurs[int(self.deplacement_joueurs[self.touche][1])])[1]> 5:   
                        if self.mode == 1 and self.typej == 1 and int(self.deplacement_joueurs[self.touche][1]) == 0:                    #si la barre ne va pas en dehors de la fenetre et qu'on joue en local et que le joueur est le numéro 1
                            self.fond.move(self.joueurs[int(self.deplacement_joueurs[self.touche][1])],0,self.deplacement_joueurs[self.touche][0]) #déplace le joueur
                        elif self.mode == 1 and self.typej == 2 and int(self.deplacement_joueurs[self.touche][1]) == 1:
                            self.fond.move(self.joueurs[int(self.deplacement_joueurs[self.touche][1])],0,self.deplacement_joueurs[self.touche][0])
                        elif self.mode == 0:                                                                              #si on joue sur le même appareil
                            self.fond.move(self.joueurs[int(self.deplacement_joueurs[self.touche][1])],0,self.deplacement_joueurs[self.touche][0])
                
                elif self.fond.coords(self.joueurs[int(self.deplacement_joueurs[self.touche][1])])[3]<self.hauteur_fenetre:                   #même chose mais cette fois-ci, si on déplace la barre vers le bas
                    if self.mode == 1 and self.typej == 1 and int(self.deplacement_joueurs[self.touche][1]) == 0 :
                        self.fond.move(self.joueurs[int(self.deplacement_joueurs[self.touche][1])],0,self.deplacement_joueurs[self.touche][0])

                    elif self.mode == 1 and self.typej == 2 and int(self.deplacement_joueurs[self.touche][1]) == 1 :
                        self.fond.move(self.joueurs[int(self.deplacement_joueurs[self.touche][1])],0,self.deplacement_joueurs[self.touche][0])
                    
                    elif self.mode == 0 :
                        self.fond.move(self.joueurs[int(self.deplacement_joueurs[self.touche][1])],0,self.deplacement_joueurs[self.touche][0])  
            
          
            self.balle_y += self.direction_balle_y                                    #modifie la variable donnant les coordonnées de la balle
            self.balle_x += self.direction_balle_x
            self.fond.coords(self.balle,self.balle_x,self.balle_y,self.balle_x+20,self.balle_y+20)        #réactualise la position de la balle
            self.rebondissement_balle()
            
            if self.mode == 0 or self.typej == 1:
                self.fond.delete(self.affichage_score)                                    #supprime le score pour le remettre et éviter la superposition de deux score où l'absence d'actualisation
                self.affichage_score = self.fond.create_text(750,50, text=(str(self.score[0]),":",str(self.score[1])), fill="white", font=("Raleway",30,"bold"))
            self.fenetre_pong.after(10,self.mouvement_joueurs_et_balle)
            

    def multi(self):
            
            self.bouton_joueur_1.destroy()
            self.bouton_joueur2.destroy()
            print("\n***********************************\n") 
            self.fin=True
            self.balle_x = 750           #initialise les coordonnées de la balle
            self.balle_y = 400
            self.direction_balle_y = 0   #initialise les coordonnées du vecteur vitesse de la balle
            self.direction_balle_x = 0
            self.mouvement_joueurs_et_balle()
            

            if self.typej == 1:                        #si le joueur est de numéro 1
                self.ss = socket(AF_INET,SOCK_STREAM)
                self.ss.bind(("localhost",50004))
                self.ss.listen(1)
                self.connexion=True
                

                while self.connexion:
                    print("\n***********************************\n")
                    print("\nEn attente d'un joueur...\n")
                    self.client, self.adresse= self.ss.accept()       #établit la connexion avec l'appareil du joueur de numéro 2
                    print("\n***********************************\n")
                    print("Client {} connecté".format(self.adresse))
                    print("\n***********************************\n")
            
                    self.direction_balle_y = 7   #la balle bouge, la partie commence
                    self.direction_balle_x = 7
                    
                    while self.fin:
                        self.client.send((str(self.fond.coords(self.joueurs[0]))+","+str(self.fond.coords(self.balle))+","+str(self.score)).encode("utf8"))    #envoie les coordonnées de la barre du joueur 1, de la balle et le score
                        self.reponsebrut = self.client.recv(1024).decode("utf8")                                                           #réception du message du joueur 2 en le décodant contenant les coordonnées de la barre ce dernier                                     
                        self.reponse = re.sub("\[|\]","",self.reponsebrut).split(", ")                                                     #nettoie le message
                    
                        if len(self.reponse)==4:                                                                                      #si le message est de longueur 4 (il se peut que deux messages soient reçus en même temps, générant ainsi des problèmes)
                            self.fond.coords(self.joueurs[1], float(self.reponse[0]),float(self.reponse[1]),float(self.reponse[2]),float(self.reponse[3]))     #actualise les coordonnées de la barre du joueur 1   

                        self.fenetre_pong.update()
                
                    

            if self.typej == 2:
                self.sc = socket(AF_INET,SOCK_STREAM)     
                self.sc.connect(("localhost",50004))
            
                self.direction_balle_y = 7                                           #la balle bouge, la partie commence
                self.direction_balle_x = 7                                           

                while self.fin:
                        self.sc.send(str(self.fond.coords(self.joueurs[1])).encode("utf8"))       #envoie les coordonnées de la barre du joueur 2      
                        self.reponsebrut=self.sc.recv(1024).decode("utf8").split(",")        #réception du message du joueur 1 en le décodant contenant les coordonnées de la barre ce dernier, celles de la balle et le score
                        
                        self.coords=[]
                        for self.coordsbrut in self.reponsebrut :                            #nettoie le message
                            self.coords.append(re.sub("\[|\]","",self.coordsbrut).split(","))


                        if len(self.coords)==10:                                        #si le message est de longueur 10 (il se peut que deux messages soient reçus en même temps, générant ainsi des problèmes)
                            self.fond.coords(self.joueurs[0], float(self.coords[0][0]), float(self.coords[1][0]), float(self.coords[2][0]), float(self.coords[3][0]))        #actualise les coordonnées de la barre du joueur 2
                            self.fond.coords(self.balle, float(self.coords[4][0]), float(self.coords[5][0]), float(self.coords[6][0]), float(self.coords[7][0]))             #actualise les coordonnées de la balle

                            if int(self.coords[8][0]) != self.score[0]  or int(self.coords[9][0]) != self.score[1]:                                                #si le score reçu est différent du score actuel, la suite du code va alors actualiser ce dernier
                                self.score[0], self.score[1] = int(self.coords[8][0]), int(self.coords[9][0])
                                self.fond.delete(self.affichage_score)
                                self.affichage_score = self.fond.create_text(750,50, text=(str(self.score[0]),":",str(self.score[1])), fill="white", font=("Raleway",30,"bold"))     #actualise le score

                        self.fenetre_pong.update()
            

        
        

    def multiThread(self):
        self.thread = threading.Thread(target=self.multi)         
        self.thread.start()                              #démarre le thread afin que le processus de connexion tourne en parallèle et ne bloque pas le code
                     



         

    def selection_joueurs(self):
    
        self.bouton_meme_ordinateur.destroy()
        self.bouton_deux_ordinateur.destroy()
        self.bouton_joueur_1 = Button(self.fenetre_pong,width=50, height= 50, command = lambda:[self.joueur_un(),self.commencement_jeu(),self.multiThread()], bg='blue',text= 'HOST')
        self.bouton_joueur2 = Button(self.fenetre_pong,width=50, height= 50, command = lambda:[self.joueur_deux(),self.commencement_jeu(),self.multiThread()], bg='red',text = 'CLIENT')
        self.bouton_joueur_1.grid(column = 0, row = 0)
        self.bouton_joueur2.grid(column = 1, row = 0)

    def meme_ordinateur(self):
        self.mode = 0
        
    def deux_ordinateur(self):
        self.mode = 1

    def joueur_un(self):
        self.typej = 1

    def joueur_deux(self):
        self.typej = 2

    def destruction(self):
        self.bouton_meme_ordinateur.destroy()
        self.bouton_deux_ordinateur.destroy()

lancer = Pong()