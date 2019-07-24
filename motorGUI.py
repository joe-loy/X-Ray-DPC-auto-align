from tkinter import*



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


"""
class motorGUI(tk.Frame):
    def __init__(self, master):
        self.master = master
        master.title("Picomotor Controller Alignment GUI")
        
        # Helper methods to construct the GUI
        self.createButtons(self)
        self.createTextBoxes(self)

        # Application Variables
        self.x_dist = 0
        self.z_dist = 0
        self.x_theta = 0
        self.y_theta = 0
        self.z_theta = 0

        
    # Creates Buttons responsible
    def createButtons(self):
        self.x_slide_dir = Radiobutton(text
        self.z_slide_dir =
        self.x_turn_dir =
        self.y_turn_dir = 
        self.z_turn_dir =
        
    def createTextBoxes(self):
"""

    
