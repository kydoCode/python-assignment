import tkinter as tk
from tkinter import messagebox, simpledialog
from enum import Enum
import json
from tkinter import ttk

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

# Liste des types de Pokémon
TYPES_POKEMON = [type_.value for type_ in Types]

class Pokemon:
    def __init__(self, name, p_type, abilities):
        self.name = name
        self.type = p_type
        self.abilities = abilities

# Charge les données des Pokémon depuis un fichier JSON
def load_pokemons():
    try:
        with open("pokemons.json", "r") as f:
            pokemons_data = json.load(f)
        pokemons = [Pokemon(data['name'], Types[data['type']], data['abilities']) for data in pokemons_data]
    except (FileNotFoundError, json.JSONDecodeError):
        pokemons = []
    return pokemons

# Enregistre les données des Pokémon dans un fichier JSON
def save_pokemons(pokemons):
    pokemons_data = [{'name': pokemon.name, 'type': pokemon.type.value, 'abilities': pokemon.abilities} for pokemon in pokemons]
    with open("pokemons.json", "w") as f:
        json.dump(pokemons_data, f, indent=4)

# Crée une nouvelle instance de la classe Tk pour la fenêtre principale de l'application
fenetre = tk.Tk()
fenetre.title("ポケモンずかん - [Pokédex]")
fenetre.geometry("336x432")

# Charge les données des Pokémon depuis le fichier JSON
pokeListArr = load_pokemons()

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

# Remplir la listbox avec les noms des Pokémon
for pokemon in pokeListArr:
    listbox.insert(tk.END, pokemon.name)

# Affiche les détails du Pokémon sélectionné
def open_desc():
    current_indexes = listbox.curselection()
    if current_indexes:
        current_index = current_indexes[0]
        current_pokemon = pokeListArr[current_index]
        
        # Vérifie si le type du Pokémon est bien un objet Enum
        if isinstance(current_pokemon.type, Types):
            pokemon_type = current_pokemon.type.value
        else:
            pokemon_type = current_pokemon.type
        
        # Affiche les détails du Pokémon dans une boîte de message
        messagebox.showinfo("Détails Pokémon", f"Nom: {current_pokemon.name}\nType: {pokemon_type}\nCapacités: {current_pokemon.abilities}")


# Bouton pour afficher les détails du Pokémon sélectionné
bouton = tk.Button(fenetre, text="Détails", command=open_desc)
bouton.pack()

# Définition de la fonction pour afficher une boîte de dialogue personnalisée
def ask_type():
    # Création d'une nouvelle fenêtre
    type_window = tk.Toplevel(fenetre)
    type_window.title("Sélectionnez le type du nouveau Pokémon")

    # Étiquette pour guider l'utilisateur
    label = tk.Label(type_window, text="Sélectionnez le type du nouveau Pokémon:")
    label.pack()

    # Liste déroulante pour les types de Pokémon
    selected_type = tk.StringVar(type_window)
    selected_type.set(TYPES_POKEMON[0])  # Sélectionne le premier type par défaut
    dropdown = ttk.Combobox(type_window, textvariable=selected_type, values=TYPES_POKEMON)
    dropdown.pack()

    # Bouton pour valider la sélection
    button = tk.Button(type_window, text="Valider", command=lambda: type_window.destroy())
    button.pack()

    # Attend que la fenêtre soit fermée avant de renvoyer la sélection
    type_window.wait_window()

    # Renvoie le type sélectionné
    return selected_type.get()

# Fonction pour ajouter un nouveau Pokémon
def add_new_pokemon():
    # Demande à l'utilisateur d'entrer le nom du nouveau Pokémon
    name = simpledialog.askstring("Nouveau Pokémon", "Entrez le nom du nouveau Pokémon:")
    
    if name:
        # Demande à l'utilisateur de sélectionner le type du nouveau Pokémon
        p_type = ask_type()
        
        if p_type:
            # Demande à l'utilisateur d'entrer les capacités du nouveau Pokémon
            abilities = simpledialog.askstring("Nouveau Pokémon", "Entrez les capacités du nouveau Pokémon:")
            
            if abilities:  
                # Crée un nouvel objet Pokemon avec les informations saisies par l'utilisateur
                new_pokemon = Pokemon(name, p_type, abilities)
                
                # Ajoute le nouveau Pokémon à la liste pokeListArr
                pokeListArr.append(new_pokemon)
                
                # Rafraîchit la listbox pour afficher le nouveau Pokémon ajouté
                listbox.insert(tk.END, new_pokemon.name)
                
                # Affiche un message de confirmation
                messagebox.showinfo("Succès", "Le nouveau Pokémon a été ajouté avec succès !")
            else:
                # Affiche un message d'erreur si les capacités n'ont pas été saisies
                messagebox.showerror("Erreur", "Veuillez saisir les capacités pour ajouter un nouveau Pokémon.")
        else:
            # Affiche un message d'erreur si le type de Pokémon n'a pas été sélectionné
            messagebox.showerror("Erreur", "Veuillez sélectionner un type de Pokémon.")
    else:
        # Affiche un message d'erreur si le nom du Pokémon n'a pas été saisi
        messagebox.showerror("Erreur", "Veuillez saisir un nom pour ajouter un nouveau Pokémon.")

# Mettez à jour le bouton pour ajouter un nouveau Pokémon pour appeler la fonction add_new_pokemon()
boutonTwo = tk.Button(fenetre, text="Nouveau Pokémon", command=add_new_pokemon)
boutonTwo.pack()

# boutonTwo = tk.Button(fenetre, text="Nouveau Pokémon", command=save_pokemons)
#boutonTwo = tk.Button(fenetre, text="Nouveau Pokémon", command=add_new_pokemon)


# Label pour afficher la version de l'application
etiquetteTwo = tk.Label(fenetre, text="[Pokédex]- v1 by Kody san")
etiquetteTwo.pack()

# Lancer la boucle principale de l'interface utilisateur
fenetre.mainloop()
