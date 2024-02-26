import tkinter as tk
from tkinter import messagebox
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
    def __init__(self, name, abilities): #desc,
        self.name = name
        #self.desc = desc
        self.type = Types
        self.abilities = abilities

# MAIN VIEW
fenetre = tk.Tk()
fenetre.title("ポケモンずかん - [Pokédex]") # Pokeded 
fenetre.geometry("336x432")

# Affichage du logo Pokémon

logo = tk.PhotoImage(file="Int_Poke_logo.png")
etiquetteThree = tk.Label(fenetre, image=logo)
etiquetteThree.place(x=0, y=168)

# Affichage du texte pour la listebox
etiquette = tk.Label(fenetre, text="Sélectionnez un Pokémon:")
etiquette.pack()

# Liste de Pokemons: list
listbox = tk.Listbox(fenetre)
listbox.pack()


# Ajout d'éléments à la liste
# listbox.insert(tk.END, "Pokémon 1") # Remplacer par la variable du fichier
# listbox.insert(tk.END, "Pokémon 2")
# listbox.insert(tk.END, "Pokémon 3")

pokeList = ["Bulbizarre", "Salamèche", "Carapuce", "Chenipan", "Pikachu", "Roucool", "Rattata"]
pokeListEng = ["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","Nidoran","Nidorina","Nidoqueen","Nidoran","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetch'd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr. Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew"]
pokeListArr = {0: {'name': 'Bulbizarre', 'type': f'{Types.PLANTE.value}', 'abilities': 'Engrais'}, 1: {'name': 'Salamèche', 'type': f'{Types.FEU.value}', 'abilities': 'Brasier'}, 2: {'name': 'Carapuce', 'type': f'{Types.EAU.value}', 'abilities': 'Torrent'}}

#{
#        self.name: 'Salamèche', 
#        self.type: f'{Types.FEU.value}', 
#        self.abilities: 'Brasier'}


def open_desc():
    messagebox.showinfo
    pass

# stopValue = len(pokeListArr)

# for i in range(i = 0, i <= stopValue, i+=1):
for poke in pokeListArr:
        # for key,value
        listbox.insert(tk.END, f"{pokeListArr[poke]['name']}")#, command=open_desc)


# sdvaluepokeListArr[]['name']
# Button add pokemon : champs de saisie trois valeurs: nom champ libre, type enum menu déroulant, capacité s champ libre
    
bouton = tk.Button()
# Instancec de classe Pokemon()
# Savuegarder au tableau puis dans le fichier (les deux en même temps)



etiquetteTwo = tk.Label(fenetre, text="[Pokédex]- v1 by Kody san")
etiquetteTwo.pack()

# DETAIL VIEW

# ADD POKEMON VIEW


fenetre.mainloop()