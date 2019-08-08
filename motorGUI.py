from tkinter import*

"""
class: motorGUI

This class is used to create a GUI that will allow a user to specify commands that will allow
for manual adjustments of the motor in each of the five dimensions of freedom(x,z,thetaX,thetaY,thetaZ)
by specifying a direction and magnitude. The z-axis goes directly towards the gratings, the x-axis is
parallel to the plates holding the gratings, and the rotational axis are based off of the specified
coordinates above.

"""

class motorGUI:

    def __init__(self, master):
        self.master = master
        master.title("Picomotor Controller Alignment GUI")



        # Create all buttons and textboxes for GUI

        # Make translational x-axis control component
        self.xLabel_t = Label(master, text="Translational X-axis")
        self.xDist = IntVar()
        self.x_dist = Entry(master, textvariable=self.xDist, width=10)
        self.xSlide = IntVar(value=0)
        self.x_slide1 = Radiobutton(master, text="Left", variable=self.xSlide, value=0)
        self.x_slide2 = Radiobutton(master, text="Right", variable=self.xSlide, value=1)
        # Test command for button that should allow motors to move according to user input in translational x-axis
        # TO DO: Using direction and distance from entry field, command motors to move
        def xMove():
            distance = self.x_dist.get()
            direc = self.xSlide.get()
            print("zTurn selected, distance = " + str(distance) + " , direction = " + str(direc))
        self.x_button_t = Button(master, command=xMove, text="Move motors")

        # Make translational z-axis control component
        self.zLabel_t = Label(master, text="Translational Z-axis")
        self.zDist = IntVar()
        self.z_dist = Entry(master, textvariable=self.zDist, width=10)
        self.zSlide = IntVar(value=0)
        self.z_slide1 = Radiobutton(master, text="Left", variable = self.zSlide, value = 0)
        self.z_slide2 = Radiobutton(master, text="Right", variable = self.zSlide, value = 1)
        # Test command for button that should allow motors to move according to user input in translational z-axis
        # TO DO: Using direction and distance from entry field, command motors to move
        def zMove():
            distance = self.z_dist.get()
            direc = self.zSlide.get()
            print("zMove selected, distance = " + str(distance) + " , direction = " + str(direc))
        self.z_button_t = Button(master, command=zMove, text="Move motors")

        # Make rotational x-axis control component
        self.xLabel_r = Label(master, text="Rotational X-axis")
        self.xTheta = IntVar()
        self.x_theta = Entry(master, textvariable=self.xTheta, width=10)
        self.x_turn = IntVar(value=0)
        self.x_turn1 = Radiobutton(master, text="Left", variable = self.x_turn, value = 0)
        self.x_turn2 = Radiobutton(master, text="Right", variable = self.x_turn, value = 1)
        # Test command for button that should allow motors to move according to user input in rotational x-axis
        # TO DO: Using direction and distance from entry field, command motors to move
        def xTurn():
            distance = self.x_theta.get()
            direc = self.xTheta.get()
            print("xTurn selected, distance = " + str(distance) + " , direction = " + str(direc))

        self.x_button_r = Button(master, command=xTurn, text="Move motors")

        # Make rotational y-axis control component
        self.yLabel_r = Label(master, text="Rotational Y-axis")
        self.yTheta = IntVar()
        self.y_theta = Entry(master, textvariable=self.yTheta, width=10)
        self.y_turn = IntVar(value=0)
        self.y_turn1 = Radiobutton(master, text="Left", variable = self.y_turn, value = 0)
        self.y_turn2 = Radiobutton(master, text="Right", variable = self.y_turn, value = 1)
        # Test command for button that should allow motors to move according to user input in rotational y-axis
        # TO DO: Using direction and distance from entry field, command motors to move
        def yTurn():
            distance = self.y_theta.get()
            direc = self.yTheta.get()
            print("yTurn selected, distance = " + str(distance) + " , direction = " + str(direc))
        self.y_button_r = Button(master, command=yTurn, text="Move motors")

        # Make rotational z-axis control component
        self.zLabel_r = Label(master, text="Rotational Z-axis")
        self.zTheta = IntVar()
        self.z_theta = Entry(master, textvariable=self.zTheta, width=10)
        self.z_turn = IntVar(value=0)
        self.z_turn1 = Radiobutton(master, text="Left", variable = self.z_turn, value = 0)
        self.z_turn2 = Radiobutton(master, text="Right", variable = self.z_turn, value = 1)
        # Test command for button that should allow motors to move according to user input in rotational z-axis
        # TO DO: Using direction and distance from entry field, command motors to move
        def zTurn():
            distance = self.z_theta.get()
            direc = self.zTheta.get()
            print("zTurn selected, distance = " + str(distance) + " , direction = " + str(direc))
        self.z_button_r = Button(master, command=zTurn, text="Move motors")

        # Create picture and auto-align buttons
        def snapPic():
            print("Snap pic")
        self.takePic = Button(master, command=snapPic, text="Take Picture")

        def align():
            print("auto-align")
        self.autoAlign = Button(master, command=align, text="Auto-Align")



        # Organize buttons on screen

        # Organize buttons controlling translational motion in x-axis
        self.xLabel_t.grid(column=0, row=0)
        self.x_dist.grid(column=0, row=1)
        self.x_slide1.grid(column=0, row=2)
        self.x_slide2.grid(column=8, row=2)
        self.x_button_t.grid(column=0, row=3)

        # Organize buttons controlling translational motion in z-axis
        self.zLabel_t.grid(column=20, row=0)
        self.z_dist.grid(column=20, row=1)
        self.z_slide1.grid(column=20, row=2)
        self.z_slide2.grid(column=28, row=2)
        self.z_button_t.grid(column=20, row=3)

        # Organize buttons controlling rotational motion in x-axis
        self.xLabel_r.grid(column=0, row=20)
        self.x_theta.grid(column=0, row=21)
        self.x_turn1.grid(column=0, row=22)
        self.x_turn2.grid(column=8, row=22)
        self.x_button_r.grid(column=0, row=23)

        # Organize buttons controlling rotational motion in y-axis
        self.yLabel_r.grid(column=20, row=20)
        self.y_theta.grid(column=20, row=21)
        self.y_turn1.grid(column=20, row=22)
        self.y_turn2.grid(column=28, row=22)
        self.y_button_r.grid(column=20, row=23)

        # Organize buttons controlling rotational motion in z-axis
        self.zLabel_r.grid(column=40, row=20)
        self.z_theta.grid(column=40, row=21)
        self.z_turn1.grid(column=40, row=22)
        self.z_turn2.grid(column=48, row=22)
        self.z_button_r.grid(column=40, row=23)

        # Organize take picture and auto-align buttons
        self.takePic.grid(column=0, row=40)
        self.autoAlign.grid(column=20, row = 40)

    
root = Tk()
my_gui = motorGUI(root)
root.mainloop()


    
