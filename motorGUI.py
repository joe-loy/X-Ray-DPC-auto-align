from tkinter import*
from PIL import*
from PIL import Image
from PIL import ImageTk
import matplotlib.pylab as plt
import numpy as np
import cv2
from fiducialImageGradientDescent import imageGradientDescent
"""
class: motorGUI

This class is used to create a GUI that will allow a user to specify commands that will allow
for manual adjustments of the motor in each of the five dimensions of freedom(x,z,thetaX,thetaY,thetaZ)
by specifying a direction and magnitude. The z-axis goes directly towards the gratings, the x-axis is
parallel to the plates holding the gratings, and the rotational axis are based off of the specified
coordinates above.

"""

class motorGUI:
    """ add after master.title("blah blag")
        
    """
    
    def __init__(self, master):
        self.master = master
        master.title("Picomotor Controller Alignment GUI")

        # Initalize fiducial gradient descent class(which starts motors and camera)
        self.alignmentSystem = imageGradientDescent()
        self.cam = self.alignmentSystem.cam
        self.controller = self.alignmentSystem.controller

        # Create all buttons and textboxes for GUI
        
        # Create default image and image button for images to be displayed
        self.img = Image.open('z500_r7_0_d8_aligned.tiff')
        width, height = self.img.size        
        self.img = self.img.resize((width//10, height//10)) 
        self.dispImg = ImageTk.PhotoImage(self.img)
        self.panel = Label(master, image=self.dispImg)


        # Make translational x-axis control component
        self.xLabel_t = Label(master, text="Translational X-axis")
        self.xDist_t = IntVar()
        self.xEntry_dist_t = Entry(master, textvariable=self.xDist_t, width=10)
        self.xDir_t = IntVar(value=0)
        self.xDir_t_neg = Radiobutton(master, text="Left", variable=self.xDir_t, value=0)
        self.xDir_t_pos = Radiobutton(master, text="Right", variable=self.xDir_t, value=1)
        # Command translational x motors to move based on GUI entries
        def xMove_t():
            distance = self.xEntry_dist_t.get()
            direc = self.xDir_t.get()
            self.controller.moveX(direc, distance)
            print("xMove_t selected, distance = " + str(distance) + " , direction = " + str(direc))
        self.x_button_t = Button(master, command=xMove_t, text="Move motors")


        # Make translational z-axis control component
        self.zLabel_t = Label(master, text="Translational Z-axis")
        self.zDist_t = IntVar()
        self.zEntry_dist_t = Entry(master, textvariable=self.zDist_t, width=10)
        self.zDir_t = IntVar(value=0)
        self.zDir_t_neg = Radiobutton(master, text="Backward", variable = self.zDir_t, value = 0)
        self.zDir_t_pos = Radiobutton(master, text="Forward", variable = self.zDir_t, value = 1)
        # Command translational z motors to move based on GUI entries
        def zMove_t():
            distance = self.zEntry_dist_t.get()
            direc = self.zDir_t.get()
            self.controller.moveZ(direc, distance)
            print("zMove_t selected, distance = " + str(distance) + " , direction = " + str(direc))
        self.z_button_t = Button(master, command=zMove_t, text="Move motors")



        # Make rotational x-axis control component
        self.xLabel_r = Label(master, text="Rotational X-axis")
        self.xDist_r = IntVar()
        self.xEntry_dist_r = Entry(master, textvariable=self.xDist_r, width=10)
        self.xDir_r = IntVar(value=0)
        self.xDir_r_neg = Radiobutton(master, text="Left", variable = self.xDir_r, value = 0)
        self.xDir_r_pos = Radiobutton(master, text="Right", variable = self.xDir_r, value = 1)
        # Command rotational x motors to move based on GUI entries
        def xMove_r():
            distance = self.xEntry_dist_r.get()
            direc = self.xDir_r.get()
            self.controller.turnX(direc, distance)
            print("xMove_r selected, distance = " + str(distance) + " , direction = " + str(direc))
        self.x_button_r = Button(master, command=xMove_r, text="Move motors")



        # Make rotational y-axis control component
        self.yLabel_r = Label(master, text="Rotational Y-axis")
        self.yDist_r = IntVar()
        self.yEntry_dist_r = Entry(master, textvariable=self.yDist_r, width=10)
        self.yDir_r = IntVar(value=0)
        self.yDir_r_neg = Radiobutton(master, text="Left", variable = self.yDir_r, value = 0)
        self.yDir_r_pos = Radiobutton(master, text="Right", variable = self.yDir_r, value = 1)
        # Command rotational y motors to move based on GUI entries
        def yMove_r():
            distance = self.yEntry_dist_r.get()
            direc = self.yDir_r.get()
            self.controller.turnY(direc, distance)
            print("yMove_r selected, distance = " + str(distance) + " , direction = " + str(direc))
        self.y_button_r = Button(master, command=yMove_r, text="Move motors")



        # Make rotational z-axis control component
        self.zLabel_r = Label(master, text="Rotational Z-axis")
        self.zDist_r = IntVar()
        self.zEntry_dist_r = Entry(master, textvariable=self.zDist_r, width=10)
        self.zDir_r = IntVar(value=0)
        self.zDir_r_neg = Radiobutton(master, text="Left", variable = self.zDir_r, value = 0)
        self.zDir_r_pos = Radiobutton(master, text="Right", variable = self.zDir_r, value = 1)
        # Command rotational z motors to move based on GUI entries 
        def zMove_r():
            distance = self.zEntry_dist_r.get()
            direc = self.zDir_r.get()
            self.controller.turnZ(direc, distance)
            print("zMove_r selected, distance = " + str(distance) + " , direction = " + str(direc))
        self.z_button_r = Button(master, command=zMove_r, text="Move motors")



        # Create picture and auto-align buttons
        def snapPic():
            # Must cast array type as uint (thorcam uses ushorts to store values)
            self.img = Image.fromarray(self.cam.takePicture().astype('uint8'), 'L')
            width, height = self.img.size
            self.img = self.img.resize((width//10, height//10)) 
            self.dispImg = ImageTk.PhotoImage(self.img)
            self.panel.configure(image=self.dispImg)
        self.takePic = Button(master, command=snapPic, text="Take Picture")



        def align():
            self.alignmentSystem.gradientDescent()
            print("auto align done")
        self.autoAlign = Button(master, command=align, text="Auto-Align")



        # Organize buttons on screen

        # Organize buttons controlling translational motion in x-axis
        self.xLabel_t.grid(column=1, row=9001)
        self.xEntry_dist_t.grid(column=1, row=9002)
        self.xDir_t_neg.grid(column=1, row=9003)
        self.xDir_t_pos.grid(column=9, row=9003)
        self.x_button_t.grid(column=1, row=9004)

        # Organize buttons controlling translational motion in z-axis
        self.zLabel_t.grid(column=20, row=9001)
        self.zEntry_dist_t.grid(column=20, row=9002)
        self.zDir_t_neg.grid(column=20, row=9003)
        self.zDir_t_pos.grid(column=28, row=9003)
        self.z_button_t.grid(column=20, row=9004)

        # Organize buttons controlling rotational motion in x-axis
        self.xLabel_r.grid(column=1, row=9020)
        self.xEntry_dist_r.grid(column=1, row=9021)
        self.xDir_r_neg.grid(column=1, row=9022)
        self.xDir_r_pos.grid(column=9, row=9022)
        self.x_button_r.grid(column=1, row=9023)

        # Organize buttons controlling rotational motion in y-axis
        self.yLabel_r.grid(column=20, row=9020)
        self.yEntry_dist_r.grid(column=20, row=9021)
        self.yDir_r_neg.grid(column=20, row=9022)
        self.yDir_r_pos.grid(column=28, row=9022)
        self.y_button_r.grid(column=20, row=9023)

        # Organize buttons controlling rotational motion in z-axis
        self.zLabel_r.grid(column=40, row=9020)
        self.zEntry_dist_r.grid(column=40, row=9021)
        self.zDir_r_neg.grid(column=40, row=9022)
        self.zDir_r_pos.grid(column=48, row=9022)
        self.z_button_r.grid(column=40, row=9023)

        # Organize take picture and auto-align buttons
        self.takePic.grid(column=1, row=9040)
        self.autoAlign.grid(column=20, row = 9040)

        # Organize photo canvas
        self.panel.grid(column=100, row=0)
        

    
root = Tk()
my_gui = motorGUI(root)
root.mainloop()


    
