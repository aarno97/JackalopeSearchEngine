from tkinter import *
from tkinter import Tk, Label, font, Button
import os
class Mainpage:
        entrysave = ""
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
                self.pad8 = Frame(master, width=600, height=45, bg="black")
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
        ########### Second page is called when you click the button #############################
	########### This system call uses the entered information to log in to the server #######
        ########### and immediately runs the C++ file that is already compiled and calls ########
        ########### the second page of the Gui which is a python file stored on the server. #####
                def secondpage():
                        os.system("sshpass -p \'" + self.entry1.get() + "\' ssh -Y " + self.entry.get() + "@" + self.entry2.get() + " ./runningcinthenineties")
        ########################################################################################
                self.button3 = Button(master, text="Login", width=20, command=secondpage)
        ########### The "grid()" command actually puts the widgets in the display box. #########
                self.pad.grid()
                self.label.grid() #jackalope search engine
                self.pad1.grid()
                self.label1.grid() #server username
                self.entry.grid()
                self.pad5.grid()
                self.pad2.grid()
                self.label3.grid() #server password
                self.entry1.grid()
                self.pad6.grid()
                self.pad3.grid()
                self.label2.grid() #server ip address
                self.entry2.grid()
                self.pad7.grid()
                self.pad4.grid()
                self.button3.grid()
                self.pad8.grid()
        #########################################################################################


root = Tk()
root.title("JSE")
root.configure(bg = "black")
gui = Mainpage(root)
root.mainloop()
