from tkinter import *
from tkinter import messagebox

import csv

def Ajouter():
    f = open('carnet.csv', 'a')
    w = csv.writer(f, delimiter=';',lineterminator='\n')
    w.writerow([eNom.get(), eMail.get(), eNum.get()])
    root.quit()

def ajouterWindow():
    root.withdraw()
    global eNom,eMail,eNum
    ajouter = Toplevel(root)
    ajouter.title("Ajouter")
    ajouter.iconbitmap('add.ico')
    ajouter.config(bg = bg)
    Label(ajouter,text="Saisir Le Nom : ",font='TimeNewRoman 18 bold italic',bg=bg,fg=fg).grid(row=0,column=0)
    Label(ajouter, text="Saisir Le Mail : ",font='TimeNewRoman 18 bold italic',bg=bg,fg=fg).grid(row=1, column=0)
    Label(ajouter, text="Saisir Le Numero : ",font='TimeNewRoman 18 bold italic',bg=bg,fg=fg).grid(row=2, column=0)
    eNom = Entry(ajouter)
    eMail = Entry(ajouter)
    eNum= Entry(ajouter)
    eNom.grid(row=0,column=1)
    eMail.grid(row=1, column=1)
    eNum.grid(row=2, column=1)
    EnterButton=Button(ajouter,text='Enter',padx=99,command=Ajouter,bg=bbg).grid(row=3,column=0,columnspan=2)

def Modifier():
    index=names.index(selected.get())+1
    dataset[index]=[selected.get(),eMail.get(),eNum.get()]
    f = open('carnet.csv', 'w')
    writer = csv.writer(f, delimiter=';', lineterminator='\n')
    writer.writerows(dataset)
    root.quit()

def modifierWindow():
    root.withdraw()
    global selected
    global eNom,eMail,eNum
    modifier = Toplevel(root)
    modifier.config(bg = bg)
    modifier.title("Modifier")
    modifier.iconbitmap('edit.ico')
    selected =StringVar()
    selected.set(names[0])
    drop =OptionMenu(modifier,selected,*names)
    Label(modifier, text="sélectionner Le Nom a modifier ",font='TimeNewRoman 18 bold italic',bg=bg,fg=fg).grid(row=0, column=0 , columnspan=2)
    Label(modifier, text="Saisir Le Nouveau Mail : ",font='TimeNewRoman 18 bold italic',bg=bg,fg=fg).grid(row=1, column=0)
    Label(modifier, text="Saisir Le Nouveau Numero : ",font='TimeNewRoman 18 bold italic',bg=bg,fg=fg).grid(row=2, column=0)
    eMail=Entry(modifier)
    eNum=Entry(modifier)
    eMail.grid(row=1, column=1)
    eNum.grid(row=2, column=1)
    EnterButton=Button(modifier,text='Enter',padx=99,command=Modifier,bg=bbg).grid(row=3,column=0,columnspan=2)
    drop.grid(row=0,column=3)

def Rechercher(currentwindow,button):
    index = names.index(selected.get()) + 1
    Label(currentwindow,text='Nom : ' + dataset[index][0],font='TimeNewRoman 18 bold italic',bg=bg,fg=fg).grid(row=1,column=0)
    Label(currentwindow,text='Mail : ' + dataset[index][1],font='TimeNewRoman 18 bold italic',bg=bg,fg=fg).grid(row=2,column=0)
    Label(currentwindow,text='Numero : ' + dataset[index][2],font='TimeNewRoman 18 bold italic',bg=bg,fg=fg).grid(row=3,column=0)
    button.config(text='Exit', padx=50,bg=bbg, command=root.quit)


def rechercherWindow():
    global selected
    root.withdraw()
    rechercher = Toplevel(root)
    rechercher.config(bg = bg)
    rechercher.title("Rechercher")
    rechercher.iconbitmap('find.ico')
    selected = StringVar()
    selected.set(names[0])
    drop = OptionMenu(rechercher, selected, *names)
    Label(rechercher, text="sélectionner Le Nom a rechercher",font='TimeNewRoman 18 bold italic',bg=bg,fg=fg).grid(row=0, column=0)
    drop.grid(row=0, column=1)
    EnterButton = Button(rechercher, text='Enter', padx=50,bg=bbg, command=lambda :Rechercher(rechercher,EnterButton))
    EnterButton.grid(row=0, column=2)

def Supprimer():
    index = names.index(selected.get()) + 1
    del(dataset[index])
    f = open('carnet.csv', 'w')
    writer = csv.writer(f, delimiter=';', lineterminator='\n')
    writer.writerows(dataset)
    root.quit()
def supprimerWindow():
    global selected
    root.withdraw()
    supprimer = Toplevel(root)
    supprimer.config(bg = bg)
    supprimer.title("Supprimer")
    supprimer.iconbitmap('delete.ico')
    selected = StringVar()
    selected.set(names[0])
    drop = OptionMenu(supprimer, selected, *names)
    Label(supprimer, text="sélectionner Le Nom a supprimer ",font='TimeNewRoman 18 bold italic',bg=bg,fg=fg).grid(row=0, column=0)
    drop.grid(row=0,column=1)
    EnterButton=Button(supprimer,text='Enter',padx=50,bg=bbg,command=Supprimer).grid(row=1,column=0)

def supprimertoutWindow():
    root.withdraw()
    warning = messagebox.askyesno( title='Warning', message='Vous etes sure de supprimer tout ?')
    if warning==1:
        f = open('carnet.csv', 'w')
        w = csv.writer(f, delimiter=';', lineterminator='\n')
        w.writerow(["Nom", "Mail", "Numero"])
        f.close()
    root.quit()
def afficher(root,dataset):
        for rowindex, row in enumerate(dataset):
            for index, i in enumerate(row):
                label = Label(root, text=i,font='TimeNewRoman 18 bold italic',bg=bg,fg=fg)
                label.grid(row=rowindex, column=index)

bg='#ffcdb2'
fg='#b5838d'
bbg='#b5e48c'

root = Tk()
root.iconbitmap('contact.ico')
root.title('Carnet')
root.geometry('+600+300')
root.config(bg = bg)
dataset=([line.strip().split(';') for line in open('carnet.csv')])
names=[dataset[name][0] for name in range(1,len(dataset))]
afficher(root,dataset)
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='Edit', menu=filemenu)
filemenu.add_command(label='Ajouter',command=ajouterWindow)
filemenu.add_command(label='Modifier',command=modifierWindow)
filemenu.add_command(label='Recherche',command=rechercherWindow)
filemenu.add_command(label='Supprimer',command = supprimerWindow)
filemenu.add_command(label='Supprimer Tout',command=supprimertoutWindow)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
mainloop()