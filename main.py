import tkinter as tk
from io import BytesIO
import PIL.Image, PIL.ImageTk
import pypokedex
import urllib3

window = tk.Tk()
window.geometry("600x500")
window.title("PyDex")
window.config(padx=10, pady=10)

title_label = tk.Label(window, text="PyDex")
title_label.config(font=("Helvetica", 40))
title_label.pack(padx=10, pady=10)

#SPRITE
pokemon_image = tk.Label(window)
pokemon_image.pack(padx=10, pady=10)

#INFO
pokemon_information = tk.Label(window)
pokemon_information.config(font=("Helvetica", 20))
pokemon_information.pack(padx=10, pady=10)

#TYPES
pokemon_types = tk.Label(window)
pokemon_types.config(font=("Helvetica", 20))
pokemon_types.pack(padx=10, pady=10)

#FUNCTION
def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))
    
    #IMAGE FROM HTTP
    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))

    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    #FORMATTING
    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}".title())
    pokemon_types.config(text=" - ".join([t for t in pokemon.types]).title())


label_id_name = tk.Label(window, text="ID or Name")
label_id_name.config(font=("Helvetica", 20))
label_id_name.pack(padx=10, pady=10)

text_id_name = tk.Text(window, height=1)
text_id_name.config(font=("Helvetica", 20))
text_id_name.pack(padx=10, pady=10)

btn_load = tk.Button(window, text="Who's That Pokemon?", command=load_pokemon)
btn_load.config(font=("Helvetica", 20))
btn_load.pack(padx=10, pady=10)

window.mainloop()
