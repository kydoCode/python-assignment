import tkinter as tk
from tkinter import messagebox
from enum import Enum
# from pickle import *
# import pickle
import json

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
    def __init__(self, name, abilities): #desc,
        self.name = name
        #self.desc = desc
        self.type = Types
        self.abilities = abilities

# MAIN VIEW
fenetre = tk.Tk()
fenetre.title("ポケモンずかん - [Pokédex]")
fenetre.geometry("336x432")
sd
# Affichage du logo Pokémon

logo = tk.PhotoImage(file="Int_Poke_logo.png")
etiquetteThree = tk.Label(fenetre, image=logo)
etiquetteThree.place(x=0, y=168)

# Affichage du texte pour la listebox
etiquette = tk.Label(fenetre, text="Sélectionnez un Pokémon:")
etiquette.pack()

# Liste de Pokémons: list
listbox = tk.Listbox(fenetre)
listbox.pack()

pokeListArr = [
    {'name': 'Bulbizarre', 'type': Types.PLANTE, 'abilities': 'Engrais'},
    {'name': 'Salamèche', 'type': Types.FEU, 'abilities': 'Brasier'},
    {'name': 'Carapuce', 'type': Types.EAU, 'abilities': 'Torrent'}
]
# pokeListArr = {0: {'name': 'Bulbizarre', 'type': f'{Types.PLANTE.value}', 'abilities': 'Engrais'}, 1: {'name': 'Salamèche', 'type': f'{Types.FEU.value}', 'abilities': 'Brasier'}, 2: {'name': 'Carapuce', 'type': f'{Types.EAU.value}', 'abilities': 'Torrent'}}

# Ecriture
with open("pokeListArr.pkl", "wb") as f:
    pickle.dump(pokeListArr, f)
f.close()

# lecture
with open("pokeListArr.pkl", "rb") as f:
    pokeListArr = pickle.load(f)
f.close()

for poke in pokeListArr:
        listbox.insert(tk.END, f"{pokeListArr[poke]['name']}")#, command=open_desc)


# Button add pokemon : champs de saisie trois valeurs: nom champ libre, type enum menu déroulant, capacité s champ libre
    
def open_desc():
    current_indexes = listbox.curselection()
    if current_indexes:
         current_index = current_indexes[0]
         current_item = listbox.get(current_index)
         print("Item sélectionné: ", current_item)
         
         # etiquetteFour = tk.Label(fenetre, text=f"Détail de {pokeListArr[current_item]['name']}\n", f"{pokeListArr[current_item]['name']}\n{pokeListArr[current_item]['type']}\n{pokeListArr[current_item]['abilities']}")
         # messagebox.showinfo(etiquetteFour.pack())
 
    # poke = current_item
    
    # checkList = []
    checkItem = current_item
    print("checkItem vaut: (AVB)", checkItem)
    print("current_item vayt: (AVB)", current_item)

    # poke, value in pokeListArr.items() -> check
    for key, checkItem in pokeListArr.items():
        print("current_item vaut dans la boucle:", checkItem)
        
        for pokey[0] in current_item:
            if checkItem == current_item:
                print(current_item, checkItem)
                messagebox.showinfo(f"Détail de {pokeListArr[current_item]['name']}\n", f"{pokeListArr[current_item]['name']}\n{pokeListArr[current_item]['type']}\n{pokeListArr[current_item]['abilities']}")
                print(current_item, checkItem)
            else:
                break
       
bouton = tk.Button(fenetre, text="Détails", command=open_desc)
bouton.pack()

# Instance de classe Pokemon()
# Savuegarder au tableau puis dans le fichier (les deux en même temps)

boutonTwo = tk.Button(fenetre, text="Nouveau Pokémon")#, command)
boutonTwo.pack()

etiquetteTwo = tk.Label(fenetre, text="[Pokédex]- v1 by Kody san")
etiquetteTwo.pack()

# DETAIL VIEW

# ADD POKEMON VIEW

def add_pokemon():
    i = len(pokeListArr) + 1
    print("Valeur de i:", i)
    pokeListArr[i] = {}
    pokeListArr[i]['name'] = "" #/.get()
    pokeListArr[i]['type'] = Types
    pokeListArr[i]['abilities'] = ""

   # pokeListArr[j] = {'name': f'{}', 'type': Types, 'abilities': f'{}'}

fenetre.mainloop()