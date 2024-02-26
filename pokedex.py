import tkinter as tk
from enum import Enum
from pickle import *

class Types(Enum):
    ACIER = "Acier"
    COMBAT = "Combat"
    DRAGON = "Dragon"
    EAU = "Eau"
    ELECTRIK = "Electrik"
    FEU = "Feu"
    FEE = "Fée"
    GLACE = "Glace"
    INSECTE = "Insecte"
    NORMAL = "Normal"
    PLANTE = "Plante"
    POISON = "Poison"
    PSY = "Psy"
    ROCHE = "Roche"
    SOL = "Sol"
    SPECTRE = "Spectre"
    TENEBRES = "Ténèbres"
    VOL = "Vol"

class Pokemon:
    def __init__(self, name, type, abilities): #desc,
        self.name = name
        #self.desc = desc
        self.type = type
        self.abilities = abilities

fenetre = tk.Tk()
fenetre.title("Pokeded by Kody")


fenetre.mainloop()