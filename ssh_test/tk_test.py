from tkinter import Tk, Label, Button

# This is a simple GUI to test if you've configured X11 and Xming correctly.

# Save this program to the /home/yourusername directory on the CentOS machine

# This program should be called from a terminal opend on your Windows Ubuntu Shell, this could be done via the command:
#   sshpass -p 'somepassword' ssh -Y username@192.168.1.xxx python3.7 tk_test.py


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()
        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
    def greet(self):
        print("Greetings!")
root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
