from tkinter import *
from tkinter import Tk, Label, font

class Mainpage:
        def __init__(self, master):
                self.master = master
                self.titlefnt = font.Font(family='System', size=25, weight='bold')
                self.labelfnt = font.Font(family='System', size=15, weight='bold')
        ########### The pads just make things look nice #########################################
                self.pad = Frame(master, width=600, height=45, bg = "black")
                self.pad1 = Frame(master, width=600, height=45, bg="black")
                self.pad2 = Frame(master, width=600, height=45, bg="black")
                self.pad3 = Frame(master, width=600, height=45, bg="black")
                self.pad4 = Frame(master, width=600, height=45, bg="black")
                self.pad5 = Frame(master, width=600, height=25, bg="black")
                self.pad6 = Frame(master, width=600, height=25, bg="black")
                self.pad7 = Frame(master, width=600, height=25, bg="black")
        #######################################################################################
                self.label = Label(master, text="Jackalope Search Engine", font = self.titlefnt, pady = 10, padx = 5, bg = "black", fg = "white")
                self.label1 = Label(master, text="Server username:", font = self.labelfnt, pady = 10, padx = 5, bg = "black", fg = "white")
                self.label2 = Label(master, text="Server IP Address:", font = self.labelfnt, pady = 10, padx = 5, bg ="black", fg = "white")
                self.label3 = Label(master, text="Server password:", font=self.labelfnt, pady=10, padx=5, bg="black", fg="white")
        ########### The "entry" widgets are the text boxes that take the text ###################
                self.entry = Entry(master)
                self.entry.focus_set()
                self.entry1 = Entry(master)
                self.entry1.focus_set()
                self.entry2 = Entry(master)
                self.entry2.focus_set()
        #########################################################################################
        ########### When you click the save buttons the text saves to these variables ###########
                self.entrytext = ""
                self.entrytext1 = ""
                self.entrytext2 = ""
        #########################################################################################
        ########### These are the functions that are called when you click the buttons ##########
                def save():
                    entrytext = self.entry.get()
                def save1():
                    entrytext1 = self.entry1.get()
                def save2():
                    entrytext2 = self.entry2.get()
        ########################################################################################
                self.button = Button(master, text="save", width=10, command=save)
                self.button1 = Button(master, text="save", width=10, command=save1)
                self.button2 = Button(master, text="save", width=10, command=save2)
        ########### The "grid()" command actually puts the widgets in the display box. #########
                self.pad.grid()
                self.label.grid() #jackalope search engine
                self.pad1.grid()
                self.label1.grid() #server username
                self.entry.grid()
                self.pad5.grid()
                self.button.grid()
                self.pad2.grid()
                self.label3.grid() #server password
                self.entry1.grid()
                self.pad6.grid()
                self.button1.grid()
                self.pad3.grid()
                self.label2.grid() #server ip address
                self.entry2.grid()
                self.pad7.grid()
                self.button2.grid()
                self.pad4.grid()
        #########################################################################################

# note this page is shorter than the main page, but still performs the same functionality
class SearchQuery:
    def __init__(self, master):
        self.master = master
        self.titlefnt = font.Font(family = 'System', size = 25, weight = 'bold')
        self.labelfnt = font.Font(family = 'System', size = 15, weight = 'bold')

        self.pad = Frame(master, width = 600, height = 45, bg = "black")
        self.pad1 = Frame(master, width = 600, height = 45, bg = "black")
        self.pad2 = Frame(master, width = 600, height = 25, bg = "black")
        self.pad3 = Frame(master, width = 600, height = 25, bg = "black")

        self.label = Label(master, text = "Jackalope Search Engine", font = self.titlefnt, pady = 10, padx = 5, bg = "black", fg = "white")
        self.label1 = Label(master, text = "Search Query:", font = self.labelfnt, pady = 10, padx = 5, bg = "black", fg = "white")

        self.entry = Entry(master)
        self.entry.focus_set()
        
        self.entrytext = ""

        def save():
            entrytext = self.entry.get()
        
        self.button = Button(master, text = "search", width = 10, command = save)
        
        self.pad.grid()
        self.label.grid()
        self.pad1.grid()
        self.label1.grid()
        self.entry.grid()
        self.pad2.grid()
        self.button.grid()
        self.pad3.grid()
   
root = Tk()
root.title("JSE")
root.configure(bg = "black")
gui = Mainpage(root)
#gui = SearchQuery(root)
root.mainloop()
