import tkinter as tk
from tkinter import messagebox, simpledialog
from enum import Enum
import json
from tkinter import ttk
import os

# Define an Enum class for the different types of Pokemons
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

# List of Pokemon types
TYPES_POKEMON = [type_.name for type_ in Types]

# Pokemon class definition
class Pokemon:
    def __init__(self, name, p_type, abilities):
        self.name = name
        self.type = p_type
        self.abilities = abilities

# Function to load Pokemons from a JSON file

# Function to load Pokemons from a JSON file
def load_pokemons():
    try:
        with open("pokemons.json", "r") as f:
            pokemons_data = json.load(f)

        def string_to_types(t):
            return Types[t.upper()]

        pokemons = []
        for data in pokemons_data:
            try:
                pokemons.append(Pokemon(data['name'], string_to_types(data['type']), data['abilities'].split(', ')))
            except KeyError as e:
                messagebox.showerror("Erreur de type", f"Le type de Pokémon '{e.args[0]}' n'est pas valide.")

    except FileNotFoundError:
        messagebox.showwarning("Fichier manquant", "Le fichier de données des Pokémon n'a pas été trouvé.")
    except json.JSONDecodeError:
        messagebox.showerror("Erreur de format", "Le fichier de données des Pokémon est corrompu.")

    return pokemons

# Function to save Pokemons to a JSON file
def save_pokemons(pokemons):
    try:
        pokemons_data = [{'name': pokemon.name, 'type': pokemon.type.value, 'abilities': ', '.join(pokemon.abilities)} for pokemon in pokemons]
        with open("pokemons.json", "w") as f:
            json.dump(pokemons_data, f, indent=4)
    except Exception as e:
        messagebox.showerror("Erreur d'enregistrement", f"Une erreur s'est produite lors de l'enregistrement des données : {str(e)}")

# Initialize the main window
fenetre = tk.Tk()
fenetre.title("ポケモンずかん - [Pokédex]")
fenetre.geometry("336x432")

# Load Pokemons from the JSON file
pokeListArr = load_pokemons()

# Load the logo image
logo = tk.PhotoImage(file="Int_Poke_logo.png")

# Add the logo image to the main window
etiquetteThree = tk.Label(fenetre, image=logo)
etiquetteThree.place(x=0, y=168)

# Add a label to the main window
etiquette = tk.Label(fenetre, text="Sélectionnez un Pokémon:")
etiquette.pack()

# Add a listbox to the main window
listbox = tk.Listbox(fenetre)
listbox.pack()

# Add each Pokemon name to the listbox
for pokemon in pokeListArr:
    listbox.insert(tk.END, pokemon.name)

# Function to display Pokemon details
def open_desc():
    current_indexes = listbox.curselection()
    if current_indexes:
        current_index = current_indexes[0]
        current_pokemon = pokeListArr[current_index]

        if isinstance(current_pokemon.type, Types):
            pokemon_type = current_pokemon.type.value
        else:
            pokemon_type = current_pokemon.type

        messagebox.showinfo("Détails Pokémon", f"Nom: {current_pokemon.name}\nType: {pokemon_type}\nCapacités: {', '.join(current_pokemon.abilities)}")

# Add a button to the main window to display Pokemon details
bouton = tk.Button(fenetre, text="Détails", command=open_desc)
bouton.pack()

# Function to ask for a new Pokemon type
def ask_type():
    type_window = tk.Toplevel(fenetre)
    type_window.title("Sélectionnez le type du nouveau Pokémon")

    label = tk.Label(type_window, text="Sélectionnez le type du nouveau Pokémon:")
    label.pack()

    selected_type = tk.StringVar(type_window)
    selected_type.set(TYPES_POKEMON[0])
    dropdown = ttk.Combobox(type_window, textvariable=selected_type, values=TYPES_POKEMON)
    dropdown.pack()

    def on_ok():
        selected_type_str = selected_type.get()  # Removed .lower() here
        type_window.destroy()
        return selected_type_str

    button = tk.Button(type_window, text="Valider", command=on_ok)
    button.pack()

    type_window.grab_set()  # Prevents interaction with the main window until the type_window is closed
    type_window.wait_window()
    return on_ok()
    
# Function to add a new Pokemon
def add_new_pokemon():
    name = simpledialog.askstring("Nouveau Pokémon", "Entrez le nom du nouveau Pokémon:")

    if name:
        p_type_str = ask_type()
        
        if p_type_str is not None:
            try:
                p_type = Types[p_type_str]
                abilities = simpledialog.askstring("Nouveau Pokémon", "Entrez les capacités du nouveau Pokémon:")

                if abilities is not None:
                    new_pokemon = Pokemon(name, p_type, abilities.split(', '))
                    pokeListArr.append(new_pokemon)
                    save_pokemons(pokeListArr)
                    listbox.insert(tk.END, new_pokemon.name)
                    messagebox.showinfo("Succès", "Le nouveau Pokémon a été ajouté avec succès !")
                else:
                    messagebox.showerror("Erreur", "Veuillez saisir les capacités pour ajouter un nouveau Pokémon.")
            except KeyError:
                messagebox.showerror("Erreur", "Le type de Pokémon sélectionné n'est pas valide.")
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner un type pour ajouter un nouveau Pokémon.")
    else:
        messagebox.showerror("Erreur", "Veuillez saisir un nom pour ajouter un nouveau Pokémon.")

# Add a button to the main window to add a new Pokemon
boutonTwo = tk.Button(fenetre, text="Nouveau Pokémon", command=add_new_pokemon)
boutonTwo.pack()

# Add a label to the main window with the version number
etiquetteTwo = tk.Label(fenetre, text="[Pokédex]- v1 by Kody san")
etiquetteTwo.pack()

# Start the main event loop
fenetre.mainloop()