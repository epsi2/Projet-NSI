from re import M



#importation de Tkinter
from tkinter import*

#importation de la classe pour l'enregistrement
from enregistrement import Enregistrement

#importation de la classe pour jouer au morpion
from morpion import Tictac

#fonction pour le jeu du morpion
def tictac():

    #création d'un objet de la classe Tictac
    objetmorpion = Tictac()

#fonction pour le jeu de dame À COMPLÉTER
def dame():
    pass 

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

#création du bouton pour lancer le jeu de dame
damebutton = Button(damecanvas, bg="#049300", text="jouer au jeu de dame", command=dame)
damebutton.place(x=100, y=0)

#création de l'image du jeu de dame dans le canvas
dameimage = PhotoImage(file="images/jeu-de-dame.gif")
damecanvas.create_image(0, 0, image = dameimage, anchor = NW)

#création du canvas pour le jeu de dame
ticcanvas = Canvas(maincanvas)
ticcanvas.place(x= 600, y=40)
 
#création du bouton pour lancer le morpion
ticbutton = Button(ticcanvas, bg="#049300", text="jouer au morpion", command=tictac)
ticbutton.place(x=0, y=0)

#création de l'image du morpion dans le canvas
ticimage = PhotoImage(file="images/tictacimage.gif")
ticcanvas.create_image(0, 0, image = ticimage, anchor = NW)


mainwindow.mainloop()