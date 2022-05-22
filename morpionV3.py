from tkinter import Canvas,Tk,Button, Toplevel
from collections import Counter
from socket import socket, AF_INET, SOCK_STREAM
import time
import threading

class Morpion():

    def __init__(self):

        self.fenetre = Toplevel()

        self.X=[]
        self.O=[]
        self.case= {"0":(100,100,0,0),"1":(300,100,1,0),"2":(500,100,2,0),"3":(100,300,0,1),"4":(300,300,1,1),"5":(500,300,2,1),"6":(100,500,0,2),"7":(300,500,1,2),"8":(500,500,2,2)}
        self.cases=[0,1,2,3,4,5,6,7,8]   
        self.tour=1
        self.tourmulti=1
        self.mode=0

     
        self.bouton_commencement_jeu = Button(self.fenetre,width=50, height= 50, command = lambda:[self.destruction(),self.meme_ordinateur(),self.commencement_jeu()], bg='blue',text= 'même ordinateur')
        self.bouton_deux_ordinateurs = Button(self.fenetre,width=50, height= 50, command = lambda:[self.deux_ordinateurs(),self.selection_joueurs()], bg='red',text = 'local')
        self.bouton_commencement_jeu.grid(column = 0, row = 0)
        self.bouton_deux_ordinateurs.grid(column = 1, row = 0)

        self.fenetre.mainloop()



    def commencement_jeu(self):

        self.princ = Canvas(self.fenetre, width=600, height= 600, background = "red")
        self.linge1 = self.princ.create_line(200,0,200,600,fill="white")
        self.ligne2 = self.princ.create_line(400,0,400,600,fill="white")
        self.ligne3 = self.princ.create_line(0,200,600,200,fill="white")
        self.ligne4 = self.princ.create_line(0,400,600,400,fill="white")

        self.princ.grid(column = 0,row=0)

        self.fenetre.bind("<Button-1>", self.jeu)

                    
    def victoire(self, joueur):  #vérifie la victoire d'un joueur

        self.joueur_triee=sorted(joueur)     
    
        if len(self.joueur_triee)>=3:   #après que trois cases ont été chosies
            self.num_ligne_joueur=[]
            for self.num in self.joueur_triee:              
                self.num_ligne_joueur.append(self.case[str(self.num)][3])  #permet d'ajouter le numéro de la ligne correspondant à la case
                
            self.num_colonne_joueur=[]

            for self.num in self.joueur_triee:
                self.num_colonne_joueur.append(self.case[str(self.num)][2]) #permet d'ajouter le numéro de la colonne correspondant à la case
                
            
            if Counter(self.num_ligne_joueur).most_common(1)[0][1]==3:  #vérfie le nombre d'occurrences d'un même numéro de ligne et indique que la partie est finie si le nombre atteint 3
                return False

            elif Counter(self.num_colonne_joueur).most_common(1)[0][1]==3:  #vérfie le nombre d'occurrences d'un même numéro de colonne et indique que la partie est finie si le nombre atteint 3
                return False 

            elif 6 in self.joueur_triee and 4 in self.joueur_triee and 2 in self.joueur_triee: #vérifie si le joueur a la diagonale d'en haut à droite jusqu'en bas à gauche
                return False

            elif 8 in self.joueur_triee and 4 in self.joueur_triee and 0 in self.joueur_triee: #vérifie si le joueur a la diagonale d'en haut à gauche jusqu'en bas à droite
                return False

            else:
                return True
            
        else :
            return True


    def affvict(self):

        if len(self.X)==5 and self.victoire(self.X) == True:    
                self.princ.create_text(300, 285, text="Match nul", fill="#1c784b", font=("Raleway",20,"bold"))    
        
        elif self.victoire(self.X)==False:
                self.princ.create_text(300, 285, text="Le joueur X a gagné", fill="#1c784b", font=("Raleway",20,"bold"))  
        
        elif self.victoire(self.O)==False:
                self.princ.create_text(300, 285, text="Le joueur O a gagné", fill="#1c784b", font=("Raleway",20,"bold"))  
        
        else:
                self.princ.create_text(300, 285, text="Erreur", fill="white", font=("Raleway",20,"bold")) 
        self.ss.close() 

            
    def jeu(self, evt):

        self.ymax=200   #coordonnée y supérieure de la case
        self.ymin=0     #coordonnée y inférieure de la case

        if self.tour %2 == 1 and self.tourmulti%2 == 1 or self.tour%2 == 1 and self.mode==0 :  #si c'est au tour du joueur 1 de jouer (que ce soit en réseau ou sur le même appreil)
  
            for i, j, k in zip(list(range(9)), list(range(200, 601, 200))*3, list(range(0, 401, 200))*3):  #l'itérateur i est la case correspondant aux coordonnées x supérieure et x inférieure de la case (itérateur j et k)  
                self.ymax += 200/3    #augmente la coordonnée y maximale de la case de sorte qu'elle ait augmenté de 200 à la fin d'une ligne
                self.ymin += 200/3
                if evt.x<j and evt.x>k and evt.y<200*(self.ymax//201) and evt.y>200*(self.ymin//201) and i not in self.O: #vérifie si les coordonnées du clic se situent entre les coordonnées min et max de x et y de la case. Si c'est le cas, on ajoute l'itérateur i à la liste du joueur.
                    self.X.append(i)
            
            self.tourmulti += 1 

        elif self.tour%2 == 0 and self.tourmulti%2 == 1 or self.tour%2 == 0 and self.mode==0 : #si c'est au tour du joueur 2 de jouer (que ce soit en réseau ou sur le même appreil)
            
            for i, j, k in zip(list(range(9)), list(range(200, 601, 200))*3, list(range(0, 401, 200))*3):
                self.ymax+= 200/3
                self.ymin+= 200/3
                if evt.x<j and evt.x>k and evt.y<200*(self.ymax//201) and evt.y>200*(self.ymin//201) and i not in self.X :
                    self.O.append(i)

            self.tourmulti += 1
    

        if self.victoire(self.X)==True and self.victoire(self.O)==True and len(self.X)!=5:  #si personne n'a gagnée ou toutes les cases sont remplies
            
            if self.tour%2 ==1:
                self.princ.create_text(self.case[str(self.X[-1])][0], self.case[str(self.X[-1])][1], text="X", fill="white", font=("Raleway",100,"bold")) #affiche une croix où le joueur a cliqué
                self.cases.remove(int(self.X[-1])) #enlève la case choisie par le joueur de la liste des cases disponibles
                self.victoire(self.X)
                self.fenetre.update()
                
                if self.mode == 0:
                    self.tour += 1
                    self.princ.configure(bg='blue')
                print(self.X)

            else: 
                time.sleep(0.1)
                self.princ.create_text(self.case[str(self.O[-1])][0], self.case[str(self.O[-1])][1], text="O", fill="white", font=("Raleway",100,"bold"))
                self.victoire(self.O)
                self.cases.remove(int(self.O[-1]))
                self.fenetre.update()
                if self.mode == 0:
                    self.tour += 1
                    self.princ.configure(bg='red')
                print(self.O)

        else:
            self.affvict()  




    def multi(self):

        self.bouton_joueur1.destroy()
        self.bouton_joueur2.destroy()
        print("\n***********************************\n")
        self.fin = True
        self.adresse_serveur = ("localhost", 50004)

        if self.typej == 1:    #si le joueur est serveur

            self.tour = 1
            self.tourmulti = 1 
            self.ss = socket(AF_INET,SOCK_STREAM)
            self.ss.bind(self.adresse_serveur)
            self.ss.listen(1)
            self.connexion=True
            

            while self.connexion:

                print("\nEn attente d'un joueur...\n")
                self.client, adresse= self.ss.accept()
                print("\n***********************************\n")
                print("self.client {} connecté".format(adresse))
                print("\n***********************************\n")

                while self.fin:             #tant que la pertie n'est pas finie, envoie continuellement la dernière case chosie par le joueur serveur
                    
                    if len(self.X) == 0:
                        self.client.send("test".encode("utf8"))
                    
                    else:
                        self.client.send(str(self.X[-1]).encode("utf8"))

                    self.reponse = self.client.recv(1024).decode("utf8")
                    
                        
                    if self.reponse != "test" and self.reponse !="testtest":  #si le message reçu ne signifie pas que la liste des cases du joueur client est vide
                        
                        if len(self.O) == 0:    #si la liste des cases du joueur client chez le joueur serveur est vide
                            self.O.append(int(self.reponse))
                            self.princ.create_text(self.case[str(self.O[-1])][0], self.case[str(self.O[-1])][1], text="O", fill="white", font=("Raleway",100,"bold"))
                            self.tourmulti += 1
                            
                        if int(self.reponse) != self.O[-1]: #si le numéro de case reçu ne correspond pas au dernier numéro de la liste de cases du joueur client
                            self.O.append(int(self.reponse))
                            self.princ.create_text(self.case[str(self.O[-1])][0], self.case[str(self.O[-1])][1], text="O", fill="white", font=("Raleway",100,"bold"))
                            self.tourmulti += 1
                            

                    if self.victoire(self.X)!=True or self.victoire(self.O)!=True or len(self.X)==5:
                        self.affvict()   
                    
                    if self.tourmulti%2 == 1:           #change le tour et change la couleur de fond
                        self.princ.configure(bg='blue')
                        self.fenetre.update()
                    else :
                        self.princ.configure(bg='red')
                        self.fenetre.update()
                

        if self.typej == 0:   #si le joueur est client
            
            self.tour = 0
            self.tourmulti = 0
            self.sc = socket(AF_INET,SOCK_STREAM)     
            self.sc.connect(self.adresse_serveur)

            while self.fin:
                    if len(self.O) == 0:  #si la liste de cases du joueur client est vide, envoyer "test"
                        self.sc.send("test".encode("utf8"))
                    else:                                           #sinon envoyer continuellement le dernier élément de la liste de cases du joueur client
                        self.sc.send(str(self.O[-1]).encode("utf8")) 
                        
                    self.reponse = self.sc.recv(1024).decode("utf8")

                    if self.reponse != "test" and self.reponse !="testtest": #si le message reçu ne signifie pas que la liste des cases du joueur serveur est vide
                        if len(self.X) == 0:   #si la liste des cases du joueur serveur chez le joueur client est vide
                            self.X.append(int(self.reponse))
                            self.princ.create_text(self.case[str(self.X[-1])][0], self.case[str(self.X[-1])][1], text="X", fill="white", font=("Raleway",100,"bold"))
                            self.tourmulti += 1

                        if int(self.reponse) != self.X[-1]:  #si le numéro de case reçu ne correspond pas au dernier numéro de la liste de cases du joueur client
                            self.X.append(int(self.reponse))
                            self.princ.create_text(self.case[str(self.X[-1])][0], self.case[str(self.X[-1])][1], text="X", fill="white", font=("Raleway",100,"bold"))
                            self.tourmulti += 1
                        
                    if self.victoire(self.X)!=True or self.victoire(self.O)!=True or len(self.X)==5:
                        self.affvict(self.X, self.O, self.princ)
                    
                    if self.tourmulti%2 == 1:
                        self.princ.configure(bg='red')
                        self.fenetre.update()
                    else :
                        self.princ.configure(bg='blue')
                        self.fenetre.update()
            

     

    def threadMulti(self):  #permet de faire tourner la partie multijoueur (envoi et réception des numéros de case) en parallèle
        self.thread = threading.Thread(target=self.multi)
        self.thread.start()
          

    def selection_joueurs(self):
        self.bouton_commencement_jeu.destroy()
        self.bouton_deux_ordinateurs.destroy()

        self.bouton_joueur1 = Button(self.fenetre,width=50, height= 50, command = lambda:[self.joueur_un(),self.commencement_jeu(),self.threadMulti()], bg='blue',text= 'CLIENT')
        self.bouton_joueur2 = Button(self.fenetre,width=50, height= 50, command = lambda:[self.joueur_deux(),self.commencement_jeu(),self.threadMulti()], bg='red',text = 'HOST')
        
        self.bouton_joueur1.grid(column = 0, row = 0)
        self.bouton_joueur2.grid(column = 1, row = 0)
        
    def meme_ordinateur(self):
        self.mode = 0
        

    def deux_ordinateurs(self):
        self.mode = 1

    def joueur_un(self):
        self.typej = 0

    def joueur_deux(self):
        self.typej = 1

    def destruction(self):
        self.bouton_commencement_jeu.destroy()
        self.bouton_deux_ordinateurs.destroy()
        



lancer = Morpion()