"""
Sources:
https://www.daniweb.com/programming/software-development/code/440946/display-an-image-from-a-url-tkinter-python
https://python-forum.io/Thread-Display-image-from-URL

"""

import tkinter as tk
from PIL import ImageTk, Image
import os
import requests
from io import BytesIO
from ImageRipper import images


def display(imageurl):
    root = tk.Tk()
    img_url = imageurl
    response = requests.get(img_url)
    img_data = response.content
    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
    panel = tk.Label(root, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    root.mainloop()


url = "https://en.wikipedia.org/w/index.php?title=Special:Search&search=Pokémon"
print(url)
links = images(url)
for image in links:
    display(image)
print("done")