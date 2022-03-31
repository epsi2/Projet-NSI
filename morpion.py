from tkinter import *
from collections import Counter
import random
import time

global case, Cases, win

X=[]
O=[]
case= {"0":(100,100,0,0),"1":(300,100,1,0),"2":(500,100,2,0),"3":(100,300,0,1),"4":(300,300,1,1),"5":(500,300,2,1),"6":(100,500,0,2),"7":(300,500,1,2),"8":(500,500,2,2)}
Cases=[0,1,2,3,4,5,6,7,8]   


fenetre=Tk()
princ = Canvas(fenetre, width=600, height= 600, background = "black")
ligne1 = princ.create_line(200,0,200,600,fill="white")
ligne2 = princ.create_line(400,0,400,600,fill="white")
ligne3 = princ.create_line(0,200,600,200,fill="white")
ligne4 = princ.create_line(0,400,600,400,fill="white")

princ.pack()

                
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
        
        
def jeu(evt):
    global X,O
         
    if evt.x<200 and evt.y<200:
        X.append(0)
    elif evt.x>200 and evt.x<400 and evt.y<200:
        X.append(1)
    elif evt.x>400 and evt.x<600 and evt.y<200:
        X.append(2)
    elif evt.x<200 and evt.y>200 and evt.y<400:
        X.append(3) 
    elif evt.x>200 and evt.x<400 and evt.y<400 and evt.y > 200:
        X.append(4)
    elif evt.x>400 and evt.x<600 and evt.y<400 and evt.y > 200:
        X.append(5)
    elif evt.x<200 and evt.y>400 and evt.y<600:
        X.append(6)
    elif evt.x>200 and evt.x<400 and evt.y<600 and evt.y > 400:
        X.append(7)
    else:
        X.append(8)
      
    while victoire(X)==True and victoire(O)==True and len(X)!=5:
        princ.create_text(case[str(X[-1])][0], case[str(X[-1])][1], text="X", fill="white", font=("Raleway",100,"bold"))
        Cases.remove(X[-1])
        victoire(X)       
        print(X)
        print(Cases)
        fenetre.update()
        time.sleep(0.5)
        O.append(random.choice(Cases))
        princ.create_text(case[str(O[-1])][0], case[str(O[-1])][1], text="O", fill="white", font=("Raleway",100,"bold"))
        victoire(O)
        Cases.remove(O[-1])
        print(O)
        print(Cases)
          

    time.sleep(0.85)    

    if len(X)==5 and victoire(X):    
        princ.create_text(300, 285, text="Match nul", fill="#1c784b", font=("Raleway",20,"bold"))    
    elif victoire(X)==False:
        princ.create_text(300, 285, text="Le joueur X a gagné", fill="#1c784b", font=("Raleway",20,"bold"))  
    elif victoire(O)==False:
        princ.create_text(300, 285, text="Le joueur O a gagné", fill="#1c784b", font=("Raleway",20,"bold"))  
    else:
        princ.create_text(300, 285, text="Erreur", fill="white", font=("Raleway",20,"bold"))  
                
  

    
       
fenetre.bind("<Button-1>",jeu)   
        
fenetre.mainloop()

   
 