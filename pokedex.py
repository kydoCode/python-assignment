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
fenetre.title("ポケモンずかん - [Pokédex]")
fenetre.geometry("336x432")

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


# pokeList = ["Bulbizarre", "Salamèche", "Carapuce", "Chenipan", "Pikachu", "Roucool", "Rattata"]
# pokeListEng = ["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","Nidoran","Nidorina","Nidoqueen","Nidoran","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetch'd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr. Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew"]
pokeListArr = {0: {'name': 'Bulbizarre', 'type': f'{Types.PLANTE.value}', 'abilities': 'Engrais'}, 1: {'name': 'Salamèche', 'type': f'{Types.FEU.value}', 'abilities': 'Brasier'}, 2: {'name': 'Carapuce', 'type': f'{Types.EAU.value}', 'abilities': 'Torrent'}}


for poke in pokeListArr:
        listbox.insert(tk.END, f"{pokeListArr[poke]['name']}")#, command=open_desc)

# def retrieve_index():
#     li_index = listbox.curselection()
#     print(li_index)
#     return li_index

# listbox.bind('<<ListboxSelect>>', retrieve_index)



# Button add pokemon : champs de saisie trois valeurs: nom champ libre, type enum menu déroulant, capacité s champ libre
    
def open_desc():
    current_indexes = listbox.curselection()
    if current_indexes:
         current_index = current_indexes[0]
         current_item = listbox.get(current_index)
         print("Item sélectionné: ", current_item)
         
         # etiquetteFour = tk.Label(fenetre, text=f"Détail de {pokeListArr[current_item]['name']}\n", f"{pokeListArr[current_item]['name']}\n{pokeListArr[current_item]['type']}\n{pokeListArr[current_item]['abilities']}")
         # messagebox.showinfo(BulbizarreetiquetteFour.pack())
    # i = 0
    # while i <= 1: 
    # poke = current_item
    
    # checkList = []
    checkItem = current_item
    print("checkItem vaut: (AVB)", checkItem)
    print("current item vayt: (AVB)", current_item)
    for current_item in pokeListArr:
        print("currentitem vaut dans la boucle:", current_item)
        #for i in range(i=0, i=1, 1):
        #    i += 1
        # checkArray = 
        # if pokeListArr[current_item]['name']
        # i =[]
        # for i in pokeListArr:
        #     if i == pokeListArr[current_item]['name']: 
              # if len(pokeListArr)-1 == True:
        if current_item < 1: #current_item+1:
        #if current_item == checkItem:
            print(current_item, checkItem)
            messagebox.showinfo(f"Détail de {pokeListArr[current_item]['name']}\n", f"{pokeListArr[current_item]['name']}\n{pokeListArr[current_item]['type']}\n{pokeListArr[current_item]['abilities']}")
            print(current_item, checkItem)
        else:
            break
    #pass
    
        
        
    # return current_item
   
    

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

    pokeListArr[j] = {'name': f'{}', 'type': Types, 'abilities': f'{}'}

fenetre.mainloop()