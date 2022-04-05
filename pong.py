# -- coding: utf-8 --
"""
Created on Mon Apr  4 10:18:40 2022

@author: eleveSNT
"""

from tkinter import Canvas,Tk
import time
fenetrepong = Tk()
fond = Canvas(fenetrepong, width=1500, height= 800, background = "black")
fond.pack()
def joueur_1_down(evt):
    fond.move(joueur_un,0,20)
def joueur_1_up(evt):
    fond.move(joueur_un,0,-20)
def joueur_2_up(evt):
    fond.move(joueur_deux,0,-20)
def joueur_2_down(evt):
    fond.move(joueur_deux,0,20)
    
joueur_un = fond.create_rectangle(50,350,70,500, fill ="white")
joueur_deux = fond.create_rectangle(1400,350,1420,500, fill ="white")

balle_x = 750
balle_y = 400
direction_y = 30
direction_x = 30
balle = fond.create_oval(balle_x,balle_y,balle_x+30,balle_y+30, fill='white')
score = [0,0]
score_aff = fond.create_text(750,50, text=(str(score[1]),":",str(score[0])), fill="white", font=("Raleway",30,"bold"))

fenetrepong.bind("z",joueur_1_up)
fenetrepong.bind("s",joueur_1_down)
fenetrepong.bind("o",joueur_2_up)
fenetrepong.bind("l",joueur_2_down)

def mouv_balle():
    global balle_x, balle_y, direction_x ,direction_y,score,score_aff


    balle_x += direction_x

    balle_y += direction_y

    fond.coords(balle,balle_x,balle_y,balle_x+10,balle_y+10)

    if balle_y < 10 or balle_y > 790:
        direction_y =-direction_y
    if balle_x > 1490 :
        direction_x=-direction_x
    if ((fond.coords(balle)[0] > fond.coords(joueur_deux)[0] and fond.coords(balle)[0] < fond.coords(joueur_deux)[2] and fond.coords(balle)[1]>fond.coords(joueur_deux)[1] and fond.coords(balle)[1]<fond.coords(joueur_deux)[3]) or (fond.coords(balle)[2] > fond.coords(joueur_deux)[0] and fond.coords(balle)[2] < fond.coords(joueur_deux)[2] and fond.coords(balle)[3]>fond.coords(joueur_deux)[1] and fond.coords(balle)[3]<fond.coords(joueur_deux)[3])) or ((fond.coords(balle)[0] > fond.coords(joueur_un)[0] and fond.coords(balle)[0] < fond.coords(joueur_un)[2] and fond.coords(balle)[1]>fond.coords(joueur_un)[1] and fond.coords(balle)[1]<fond.coords(joueur_un)[3]) or (fond.coords(balle)[2] > fond.coords(joueur_un)[0] and fond.coords(balle)[2] < fond.coords(joueur_un)[2] and fond.coords(balle)[3]>fond.coords(joueur_un)[1] and fond.coords(balle)[3]<fond.coords(joueur_un)[3])):
        direction_x = -direction_x
    if balle_x <20 :
        direction_x=-direction_x
        score[0] += 1    
        balle_x = 150
        balle_y = 400
        fenetrepong.update()
    if balle_x >1450 :
        direction_x=-direction_x
        score[1] += 1 
        balle_x = 1300
        balle_y = 400
        fenetrepong.update()
    fond.after(50,mouv_balle)
    fond.delete(score_aff)
    score_aff = fond.create_text(750,50, text=(str(score[1]),":",str(score[0])), fill="white", font=("Raleway",30,"bold"))

mouv_balle()
    

fenetrepong.mainloop()