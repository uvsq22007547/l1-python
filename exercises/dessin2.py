import tkinter as tk
import random as rd

objets = []

def cercle():
    global objets
    x = rd.randint(0, 400)
    y = rd.randint(0, 400)
    id = canvas.create_oval((x, y), (x+100, y+100), fill=color)
    objets.append(id)

def carre():
    global objets
    x = rd.randint(0, 400)
    y = rd.randint(0, 400)
    id = canvas.create_rectangle((x, y), (x+100, y+100), fill=color)
    objets.append(id)

def croix():
    global objets
    x = rd.randint(0, 400)
    y = rd.randint(0, 400)
    id1 = canvas.create_line((x, y), (x+100, y+100), fill=color)
    id2 = canvas.create_line((x+100, y), (x, y+100), fill=color)
    objets += [id1, id2]

def choisir_couleur():
    global color
    color = input("Choisis une couleur: ")


def undo():
    # si la liste n'est pas vide
    if objets != []:
        id = objets[-1] 
        if canvas.type(id) == "line":
            est_croix = True
        else:
            est_croix = False
        canvas.delete(id)
        del(objets[-1])
        if est_croix:
            id = objets[-1] 
            canvas.delete(id)
            del(objets[-1])


color = "blue"
racine = tk.Tk()
racine.title("Mon dessin")
# création des widgets
bouton_cercle = tk.Button(racine, text="Cercle", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=cercle)
bouton_carre = tk.Button(racine, text="Carré", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=carre)
bouton_croix = tk.Button(racine, text="Croix", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=croix)
bouton_couleur = tk.Button(racine, text="Choisir une couleur", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=choisir_couleur)
bouton_undo = tk.Button(racine, text="Undo", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=undo)
canvas = tk.Canvas(racine, width=500, height=500, bg="black", bd=10, relief="raised")
# placement des widgets
bouton_cercle.grid(column=0, row=1)
bouton_carre.grid(column=0, row=2)
bouton_croix.grid(column=0, row=3)
bouton_couleur.grid(column=1, row=0)
bouton_undo.grid(column=2, row=0)
canvas.grid(column=1, row=1, rowspan=3, columnspan=2)
racine.mainloop()