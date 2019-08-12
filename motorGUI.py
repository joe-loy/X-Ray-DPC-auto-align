from tkinter import*
from PIL import*
from PIL import Image
from PIL import ImageTk
from cam import Camera
import matplotlib.pylab as plt
import numpy as np
import cv2
#from motorController import MotorController
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

        # Initalize camera
        self.cam = Camera()


        # Create all buttons and textboxes for GUI
        
        # Create default image and image button for images to be displayed
        self.img = Image.open('z500_r7_0_d8_aligned.tiff')
        
        self.img = self.img.resize((3840//10, 2748//10)) 
        self.dispImg = ImageTk.PhotoImage(self.img)
        self.panel = Label(master, image=self.dispImg)
             

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
            direc = self.x_turn.get()
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
            direc = self.y_turn.get()
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
            direc = self.z_turn.get()
            print("zTurn selected, distance = " + str(distance) + " , direction = " + str(direc))
        self.z_button_r = Button(master, command=zTurn, text="Move motors")




        # Create picture and auto-align buttons
        def snapPic():
            self.img = Image.fromarray(self.cam.takePicture(), 'L')
            self.img.show()
            width, height = self.img.size
            print(width,height)
            self.img = self.img.resize((width//10, height//10)) 
            self.dispImg = ImageTk.PhotoImage(self.img)
            self.panel.configure(image=self.dispImg)
            print("Snap pic")
        self.takePic = Button(master, command=snapPic, text="Take Picture")




        def align():
            print("auto-align")
        self.autoAlign = Button(master, command=align, text="Auto-Align")



        # Organize buttons on screen

        # Organize buttons controlling translational motion in x-axis
        self.xLabel_t.grid(column=1, row=9001)
        self.x_dist.grid(column=1, row=9002)
        self.x_slide1.grid(column=1, row=9003)
        self.x_slide2.grid(column=9, row=9003)
        self.x_button_t.grid(column=1, row=9004)

        # Organize buttons controlling translational motion in z-axis
        self.zLabel_t.grid(column=20, row=9001)
        self.z_dist.grid(column=20, row=9002)
        self.z_slide1.grid(column=20, row=9003)
        self.z_slide2.grid(column=28, row=9003)
        self.z_button_t.grid(column=20, row=9004)

        # Organize buttons controlling rotational motion in x-axis
        self.xLabel_r.grid(column=1, row=9020)
        self.x_theta.grid(column=1, row=9021)
        self.x_turn1.grid(column=1, row=9022)
        self.x_turn2.grid(column=9, row=9022)
        self.x_button_r.grid(column=1, row=9023)

        # Organize buttons controlling rotational motion in y-axis
        self.yLabel_r.grid(column=20, row=9020)
        self.y_theta.grid(column=20, row=9021)
        self.y_turn1.grid(column=20, row=9022)
        self.y_turn2.grid(column=28, row=9022)
        self.y_button_r.grid(column=20, row=9023)

        # Organize buttons controlling rotational motion in z-axis
        self.zLabel_r.grid(column=40, row=9020)
        self.z_theta.grid(column=40, row=9021)
        self.z_turn1.grid(column=40, row=9022)
        self.z_turn2.grid(column=48, row=9022)
        self.z_button_r.grid(column=40, row=9023)

        # Organize take picture and auto-align buttons
        self.takePic.grid(column=1, row=9040)
        self.autoAlign.grid(column=20, row = 9040)

        # Organize photo canvas
        self.panel.grid(column=100, row=0)
        

    
root = Tk()
my_gui = motorGUI(root)
root.mainloop()


    
