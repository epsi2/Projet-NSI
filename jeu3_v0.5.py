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
        
        

        if self.fenetre_pong.winfo_screenheight()>800:
            self.largeur_fenetre = 1500
            self.hauteur_fenetre = 800
        else:
            self.largeur_fenetre = 1200
            self.hauteur_fenetre = 650

        self.deplacement_joueurs = {'z':['-10','0','0'],'q':['0','-10','0',],'s':['10','0','0'],'d':['0','10','0'],'o':['-10','0','1'],'k':['0','-10','1',],'l':['10','0','1'],'m':['0','10','1']}  #dictionnaire des touches, de son déplacement et du joueur qu'elle déplace
        self.liste_touches = []  #les touches actuellement pressées
        self.liste_deplacement = ['z','q','s','d','o','k','l','m'] #les touches pouvant bouger les joueurs
        self.liste_barres = []
        self.score = [0,0]
        
        self.fenetre_pong.mainloop()





    def commencement_jeu(self):
        
        
        self.fond = Canvas(self.fenetre_pong, width=self.largeur_fenetre, height = self.hauteur_fenetre, background = "black")

        self.joueur_1_rectangle = self.fond.create_rectangle(50,50,100,100, fill ="blue")
        self.joueur_2_rectangle = self.fond.create_rectangle(self.largeur_fenetre-100,self.hauteur_fenetre-100,self.largeur_fenetre-50,self.hauteur_fenetre-50, fill ="white")
        self.joueurs=[self.joueur_1_rectangle,self.joueur_2_rectangle]
          
        self.fond.grid(column = 0, row = 0)
        
        self.fenetre_pong.bind("<KeyPress>", self.key_down)  
        self.fenetre_pong.bind("<KeyRelease>", self.key_up)


    def key_down(self, e): #fonction qui regarde si la touche est déjà presséee, sinon l'ajoute dans liste_touches 
    
            if e.keysym not in self.liste_touches :
                if e.keysym in self.liste_deplacement:
                    self.liste_touches.append(e.keysym)
                    print(self.liste_touches)

    def key_up(self, e): #fonction qui regarde lorsqu'une touche est relachée si elle est dans liste_touche et si oui l'enlève de liste_touche
            if e.keysym in self.liste_touches:
                self.liste_touches.remove(e.keysym)



    def mouvement_joueurs_et_barres(self):

            for self.touche in self.liste_touches: 
                self.coordj = self.fond.coords(self.joueurs[int(self.deplacement_joueurs[self.touche][1])])
                if self.coordj[0] > 5 and self.coordj[1] > 5 and self.coordj[2] < self.largeur_fenetre - 5 and self.coordj[3] < self.hauteur_fenetre - 5:
                    self.fond.move(self.joueurs[int(self.deplacement_joueurs[self.touche][2])],self.deplacement_joueurs[self.touche][1],self.deplacement_joueurs[self.touche][0])

            if len(self.liste_barres) != 0:
                for self.barre in self.liste_barres :
                    self.

            self.mouvement_joueurs_et_barres()

    def apparition_barre(self):
        
        self.coords_barrev = random.randint(0,self.largeur_fenetre-10)
        self.coords_barreh = random.randint(0,self.hauteur_fenetre-10)

        if random.randint(0,1) == 0:
            self.liste_barres.append(self.fond.create_rectangle(self.coords_barrev,0,self.coords_barrev+10,self.hauteur_fenetre, fill ="#c8c8c8"))
        
        else:
            self.liste_barres.append(self.fond.create_rectangle(0,self.coords_barreh,self.largeur_fenetre,self.coords_barreh+10, fill ="#c8c8c8"))
        


         

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