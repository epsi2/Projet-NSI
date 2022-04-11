
# -- coding: utf-8 --
"""
Created on Mon Apr  4 10:18:40 2022
@author: eleveSNT
"""

from tkinter import*

class Pong():

    def __init__(self):
        self.fenetrepong = Toplevel()
        self.fenetrepong.attributes('-fullscreen', True)

        if self.fenetrepong.winfo_screenheight()>800:
            self.w_f = 1500
            self.h_f = 800
        else:
            self.w_f = 1200
            self.h_f = 650

        self.fond = Canvas(self.fenetrepong, width=self.w_f, height= self.h_f, background = "black")
        self.fond.pack()

        self.play = Button(self.fenetrepong, text ="Cliquer pour jouer", width= self.w_f,height =self.h_f, command = lambda:[self.mouv_balle(),self.destruction()], bg ='blue')
        self.play.pack()

        self.joueur_un = self.fond.create_rectangle(50,350,70,500, fill ="white")
        self.joueur_deux = self.fond.create_rectangle((self.w_f - 50),350,(self.w_f - 70),500, fill ="white")

        self.balle_x = (self.w_f/2)
        self.balle_y = (self.h_f/2)
        self.direction_y = 10
        self.direction_x = 10
        self.balle = self.fond.create_oval(self.balle_x,self.balle_y,self.balle_x+30,self.balle_y+30, fill='white')
        self.score = [0,0]
        self.score_aff = self.fond.create_text((self.w_f)/2,50, text=(str(self.score[1]),":",str(self.score[0])), fill="white", font=("Raleway",30,"bold"))
        n =0
        print(self.fond.coords(self.balle)[0])
        print(self.w_f /2)

        self.btn_pause = Button(self.fenetrepong,text ="Cliquer pour mettre en pause", width= self.w_f,height =self.h_f,  bg ='blue')
        self.btn_pause.pack()

        

        self.fenetrepong.mainloop()


    def joueur_1_down(self, evt):
        self.fond.move(self.joueur_un,0,20)
    def joueur_1_up(self, evt):
        self.fond.move(self.joueur_un,0,-20)
    def joueur_2_up(self, evt):
        self.fond.move(self.joueur_deux,0,-20)
    def joueur_2_down(self, evt):
        self.fond.move(self.joueur_deux,0,20)

    def pause(self):
        self.n += 1
        while (self.n)%2 == 1:
            self.balle_y = self.h_f/2
            self.balle_x = self.w_f/2


    def destruction(self):
        self.play.destroy()
        self.btn_pause.pack()

    def mouv_balle(self):
        if self.direction_x == -10:
            self.fenetrepong.bind("z",self.joueur_1_up)
            self.fenetrepong.bind("s",self.joueur_1_down)
            self.fenetrepong.unbind("o")
            self.fenetrepong.unbind("l")
        if self.direction_x == 10:
            self.fenetrepong.bind("o",self.joueur_2_up)
            self.fenetrepong.bind("l",self.joueur_2_down)
            self.fenetrepong.unbind("z")
            self.fenetrepong.unbind("s")

        self.balle_x += self.direction_x

        self.balle_y += self.direction_y

        self.fond.coords(self.balle,self.balle_x,self.balle_y,self.balle_x+10, self.balle_y+10)

        if self.balle_y < 10 or self.balle_y > self.h_f-10:
            self.direction_y -= self.direction_y
        if self.balle_x > self.w_f-20 :
            self.direction_x-=  self.direction_x
        if ((self.fond.coords(self.balle)[0] > self.fond.coords(self.joueur_deux)[0] and self.fond.coords(self.balle)[0] < self.fond.coords(self.joueur_deux)[2] and self.fond.coords(self.balle)[1]>self.fond.coords(self.joueur_deux)[1] and self.fond.coords(self.balle)[1]<self.fond.coords(self.joueur_deux)[3]) or (self.fond.coords(self.balle)[2] > self.fond.coords(self.joueur_deux)[0] and self.fond.coords(self.balle)[2] < self.fond.coords(self.joueur_deux)[2] and self.fond.coords(self.balle)[3]>self.fond.coords(self.joueur_deux)[1] and self.fond.coords(self.balle)[3]<self.fond.coords(self.joueur_deux)[3])) or ((self.fond.coords(self.balle)[0] > self.fond.coords(self.joueur_un)[0] and self.fond.coords(self.balle)[0] < self.fond.coords(self.joueur_un)[2] and self.fond.coords(self.balle)[1]>self.fond.coords(self.joueur_un)[1] and self.fond.coords(self.balle)[1]<self.fond.coords(self.joueur_un)[3]) or (self.fond.coords(self.balle)[2] > self.fond.coords(self.joueur_un)[0] and self.fond.coords(self.balle)[2] < self.fond.coords(self.joueur_un)[2] and self.fond.coords(self.balle)[3]> self.fond.coords(self.joueur_un)[1] and self.fond.coords(self.balle)[3]<self.fond.coords(self.joueur_un)[3])):
            self.direction_x = -self.direction_x
        if self.balle_x <20 :
            self.direction_x=-self.direction_x
            self.score[0] += 1    
            self.balle_x = 150
            self.balle_y = self.h_f/2
            self.fenetrepong.update()
        if self.balle_x >self.w_f-50 :
            self.direction_x=-self.direction_x
            self.score[1] += 1 
            self.balle_x = self.w_f - 100
            self.balle_y = self.h_f/2
            self.fenetrepong.update()
        self.fond.after(50,self.mouv_balle)
        self.fond.delete(self.score_aff)
        self.score_aff = self.fond.create_text(self.w_f/2,50, text=f"{str(self.score[1])}:{str(self.score[0])}", fill="white", font=("Raleway",30,"bold"))
        
    
if __name__ == '__main__':
    jeu = Pong()

