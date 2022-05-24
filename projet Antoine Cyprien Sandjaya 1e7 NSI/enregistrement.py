from tkinter import*

#définition de la fenêtre d'enregistrement
class Enregistrement():
    
    def __init__(self):

        #création de la fenêtre principale
        self.mainWindow = Tk()
        self.mainWindow.geometry('500x500')
        self.mainWindow.title('veuillez vous enregistrer')

        #création du canvas principal
        self.mainCanvas = Canvas(self.mainWindow, width=500, height=500, bg="#0493ea")
        self.mainCanvas.place(x=0, y=0)

        #création du canvas servant à récupérer le nom de l'utilisateur
        self.nameCanvas = Canvas(self.mainCanvas, width=250, height=100)
        self.nameCanvas.place(x=10, y=0)

        #création de l'entry servant à récupérer le nom de l'utilisateur
        self.name = StringVar()
        self.nameEntry = Entry(self.nameCanvas, textvariable = self.name)
        self.nameEntry.place(x=20, y=10)

        #création du button servant à récupérer le nom de l'utilisateur
        self.nameButton = Button(self.nameCanvas, text="ok", command=self.getName, bg='red')
        self.nameButton.place(x=20, y=30)

        self.mainWindow.mainloop()

    #création de la fonction qui récupère le nom de l'utilisateur
    def getName(self):

        #on crée un fichier texte pour stoker le pseudo e l'utilisateur
        self.namemyFile = 'namefile.txt'
        self.myfile = open(self.namemyFile, "r+")

        #on récupère le nom de l'utilisateur
        self.userName = self.name.get()
        print(self.userName)

        #on écrit le nom de l'utilisateur dans le fichier texte
        self.myfile.write(self.userName)

        self.myfile.close()

        self.mainWindow.destroy()





if __name__ == '__main__':
    w = Enregistrement()


