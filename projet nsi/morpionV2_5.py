from tkinter import*
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

        self.commencement_jeu()


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

        self.fenetre.bind("<KeyRelease-a>", self.jeumulti)

                    
    def victoire(self, joueur):

        self.l=sorted(joueur)     
    
        if len(self.l)>=3:
            self.c1=[]
            for self.num in self.l:
                self.c1.append(self.case[str(self.num)][3])
                
                
            self.c2=[]
            for self.num in self.l:
                self.c2.append(self.case[str(self.num)][2])
                
            
            if Counter(self.c1).most_common(1)[0][1]==3:
                return False
            elif Counter(self.c2).most_common(1)[0][1]==3:
                return False 
            elif 6 in self.l and 4 in self.l and 2 in self.l:
                return False
            elif 8 in self.l and 4 in self.l and 0 in self.l:
                return False
            else:
                return True
            
        else :
            return True


    def affvict(self):
        if len(self.X)==5 and self.self.victoire(self.X) == True:    
                self.princ.create_text(300, 285, text="Match nul", fill="#1c784b", font=("Raleway",20,"bold"))    
        elif self.victoire(self.X)==False:
                self.princ.create_text(300, 285, text="Le joueur X a gagné", fill="#1c784b", font=("Raleway",20,"bold"))  
        elif self.victoire(self.O)==False:
                self.princ.create_text(300, 285, text="Le joueur O a gagné", fill="#1c784b", font=("Raleway",20,"bold"))  
        else:
                self.princ.create_text(300, 285, text="Erreur", fill="white", font=("Raleway",20,"bold")) 
        #self.ss.close() 
            
    def jeumulti(self, event):

        if self.tour%2 == 1 and self.tourmulti%2 == 1 or self.tour%2 == 1 and self.mode==0 :    
            if event.x<200 and event.y<200 and 0 not in self.O:
                self.X.append(0)
            elif event.x>200 and event.x<400 and event.y<200 and 1 not in self.O:
                self.X.append(1)
            elif event.x>400 and event.x<600 and event.y<200 and 2 not in self.O:
                self.X.append(2)
            elif event.x<200 and event.y>200 and event.y<400 and 3 not in self.O:
                self.X.append(3) 
            elif event.x>200 and event.x<400 and event.y<400 and event.y > 200 and 4 not in self.O:
                self.X.append(4)
            elif event.x>400 and event.x<600 and event.y<400 and event.y > 200 and 5 not in self.O:
                self.X.append(5)
            elif event.x<200 and event.y>400 and event.y<600 and 6 not in self.O:
                self.X.append(6)
            elif event.x>200 and event.x<400 and event.y<600 and event.y > 400 and 7 not in self.O:
                self.X.append(7)
            elif 8 not in self.O:
                self.X.append(8)
            self.tourmulti += 1

        elif self.tour%2 == 1 and self.mode==0 or self.tour%2 == 0 and self.tourmulti%2 == 1 and self.mode ==1 or self.tour%2 == 0 and self.tourmulti%2 == 0 and self.mode ==0:
            if event.x<200 and event.y<200 and 0 not in self.X:
                self.O.append(0)
            elif event.x>200 and event.x<400 and event.y<200 and 1 not in self.X:
                self.O.append(1)
            elif event.x>400 and event.x<600 and event.y<200 and 2 not in self.X:
                self.O.append(2)
            elif event.x<200 and event.y>200 and event.y<400 and 3 not in self.X:
                self.O.append(3) 
            elif event.x>200 and event.x<400 and event.y<400 and event.y > 200 and 4 not in self.X: 
                self.O.append(4)
            elif event.x>400 and event.x<600 and event.y<400 and event.y > 200 and 5 not in self.X:
                self.O.append(5)
            elif event.x<200 and event.y>400 and event.y<600 and 6 not in self.X:
                self.O.append(6)
            elif event.x>200 and event.x<400 and event.y<600 and event.y > 400 and 7 not in self.X:
                self.O.append(7)
            elif 8 not in self.X:
                self.O.append(8)
            self.tourmulti += 1
    

        if self.victoire(self.X)==True and self.victoire(self.O)==True and len(self.X)!=5:
            if self.tour%2 ==1:
                self.princ.create_text(self.case[str(self.X[-1])][0], self.case[str(self.X[-1])][1], text="X", fill="white", font=("Raleway",100,"bold"))
                self.cases.remove(int(self.X[-1]))
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

        self.self.bouton_joueur1.destroy()
        self.self.bouton_joueur2.destroy()
        print("\n***********************************\n")
        self.fin=True
        
        if self.typej == 1:
            self.tour = 1
            self.tourmulti = 1 
            self.ss = socket(AF_INET,SOCK_STREAM)
            self.ss.bind(("localhost",50004))
            self.ss.listen(1)
            self.connexion=True
            

            while self.connexion:
                print("\n***********************************\n")
                print("\nEn attente d'un joueur...\n")
                self.client, adresse= self.ss.accept()
                print("\n***********************************\n")
                print("self.client {} connecté".format(adresse))
                print("\n***********************************\n")

                while self.fin:
                    if len(self.X) == 0:
                        self.client.send("test".encode("utf8"))
                    else:
                        self.client.send(str(self.X[-1]).encode("utf8"))

                    self.reponse = self.client.recv(1024).decode("utf8")
                    
                        
                    if self.reponse != "test" and self.reponse !="testtest":
                        if len(self.O) == 0:
                            self.O.append(int(self.reponse))
                            self.princ.create_text(self.case[str(self.O[-1])][0], self.case[str(self.O[-1])][1], text="O", fill="white", font=("Raleway",100,"bold"))
                            self.tourmulti += 1
                            
                        if int(self.reponse) != self.O[-1]:
                            self.O.append(int(self.reponse))
                            self.princ.create_text(self.case[str(self.O[-1])][0], self.case[str(self.O[-1])][1], text="O", fill="white", font=("Raleway",100,"bold"))
                            self.tourmulti += 1
                            

                    if self.victoire(self.X)!=True or self.victoire(self.O)!=True or len(self.X)==5:
                        self.affvict(self.X, self.O, self.princ)   
                    
                    if self.tourmulti%2 == 1:
                        self.princ.configure(bg='blue')
                        self.fenetre.update()
                    else :
                        self.princ.configure(bg='red')
                        self.fenetre.update()
                

        if self.typej == 0:
            self.tour = 0
            self.tourmulti = 0
            self.sc = socket(AF_INET,SOCK_STREAM)     
            self.sc.connect(("localhost",50004))

            while self.fin:
                    if len(self.O) == 0:
                        self.sc.send("test".encode("utf8"))
                    else:
                        self.sc.send(str(self.O[-1]).encode("utf8"))
                        
                    self.reponse=self.sc.recv(1024).decode("utf8")
                    if self.reponse != "test" and self.reponse !="testtest":
                        if len(self.X) == 0:
                            self.X.append(int(self.reponse))
                            self.princ.create_text(self.case[str(self.X[-1])][0], self.case[str(self.X[-1])][1], text="X", fill="white", font=("Raleway",100,"bold"))
                            self.tourmulti += 1

                        if int(self.reponse) != self.X[-1]:
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
            

        print("\n***********************************\n")
        if self.mode == 1:
            self.thread = threading.Thread(target=self.multi, args=(self.princ, self.case))
            self.thread.start()
        self.fenetre.bind("<Button-1>",self.jeumulti)  

    def selection_joueurs(self):

        self.bouton_commencement_jeu.destroy()
        self.bouton_deux_ordinateurs.destroy()
        self.bouton_joueur1 = Button(self.fenetre,width=50, height= 50, command = lambda:[self.joueur_un(),self.commencement_jeu()], bg='blue',text= 'self.client')
        self.bouton_joueur2 = Button(self.fenetre,width=50, height= 50, command = lambda:[self.joueur_deux(),self.commencement_jeu()], bg='red',text = 'HOST')
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



if __name__ == "__main__":
    test = Morpion()