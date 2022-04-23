
from tkinter import*
from time import *
import threading

fenetre_pong = Tk()
hauteur_fenetre = 800
largeur_fenetre = 1500
fond = Canvas(fenetre_pong, width=largeur_fenetre, height= hauteur_fenetre, background = "black")


joueur_1_rectangle = fond.create_rectangle(50,(hauteur_fenetre/2-100),70,(hauteur_fenetre/2+100), fill ="blue")
joueur_2_rectangle = fond.create_rectangle(largeur_fenetre-100,hauteur_fenetre/2-100,largeur_fenetre-80,hauteur_fenetre/2+100, fill ="white")
joueurs=[joueur_1_rectangle,joueur_2_rectangle]

balle_x = 750
balle_y = 400
balle = fond.create_oval(balle_x,balle_y,balle_x+20,balle_y+20, fill='white')
direction_balle_y = 5
direction_balle_x = 5

fond.pack()

deplacement_joueurs = {'z':['-10','0'],'s':['10','0'],'o':['-10','1'],'l':['10','1']}  #dictionnaire des touches, de son déplacement et du joueur qu'elle déplace
liste_touches = []  #les touches actuellement pressées
liste_deplacement = ['z','s','o','l'] #les touches pouvant bouger les joueurs



def key_down(e): #fonction qui regarde si la touche est déjà presséee, sinon l'ajoute dans liste_touches 
    if e.keysym not in liste_touches :
        if e.keysym in liste_deplacement:
            liste_touches.append(e.keysym)
            print(liste_touches)

def key_up(e): #fonction qui regarde lorsqu'une touche est relachée si elle est dans liste_touche et si oui l'enlève de liste_touche
    if e.keysym in liste_touches:
        liste_touches.remove(e.keysym)


def rebondissement_balle():#gère les rebonds de la balle
    global balle_x,balle_y,direction_balle_x,direction_balle_y
    if fond.coords(balle)[0] > (largeur_fenetre - 20):
        balle_x = 750
        balle_y = 400
    elif fond.coords(balle)[0]<20:
        balle_x = 750
        balle_y = 400
    elif fond.coords(balle)[1]>hauteur_fenetre:
        direction_balle_y = -direction_balle_y
    elif fond.coords(balle)[1]<0:   
        direction_balle_y = -direction_balle_y
    for joueur in joueurs:
        if fond.coords(joueur)[1]<fond.coords(balle)[1]<fond.coords(joueur)[3] and fond.coords(joueur)[0]<fond.coords(balle)[0]<fond.coords(joueur)[2]:
            direction_balle_x = -direction_balle_x
    


def mouvement_joueurs_et_balle(*args): 
    global balle_x,balle_y
    for touche in liste_touches:#pour toutes le touches pressées actuellement, déplace les joueurs en fonction de la touche pressées
        if int(deplacement_joueurs[touche][0])<0:
            if fond.coords(joueurs[int(deplacement_joueurs[touche][1])])[1]> 5:
                fond.move(joueurs[int(deplacement_joueurs[touche][1])],0,deplacement_joueurs[touche][0])
        else:
            if fond.coords(joueurs[int(deplacement_joueurs[touche][1])])[3]<hauteur_fenetre:
                fond.move(joueurs[int(deplacement_joueurs[touche][1])],0,deplacement_joueurs[touche][0])
    balle_y += direction_balle_y #modifie la variable donnant les coordonnées de la balle
    balle_x += direction_balle_x
    fond.coords(balle,balle_x,balle_y,balle_x+20,balle_y+20)#réactualise la position de la balle
    rebondissement_balle()
    fenetre_pong.after(10,mouvement_joueurs_et_balle)
    

      
    
    
fenetre_pong.bind("<KeyPress>", key_down)  
fenetre_pong.bind("<KeyRelease>",key_up) 
mouvement_joueurs_et_balle()
fenetre_pong.mainloop()