import numpy as np
import scipy as sp
import matplotlib.pylab as plt
from skimage.io import imread
import cv2
from skimage.transform import radon, rescale
from cam import Camera
from PIL import*
from PIL import Image
from PIL import ImageTk
from motorController import MotorController
import collections

"""
fiducialImageGradientDescent.py
This script is used to implement the functions necessary to perform the
gradient descent which will be used by the motor controller in order to
automatically align gratings. The gradient descent will be based on
two seperate images of radon transforms of the fiducial images, which will
be used as components of a cost function that will be used to implement
the gradient descent.
"""

class imageGradientDescent():
    # Constants that will be necessary for evaluation of cost function
    X_PIXELS = 2160 // 10
    Y_PIXELS = 2160 // 10
    X_MIDPOINT = X_PIXELS / 2
    Y_MIDPOINT = Y_PIXELS / 2
    IDEAL_Z_DISP = 0
    EPSILON = 90
    MAX_STEPS = 100000
    
    
    
    def __init__(self):
        # Initalize the camera and motorController for use in the gradient descent
        self.cam = Camera()
        self.controller = MotorController()
        
        

    # Plot radon transform of Intensity vs projection angle and return sinogram
    def plot_radon_angle_x(self, image):
        # Open image
        img = image

        # resize image
        scale_percent = 10 # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

        # Radon transform resized image
        nSteps = width
        thetaStart = -10
        thetaEnd = 10
        thetas = np.linspace(thetaStart, thetaEnd, nSteps)
        sinogram = radon(resized, theta=thetas, circle=True)

        # Take absolute max of sinogram across axis and find location where it occurs
        absmax_sinogram = np.amax(sinogram, axis=0)
        absmax_loc = thetas[np.where(absmax_sinogram == absmax_sinogram.max())]

        # Plot original image and absMax of Intensity of radon transform vs projection angle
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.5))
        ax1.set_title("Original")
        ax1.imshow(img, cmap=plt.cm.Greys_r)
        ax2.set_title("Radon transform\n(Sinogram)")
        ax2.set_xlabel("Projection angle (deg)")
        ax2.set_ylabel("Maximum Intensity")
        ax2.plot(thetas, absmax_sinogram, '-')
        fig.tight_layout()
        plt.show()

    # Plot radon transform of Intensity vs x-pixels and return sinogram
    def plot_radon_pixels_x(self, image):
        # Open image
        img = image

        # resize image
        scale_percent = 10 # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

        # Radon transform resized image
        nSteps = height
        thetaStart = 80
        thetaEnd = 100
        thetas = np.linspace(thetaStart, thetaEnd, nSteps)
        sinogram = radon(resized, theta=thetas, circle=True)

        # Take absmax of intensity in dimensions of pixels
        absmax_sinogram = np.amax(sinogram, axis=1)
        peaks, properties = sp.signal.find_peaks(absmax_sinogram, prominence=100)

        # Plot original image and absMax of Intensity of radon transform vs projection angle
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.5))
        ax1.set_title("Original")
        ax1.imshow(img, cmap=plt.cm.Greys_r)
        ax2.set_title("Radon transform\n(Sinogram)")
        ax2.set_xlabel("Projection angle (deg)")
        ax2.set_ylabel("Maximum Intensity")
        ax2.plot(peaks, absmax_sinogram[peaks], 'x')
        fig.tight_layout()
        plt.show()

    # Plot radon transform of Intensity vs projection angle and return sinogram
    def plot_radon_angle_y(self, image):
        # Open image
        img = image

        # resize image
        scale_percent = 10 # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

        # Radon transform resized image
        nSteps = height
        thetaStart = 80
        thetaEnd = 100
        thetas = np.linspace(thetaStart, thetaEnd, nSteps)
        sinogram = radon(resized, theta=thetas, circle=True)

        # Take absolute max of sinogram across axis and find location where it occurs
        absmax_sinogram = np.amax(sinogram, axis=0)
        absmax_loc = thetas[np.where(absmax_sinogram == absmax_sinogram.max())]

        # Plot original image and absMax of Intensity of radon transform vs projection angle
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.5))
        ax1.set_title("Original")
        ax1.imshow(img, cmap=plt.cm.Greys_r)
        ax2.set_title("Radon transform\n(Sinogram)")
        ax2.set_xlabel("Projection angle (deg)")
        ax2.set_ylabel("Maximum Intensity")
        ax2.plot(thetas, absmax_sinogram, '-')
        fig.tight_layout()
        plt.show()


    # Plot radon transform of Intensity vs y-pixels and return sinogram
    def plot_radon_y_pixels(self, image):
        # Open image
        img = image

        # resize image
        scale_percent = 10 # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        
        # Radon transform resized image
        nSteps = height
        thetaStart = 80
        thetaEnd = 100
        thetas = np.linspace(thetaStart, thetaEnd, nSteps)
        sinogram = radon(resized, theta=thetas, circle=True)
        absmax_sinogram = np.amax(sinogram, axis=1)
        peaks, properties = sp.signal.find_peaks(absmax_sinogram, prominence=100)

        # Plot original image and absMax of Intensity of radon transform vs projection angle
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.5))
        ax1.set_title("Original")
        ax1.imshow(img, cmap=plt.cm.Greys_r)
        ax2.set_title("Radon transform\n(Sinogram)")
        ax2.set_xlabel("Radii (pixels)")
        ax2.set_ylabel("Maximum Intensity")
        ax2.plot(peaks, absmax_sinogram[peaks], 'x')
        fig.tight_layout()
        plt.show()

    

    # Returns location of absolute max of Intensity vs Projection angle radon transform
    def getRT_angle_x(self, image, scale):
        # Create image object
        img = image

        # resize image
        scale_percent = scale # percent of original size
        width , height = img.shape
        width = (width * scale_percent // 100)
        height = (height * scale_percent // 100)
        dim = [width, height]
        img = np.resize(img, dim)

        # Radon transform resized image
        nSteps = width
        thetaStart = -10
        thetaEnd = 10
        thetas = np.linspace(thetaStart, thetaEnd, nSteps)
        sinogram = radon(img, theta=thetas, circle=True)

        # Take absolute max of sinogram across axis and find location where it occurs
        absmax_sinogram = np.amax(sinogram, axis=0)
        absmax_loc = thetas[np.where(absmax_sinogram == absmax_sinogram.max())]
        return absmax_loc
        
        
        
    # Returns tuple of abs max and rel max locations and magnitudes
    # Returns [rmax1_mag_x, rmax1_loc_x, amax_mag_x, amax_loc_x, rmax2_mag_x, rmax2_loc_x]
    def getRT_pixel_x(self, image, scale):
        # Open image
        img = image
        

        # resize image
        scale_percent = scale # percent of original size
        width, height = img.shape 
        width = (width * scale_percent // 100)
        height = (height * scale_percent // 100)
        dim = [width, height]
        img = np.resize(img, dim)

        # Radon transform resized image
        nSteps = width
        thetaStart = -10
        thetaEnd = 10
        thetas = np.linspace(thetaStart, thetaEnd, nSteps)
        sinogram = radon(img, theta=thetas, circle=True)

        # Take absmax of intensity in dimensions of pixels
        absmax_sinogram = np.amax(sinogram, axis=1)
        peaks, properties = sp.signal.find_peaks(absmax_sinogram, height=180, distance=width/4)
        vals = [peaks, absmax_sinogram[peaks]]
        return vals
        
    # Returns tuple of abs max and rel max locations and magnitudes
    # Returns [rmax1_mag_y, rmax1_loc_y, amax_mag_y, amax_loc_y, rmax2_mag_y, rmax2_loc_y]
    def getRT_angle_y(self, image, scale):
        # Open image
        img = image

        # resize image
        scale_percent = scale # percent of original size
        width, height = img.shape
        width = (width * scale_percent // 100)
        height = (height * scale_percent // 100)
        dim = [width, height]
        img = np.resize(img, dim)

        # Radon transform resized image
        nSteps = height
        thetaStart = 80
        thetaEnd = 100
        thetas = np.linspace(thetaStart, thetaEnd, nSteps)
        sinogram = radon(img, theta=thetas, circle=True)

        # Take absolute max of sinogram across axis and find location where it occurs
        absmax_sinogram = np.amax(sinogram, axis=0)
        absmax_loc = thetas[np.where(absmax_sinogram == absmax_sinogram.max())]
        return absmax_loc

    # Ye boi
    def getRT_pixel_y(self, image, scale):
        # Open image
        img = image

        # resize image
        scale_percent = scale # percent of original size
        width, height = img.shape
        width = (width * scale_percent // 100)
        height = (height * scale_percent // 100)
        dim = [width, height]
        img = np.resize(img, dim)

        # Radon transform resized image
        nSteps = height
        thetaStart = 80
        thetaEnd = 100
        thetas = np.linspace(thetaStart, thetaEnd, nSteps)
        sinogram = radon(img, theta=thetas, circle=True)

        # Take absmax of intensity in dimensions of pixels
        absmax_sinogram = np.amax(sinogram, axis=1)
        peaks, properties = sp.signal.find_peaks(absmax_sinogram, height=180, distance=width/4)
        vals = [peaks, absmax_sinogram[peaks]]
        return vals

    # Evaluate cost function based on the three sinograms to be generated from image
    def calc_cf(self, image, scale):
        # Values needed for evaluation of cost function
        xparams = self.getRT_pixel_x(image, scale)
        yparams = self.getRT_pixel_y(image, scale)
        print('x params ' + str(xparams) + ' y params ' + str(yparams))
        zdisp_x = 0 - self.getRT_angle_x(image, scale)
        zdisp_y = 0 - self.getRT_angle_y(image, scale)
        rmax1_loc_x = xparams[0][0]
        rmax1_mag_x = xparams[1][0]
        rmax2_loc_x = xparams[0][2]
        rmax2_mag_x = xparams[1][2]
        rmax1_loc_y = yparams[0][0]
        rmax1_mag_y = yparams[1][0]
        rmax2_loc_y = yparams[0][2]
        rmax2_mag_y = yparams[1][2]
        amax_loc_x = xparams[0][1]
        amax_mag_x = xparams[1][1]
        amax_loc_y = yparams[0][1]
        amax_mag_y = yparams[1][1]
        

        # Cost function components
        s1 = np.square(self.IDEAL_Z_DISP - zdisp_x)
        s2 = np.square(self.X_MIDPOINT - amax_loc_x)
        s3 = np.square(rmax1_mag_x - rmax2_mag_x)
        s4 = np.square((amax_loc_x - rmax1_loc_x) - (rmax2_loc_x - amax_loc_x))
        s5 = np.square(self.IDEAL_Z_DISP - zdisp_y)
        s6 = np.square(self.Y_MIDPOINT - amax_loc_y)
        s7 = np.square(rmax1_mag_y - rmax2_mag_y)
        s8 = np.square((amax_loc_y - rmax1_loc_y) - (rmax2_loc_y - amax_loc_y))

        #print(str(s1) + ',' + str(s2) + ',' + str(s3) + ',' + str(s4) + ',' + str(s5) + ',' + str(s6) + ',' + str(s7) + ',' + str(s8))
        costFunction = np.sqrt(s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8)
        print(str(costFunction))
        return int(costFunction)

    # Determines the stepSize based on value of cost function
    def calc_stepSize(self, cf):
        
        if cf > 0 and cf < 100:
            stepSize = 1
            return stepSize
        elif cf >= 100 and cf <= 200:
            stepSize = 5
            return stepSize
        elif cf > 200 and cf < 300:
            stepSize = 10
            return stepSize
        else:
            stepSize = 25
            return stepSize

    # Determines image resolution based on value of cf
    def calc_scaleFactor(self, cf):

        if cf > 0 and cf < 100:
            scaleFactor = 25
            return scaleFactor
        elif cf >= 100 and cf <= 200:
            scaleFactor = 20
            return scaleFactor
        else:
            scaleFactor = 10
            return scaleFactor
        
    # 
    def gradientDescent(self):
        # Create dequeue of motors for descent
        motorDeque = collections.deque([1,2,3,4,5])
        # Initiliaze variables to keep track of number of steps and the step size
        numSteps = 0
        stepSize = 10
        scale = 10
        

        # Take a picture
        image = self.cam.takePicture().astype('uint8')
        # evaluate cost function based on the picture
        cf = self.calc_cf(image, scale)
        scale = self.calc_scaleFactor(cf)
        stepSize = self.calc_stepSize(cf)
        
        if (cf < self.EPSILON):
            return
        


        while (cf > self.EPSILON and numSteps < self.MAX_STEPS):
            # Start with first motor in dequeue
            curMotor = motorDeque.popleft()
            # Make sure to place element at end of deque
            motorDeque.append(curMotor)
            # numSteps++
            numSteps += 1
            # Choose a direction to try adjusting the motor
            direction = 0
            
            # Move appropriate motor

            # Rotational Z motor
            if curMotor == 1:
                self.controller.turnZ(direction, stepSize) 
            # Rotational X motor
            elif curMotor == 2:
                self.controller.turnX(direction, stepSize)
            # Rotational Y motor
            elif curMotor == 3:
                self.controller.turnY(direction, stepSize)
            # Translational X motor
            elif curMotor == 4:
                self.controller.moveX(direction, stepSize)
            # Translational Z motor
            else:
                self.controller.moveZ(direction, stepSize)
            
            # Take a picture & evaluate new_cf
            image = self.cam.takePicture().astype('uint8')
            new_cf = self.calc_cf(image, scale)
            scale = self.calc_scaleFactor(new_cf)
            stepSize = self.calc_stepSize(new_cf)
            # From cf determine proper step size and image scale

            # If new_cf is higher, we must go in the other direction
            if new_cf > cf:
                direction = 1
                cf = new_cf

            # If cf is lower than epsilon, break the loop
            if cf < self.EPSILON:
                break
            
            while new_cf <= cf:
                # Tweak same motor in correct direction
                # Move appropriate motor

                # Rotational Z motor
                if curMotor == 1:
                    self.controller.turnZ(direction, stepSize) 
                # Rotational X motor
                elif curMotor == 2:
                    self.controller.turnX(direction, stepSize)
                # Rotational Y motor
                elif curMotor == 3:
                    self.controller.turnY(direction, stepSize)
                # Translational X motor
                elif curMotor == 4:
                    self.controller.moveX(direction, stepSize)
                # Translational Z motor
                else:
                    self.controller.moveZ(direction, stepSize)
                numSteps += 1
                
                cf = new_cf
                image = self.cam.takePicture().astype('uint8')
                new_cf = self.calc_cf(image, scale)
                scale = self.calc_scaleFactor(new_cf)
                stepSize = self.calc_stepSize(new_cf)
                # If cf lower than epsilon, break the loop
                if new_cf < self.EPSILON:
                    break

                


    


