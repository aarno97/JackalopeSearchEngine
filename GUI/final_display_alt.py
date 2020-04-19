import tkinter as tk
import webbrowser

logfile = open("logged_results1", "r")
links = logfile.readlines()
article = ""
hyperlink = ""

def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

root = tk.Tk()
root.title("JSE")
root.configure(bg="black")

titlefnt = font.Font(family='System', size=25, weight='bold')
labelfnt = font.Font(family='System', size=15, weight='bold')
label1 = tk.Label(root, text = "Jackalope Search Engine", font=titlefnt, bg="black", fg="white")
label2 = tk.Label(root, text="Search Results:", font=labelfnt, bg="black", fg="white")
label1.pack()
label2.pack()

for i in range(len(links)):
    if "#######" in links[i]:
        if not "Traceback" in links[i+2]:
            article = links[i+2]
            hyperlink = links[i+1]
            label3 = tk.Label(root, bg = "black")
            label4 = tk.Label(root, text=article, bg="black", fg="white")
            label5 = tk.Label(root, text=hyperlink, bg="black", fg="blue", cursor="hand2")
            label3.pack()
            label4.pack()
            label5.pack()
            label5.bind("<Button-1>", callback)

root.mainloop()
