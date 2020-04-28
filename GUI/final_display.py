from tkinter import *
from tkinter import Tk, Label, font, Button
import os
os.system('pwd ; ls')
logfile = open("logged_results1", "r")
links = logfile.readlines()
finalstring = ""
for i in range(len(links)):
	if "#######" in links[i]:
		if not "Traceback" in links[i+2]: 
			finalstring = finalstring + links[i+2] + "\n"  + links[i+1] + "\n \n" 
class SearchQuery:
        def __init__(self, master):
                self.master = master
                self.titlefnt = font.Font(family='System', size=25, weight='bold')
                self.labelfnt = font.Font(family='System', size=15, weight='bold')
                self.pad = Frame(master, width=650, height=45, bg="black")
                self.pad1 = Frame(master, width=650, height=45, bg="black")
                self.pad2 = Frame(master, width=650, height=25, bg="black")
                self.pad3 = Frame(master, width=650, height=25, bg="black")
                self.label = Label(master, text="Jackalope Search Engine", font=self.titlefnt, pady=10, padx=5, bg="black", fg="white")
                self.label1 = Label(master, text="Search Results:", font=self.labelfnt, pady=10, padx=5, bg="black", fg="white")
                self.label2 = Text(master, font=self.labelfnt, pady=10, padx=5, bg="black", fg="white")
                self.label2.insert(1.0, finalstring)
                self.label2.configure(state="disabled", height = 45, width = 100)
                self.pad.grid()
                self.label.grid()
                self.pad1.grid()
                self.label1.grid()
                self.pad2.grid()
                self.label2.grid()                                                                                                     
                self.pad3.grid()

branch = Tk()
branch.title("JSE")
branch.configure(bg="black")
search = SearchQuery(branch)
branch.mainloop()
