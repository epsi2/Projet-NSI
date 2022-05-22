from re import M



#importation de Tkinter
from tkinter import*

#importation de la classe pour l'enregistrement
from enregistrement import Enregistrement

#importation de la classe pour jouer au morpion
from morpionV2_5 import Morpion

#from pong import Pong
from pong_version_finale import Pong_class

#fonction pour le jeu du morpion
def Morpion_func():

    #création d'un objet de la classe Tictac
    objetmorpion = Morpion()

def pong_game():
    
    pong_fenetre = Tk()
    pong_fenetre.geometry("500x500")
    pong_fenetre.resizable(0,0)
    pong_game = Pong_class(pong_fenetre)
    pong_fenetre.mainloop()





#création d'un objet de la classe Enregistrement
objetenregistrement = Enregistrement()


#on crée la fenêtre du menu principal
mainwindow = Tk() 
mainwindow.title(f"bienvenue, {objetenregistrement.userName}")
mainwindow.geometry("3000x2000")

#création du canvas principal
maincanvas = Canvas(mainwindow, bg="#0493ea", width=3000, height= 2000)
maincanvas.place(x=0, y=0)

#création du canvas pour le jeu de dame
damecanvas = Canvas(maincanvas)
damecanvas.place(x= 30, y=40)


#création du canvas pour le morpion
ticcanvas = Canvas(maincanvas)
ticcanvas.place(x= 600, y=40)
 
#création du bouton pour lancer le morpion
ticbutton = Button(ticcanvas, bg="#049300", text="jouer au morpion", command=Morpion_func)
ticbutton.place(x=0, y=0)

#création de l'image du morpion dans le canvas
ticimage = PhotoImage(file="images/tictacimage.gif")
ticcanvas.create_image(0, 0, image = ticimage, anchor = NW)

#création du canvas pour le pong
pongcanvas = Canvas(maincanvas)
pongcanvas.place(x= 600, y=80)
 
#création du bouton pour lancer le pong
pongbutton = Button(pongcanvas, bg="#049300", text="jouer au pong", command=pong_game)
pongbutton.place(x=600, y=80)

#création de l'image du pong dans le canvas
pongimage = PhotoImage(file="images/hqdefault.gif")
pongcanvas.create_image(0, 0, image = pongimage, anchor = NW)




mainwindow.mainloop()