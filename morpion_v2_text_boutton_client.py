from tkinter import Canvas,Tk,Button
from collections import Counter
from socket import socket, AF_INET, SOCK_STREAM
import time
import threading

global case, Cases, win
X=[]
O=[]
case= {"0":(100,100,0,0),"1":(300,100,1,0),"2":(500,100,2,0),"3":(100,300,0,1),"4":(300,300,1,1),"5":(500,300,2,1),"6":(100,500,0,2),"7":(300,500,1,2),"8":(500,500,2,2)}
Cases=[0,1,2,3,4,5,6,7,8]   
tour=1
tourmulti=1


fenetre=Tk()
def commencement_jeu():
    global ligne1,ligne2,ligne3,ligne4
    princ = Canvas(fenetre, width=600, height= 600, background = "red")
    ligne1 = princ.create_line(200,0,200,600,fill="white")
    ligne2 = princ.create_line(400,0,400,600,fill="white")
    ligne3 = princ.create_line(0,200,600,200,fill="white")
    ligne4 = princ.create_line(0,400,600,400,fill="white")

    princ.grid(column = 0,row=0)

                    
    def victoire(joueur):
        global win
        l=sorted(joueur)     
    
        if len(l)>=3:
            c1=[]
            for num in l:
                c1.append(case[str(num)][3])
                
                
            c2=[]
            for num in l:
                c2.append(case[str(num)][2])
                
            
            if Counter(c1).most_common(1)[0][1]==3:
                return False
            elif Counter(c2).most_common(1)[0][1]==3:
                return False 
            elif 6 in l and 4 in l and 2 in l:
                return False
            elif 8 in l and 4 in l and 0 in l:
                return False
            else:
                return True
            
        else :
            return True


    def affvict(X, O, princ):
        if len(X)==5 and victoire(X) == True:    
                princ.create_text(300, 285, text="Match nul", fill="#1c784b", font=("Raleway",20,"bold"))    
        elif victoire(X)==False:
                princ.create_text(300, 285, text="Le joueur X a gagné", fill="#1c784b", font=("Raleway",20,"bold"))  
        elif victoire(O)==False:
                princ.create_text(300, 285, text="Le joueur O a gagné", fill="#1c784b", font=("Raleway",20,"bold"))  
        else:
                princ.create_text(300, 285, text="Erreur", fill="white", font=("Raleway",20,"bold")) 
        ss.close() 
            
    def jeumulti(evt):
        global X,O,tour, tourmulti
        if tour%2 == 1 and tourmulti%2 == 1 or tour%2 == 1 and mode==0 :    
            if evt.x<200 and evt.y<200 and 0 not in O:
                X.append(0)
            elif evt.x>200 and evt.x<400 and evt.y<200 and 1 not in O:
                X.append(1)
            elif evt.x>400 and evt.x<600 and evt.y<200 and 2 not in O:
                X.append(2)
            elif evt.x<200 and evt.y>200 and evt.y<400 and 3 not in O:
                X.append(3) 
            elif evt.x>200 and evt.x<400 and evt.y<400 and evt.y > 200 and 4 not in O:
                X.append(4)
            elif evt.x>400 and evt.x<600 and evt.y<400 and evt.y > 200 and 5 not in O:
                X.append(5)
            elif evt.x<200 and evt.y>400 and evt.y<600 and 6 not in O:
                X.append(6)
            elif evt.x>200 and evt.x<400 and evt.y<600 and evt.y > 400 and 7 not in O:
                X.append(7)
            elif 8 not in O:
                X.append(8)
            tourmulti += 1

        elif tour%2 == 1 and mode==0 or tour%2 == 0 and tourmulti%2 == 1 and mode ==1 or tour%2 == 0 and tourmulti%2 == 0 and mode ==0:
            if evt.x<200 and evt.y<200 and 0 not in X:
                O.append(0)
            elif evt.x>200 and evt.x<400 and evt.y<200 and 1 not in X:
                O.append(1)
            elif evt.x>400 and evt.x<600 and evt.y<200 and 2 not in X:
                O.append(2)
            elif evt.x<200 and evt.y>200 and evt.y<400 and 3 not in X:
                O.append(3) 
            elif evt.x>200 and evt.x<400 and evt.y<400 and evt.y > 200 and 4 not in X: 
                O.append(4)
            elif evt.x>400 and evt.x<600 and evt.y<400 and evt.y > 200 and 5 not in X:
                O.append(5)
            elif evt.x<200 and evt.y>400 and evt.y<600 and 6 not in X:
                O.append(6)
            elif evt.x>200 and evt.x<400 and evt.y<600 and evt.y > 400 and 7 not in X:
                O.append(7)
            elif 8 not in X:
                O.append(8)
            tourmulti += 1
    

        if victoire(X)==True and victoire(O)==True and len(X)!=5:
            if tour%2 ==1:
                princ.create_text(case[str(X[-1])][0], case[str(X[-1])][1], text="X", fill="white", font=("Raleway",100,"bold"))
                Cases.remove(int(X[-1]))
                victoire(X)
                fenetre.update()
                if mode == 0:
                    tour += 1
                    princ.configure(bg='blue')
                print(X)
            else: 
                time.sleep(0.1)
                princ.create_text(case[str(O[-1])][0], case[str(O[-1])][1], text="O", fill="white", font=("Raleway",100,"bold"))
                victoire(O)
                Cases.remove(int(O[-1]))
                fenetre.update()
                if mode == 0:
                    tour += 1
                    princ.configure(bg='red')
                print(O)

        else:
            affvict(X, O, princ)









    def multi(princ, case):
        bouton_joueur_1.destroy()
        bouton_joueur_2.destroy()
        print("\n***********************************\n")
        global tour, tourmulti, ss
        fin=True
        
        if typej == 1:
            tour = 1
            tourmulti = 1 
            ss = socket(AF_INET,SOCK_STREAM)
            ss.bind(("localhost",50004))
            ss.listen(1)
            connexion=True
            

            while connexion:
                print("\n***********************************\n")
                print("\nEn attente d'un joueur...\n")
                client, adresse= ss.accept()
                print("\n***********************************\n")
                print("Client {} connecté".format(adresse))
                print("\n***********************************\n")

                while fin:
                    if len(X) == 0:
                        client.send("test".encode("utf8"))
                    else:
                        client.send(str(X[-1]).encode("utf8"))

                    reponse = client.recv(1024).decode("utf8")
                    
                        
                    if reponse != "test" and reponse !="testtest":
                        if len(O) == 0:
                            O.append(int(reponse))
                            princ.create_text(case[str(O[-1])][0], case[str(O[-1])][1], text="O", fill="white", font=("Raleway",100,"bold"))
                            tourmulti += 1
                            
                        if int(reponse) != O[-1]:
                            O.append(int(reponse))
                            princ.create_text(case[str(O[-1])][0], case[str(O[-1])][1], text="O", fill="white", font=("Raleway",100,"bold"))
                            tourmulti += 1
                            

                    if victoire(X)!=True or victoire(O)!=True or len(X)==5:
                        affvict(X, O, princ)   
                    
                    if tourmulti%2 == 1:
                        princ.configure(bg='blue')
                        fenetre.update()
                    else :
                        princ.configure(bg='red')
                        fenetre.update()
                

        if typej == 0:
            tour = 0
            tourmulti = 0
            sc = socket(AF_INET,SOCK_STREAM)     
            sc.connect(("localhost",50004))

            while fin:
                    if len(O) == 0:
                        sc.send("test".encode("utf8"))
                    else:
                        sc.send(str(O[-1]).encode("utf8"))
                        
                    reponse=sc.recv(1024).decode("utf8")

                    if reponse != "test" and reponse !="testtest":
                        if len(X) == 0:
                            X.append(int(reponse))
                            princ.create_text(case[str(X[-1])][0], case[str(X[-1])][1], text="X", fill="white", font=("Raleway",100,"bold"))
                            tourmulti += 1

                        if int(reponse) != X[-1]:
                            X.append(int(reponse))
                            princ.create_text(case[str(X[-1])][0], case[str(X[-1])][1], text="X", fill="white", font=("Raleway",100,"bold"))
                            tourmulti += 1
                        
                    if victoire(X)!=True or victoire(O)!=True or len(X)==5:
                        affvict(X, O, princ)
                    
                    if tourmulti%2 == 1:
                        princ.configure(bg='red')
                        fenetre.update()
                    else :
                        princ.configure(bg='blue')
                        fenetre.update()
            

    print("\n***********************************\n")
    if mode == 1:
        thread = threading.Thread(target=multi, args=(princ, case))
        thread.start()
    fenetre.bind("<Button-1>",jeumulti)  

def selection_joueurs():
    global bouton_joueur_1,bouton_joueur_2
    bouton_meme_ordinateur.destroy()
    bouton_deux_ordinateur.destroy()
    bouton_joueur_1 = Button(fenetre,width=50, height= 50, command = lambda:[joueur_un(),commencement_jeu()], bg='blue',text= 'client')
    bouton_joueur_2 = Button(fenetre,width=50, height= 50, command = lambda:[joueur_deux(),commencement_jeu()], bg='red',text = 'HOST')
    bouton_joueur_1.grid(column = 0, row = 0)
    bouton_joueur_2.grid(column = 1, row = 0)

def meme_ordinateur():
    global mode
    mode = 0
    

def deux_ordinateur():
    global mode
    mode = 1
def joueur_un():
    global typej
    typej = 0
def joueur_deux():
    global typej
    typej = 1
def destruction():
    bouton_meme_ordinateur.destroy()
    bouton_deux_ordinateur.destroy()

bouton_meme_ordinateur = Button(fenetre,width=50, height= 50, command = lambda:[destruction(),meme_ordinateur(),commencement_jeu()], bg='blue',text= 'même ordinateur')
bouton_deux_ordinateur = Button(fenetre,width=50, height= 50, command = lambda:[deux_ordinateur(),selection_joueurs()], bg='red',text = 'local')
bouton_meme_ordinateur.grid(column = 0, row = 0)
bouton_deux_ordinateur.grid(column = 1, row = 0)


fenetre.mainloop()


