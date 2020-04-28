import tkinter as tk
from tkinter import ttk

import webbrowser

logfile = open("logged_results1", "r")
links = logfile.readlines()
article = ""
hyperlink = ""

def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"), width=600, height=600, bg = "black")

root = tk.Tk()
root.title("JSE")
root.configure(bg="black")

# creates the frame for the article names and links with a scroll bar on the side
container = ttk.Frame(root)
canvas = tk.Canvas(container)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg = "black")

scrollable_frame.bind("<Configure>", myfunction)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

titlefnt = font.Font(family='System', size=25, weight='bold')
labelfnt = font.Font(family='System', size=15, weight='bold')
label1 = tk.Label(root, text = "Jackalope Search Engine", font=titlefnt, bg="black", fg="white")
label2 = tk.Label(root, text="Search Results:", font=labelfnt, bg="black", fg="white")
label1.pack()
label2.pack()

# seperate the article names and links to allow the hyperlink
for i in range(len(links)):
    if "#######" in links[i]:
        if not "Traceback" in links[i+2]:
            article = links[i+2]
            hyperlink = links[i+1]
            label3 = tk.Label(scrollable_frame, bg = "black")
            label4 = tk.Label(scrollable_frame, text=article, bg="black", fg="white")
            label5 = tk.Label(scrollable_frame, text=hyperlink, bg="black", fg="blue", cursor="hand2")
            label3.pack()
            label4.pack()
            label5.pack()
            label5.bind("<Button-1>", callback)

container.pack()
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()
