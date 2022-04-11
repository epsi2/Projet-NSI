# -- coding: utf-8 --
"""
Created on Mon Apr  4 10:18:40 2022

@author: eleveSNT
"""

from tkinter import Canvas,Tk,Button
fenetrepong = Tk()
fenetrepong.attributes('-fullscreen', True)


if fenetrepong.winfo_screenheight()>800:
    w_f = 1500
    h_f = 800
else:
    w_f = 1200
    h_f = 650

fond = Canvas(fenetrepong, width=w_f, height= h_f, background = "black")
fond.pack()

play = Button(fenetrepong, text ="Cliquer pour jouer", width= w_f,height =h_f, command = lambda:[mouv_balle(),destruction()], bg ='blue')
play.pack()



def joueur_1_down(evt):
    fond.move(joueur_un,0,20)
def joueur_1_up(evt):
    fond.move(joueur_un,0,-20)
def joueur_2_up(evt):
    fond.move(joueur_deux,0,-20)
def joueur_2_down(evt):
    fond.move(joueur_deux,0,20)
    
joueur_un = fond.create_rectangle(50,350,70,500, fill ="white")
joueur_deux = fond.create_rectangle((w_f - 50),350,(w_f - 70),500, fill ="white")

balle_x = (w_f/2)
balle_y = (h_f/2)
direction_y = 10
direction_x = 10
balle = fond.create_oval(balle_x,balle_y,balle_x+30,balle_y+30, fill='white')
score = [0,0]
score_aff = fond.create_text(w_f/2,50, text=(str(score[1]),":",str(score[0])), fill="white", font=("Raleway",30,"bold"))
n =0
print(fond.coords(balle)[0])
print(w_f/2)


def pause():
    global n,balle_x,balle_y
    n += 1
    while n%2 == 1:
        balle_y = h_f/2
        balle_x = w_f/2

btn_pause = Button(fenetrepong,text ="Cliquer pour mettre en pause", width= w_f,height =h_f,  bg ='blue')
def destruction():
    play.destroy()
    btn_pause.pack()



def mouv_balle():
    global balle_x, balle_y, direction_x ,direction_y,score,score_aff
    if direction_x == -10:
        fenetrepong.bind("z",joueur_1_up)
        fenetrepong.bind("s",joueur_1_down)
        fenetrepong.unbind("o")
        fenetrepong.unbind("l")
    if direction_x == 10:
        fenetrepong.bind("o",joueur_2_up)
        fenetrepong.bind("l",joueur_2_down)
        fenetrepong.unbind("z")
        fenetrepong.unbind("s")

    balle_x += direction_x

    balle_y += direction_y

    fond.coords(balle,balle_x,balle_y,balle_x+10,balle_y+10)

    if balle_y < 10 or balle_y > h_f-10:
        direction_y =-direction_y
    if balle_x > w_f-20 :
        direction_x=-direction_x
    if ((fond.coords(balle)[0] > fond.coords(joueur_deux)[0] and fond.coords(balle)[0] < fond.coords(joueur_deux)[2] and fond.coords(balle)[1]>fond.coords(joueur_deux)[1] and fond.coords(balle)[1]<fond.coords(joueur_deux)[3]) or (fond.coords(balle)[2] > fond.coords(joueur_deux)[0] and fond.coords(balle)[2] < fond.coords(joueur_deux)[2] and fond.coords(balle)[3]>fond.coords(joueur_deux)[1] and fond.coords(balle)[3]<fond.coords(joueur_deux)[3])) or ((fond.coords(balle)[0] > fond.coords(joueur_un)[0] and fond.coords(balle)[0] < fond.coords(joueur_un)[2] and fond.coords(balle)[1]>fond.coords(joueur_un)[1] and fond.coords(balle)[1]<fond.coords(joueur_un)[3]) or (fond.coords(balle)[2] > fond.coords(joueur_un)[0] and fond.coords(balle)[2] < fond.coords(joueur_un)[2] and fond.coords(balle)[3]>fond.coords(joueur_un)[1] and fond.coords(balle)[3]<fond.coords(joueur_un)[3])):
        direction_x = -direction_x
    if balle_x <20 :
        direction_x=-direction_x
        score[0] += 1    
        balle_x = 150
        balle_y = h_f/2
        fenetrepong.update()
    if balle_x >w_f-50 :
        direction_x=-direction_x
        score[1] += 1 
        balle_x = w_f - 100
        balle_y = h_f/2
        fenetrepong.update()
    fond.after(50,mouv_balle)
    fond.delete(score_aff)
    score_aff = fond.create_text(w_f/2,50, text=(str(score[1]),":",str(score[0])), fill="white", font=("Raleway",30,"bold"))
    
 

fenetrepong.mainloop()