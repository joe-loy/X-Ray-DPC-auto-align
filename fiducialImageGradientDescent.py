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
import heapq
#from .motorController.py import motorController

"""

fiducialImageGradientDescent.py

This script is used to implement the functions necessary to perform the
gradient descent which will be used by the motor controller in order to
automatically align gratings. The gradient descent will be based on
two seperate images of radon transforms of the fiducial images, which will
be used as components of a cost function that will be used to implement
the gradient descent.

"""



"""
# Open image
img = cv2.imread('z500_r7_0_d8_aligned.tiff', 0)

# resize image
scale_percent = 20 # percent of original size
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
print(properties["prominences"].max())
print(sp.signal.find_peaks(absmax_sinogram, prominence=100))

# Plot original image and absMax of Intensity of radon transform vs projection angle
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.5))
ax1.set_title("Original")
ax1.imshow(img, cmap=plt.cm.Greys_r)
ax2.set_title("Radon transform\n(Sinogram)")
ax2.set_xlabel("Radii (pixels)")
ax2.set_ylabel("Maximum Intensity")
ax2.plot(peaks, absmax_sinogram[peaks], 'x')
print(peaks)
print(absmax_sinogram[peaks])
vals = [peaks, absmax_sinogram[peaks]]
print(vals)
print(vals[1][0])
fig.tight_layout()
plt.show()
print(0)
"""


class imageGradientDescent():
    # Constants that will be necessary for evaluation of cost function
    X_PIXELS = 549
    Y_PIXELS = 768
    X_MIDPOINT = X_PIXELS / 2
    Y_MIDPOINT = Y_PIXELS / 2
    X_QPOINT = X_MIDPOINT / 2
    Y_QPOINT = Y_MIDPOINT / 2
    IDEAL_Z_DISP = 0
    EPSILON = .05
    MAX_STEPS = 1000000000000000
    
    
    
    def __init__(self):
        # Initalize the camera and motorController for use in the gradient descent
        #self.cam = Camera()
        #self.controller = MotorController()
        
        print(0)

    # Plot radon transform of Intensity vs projection angle and return sinogram
    def plot_radon_angle_x(self, image):
        # Open image
        img = cv2.imread('z500_r7_0_d8_aligned.tiff', 0)

        # resize image
        scale_percent = 20 # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        print(dim)
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
        print(absmax_loc)

        

    # Plot radon transform of Intensity vs x-pixels and return sinogram
    def plot_radon_pixels_x(self, image):
        # Open image
        img = cv2.imread('z500_r7_0_d8_aligned.tiff', 0)

        # resize image
        scale_percent = 20 # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        print(dim)
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

        print(properties["prominences"].max())
        print(absmax_sinogram.max())
        print(absmax_sinogram.argmax())
        print(heapq.nlargest(3, absmax_sinogram))
        print(sp.signal.find_peaks(absmax_sinogram, prominence=100))

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
        print(0)

    # Plot radon transform of Intensity vs projection angle and return sinogram
    def plot_radon_angle_y(self, image):
        # Open image
        img = cv2.imread('z500_r7_0_d8_aligned.tiff', 0)

        # resize image
        scale_percent = 20 # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        print(dim)
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
        print(absmax_loc)


    # Plot radon transform of Intensity vs y-pixels and return sinogram
    def plot_radon_y_pixels(self, image):
        # Open image
        img = cv2.imread('z500_r7_0_d8_aligned.tiff', 0)

        # resize image
        scale_percent = 20 # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        print(dim)
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        # Radon transform resized image
        nSteps = height
        thetaStart = 80
        thetaEnd = 100
        thetas = np.linspace(thetaStart, thetaEnd, nSteps)
        sinogram = radon(resized, theta=thetas, circle=True)
        absmax_sinogram = np.amax(sinogram, axis=1)
        peaks, properties = sp.signal.find_peaks(absmax_sinogram, prominence=100)
        print(properties["prominences"].max())
        print(sp.signal.find_peaks(absmax_sinogram, prominence=100))

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
        print(0)

    

    # Returns location of absolute max of Intensity vs Projection angle radon transform
    def getRadonTransform1Params(self):
        # Open image
        img = cv2.imread('z500_r7_0_d8_aligned.tiff', 0)

        # resize image
        scale_percent = 20 # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        print(dim)
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
        print(absmax_loc)
        return absmax_loc
        
        
        
    # Returns tuple of abs max and rel max locations and magnitudes
    # Returns [rmax1_mag_x, rmax1_loc_x, amax_mag_x, amax_loc_x, rmax2_mag_x, rmax2_loc_x]
    def getRadonTransform2Params(self):
        # Open image
        img = cv2.imread('z500_r7_0_d8_aligned.tiff', 0)

        # resize image
        scale_percent = 20 # percent of original size
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

        # Take absmax of intensity in dimensions of pixels
        absmax_sinogram = np.amax(sinogram, axis=1)
        peaks, properties = sp.signal.find_peaks(absmax_sinogram, prominence=100)
        vals = [peaks, absmax_sinogram[peaks]]
        return vals
        
    # Returns tuple of abs max and rel max locations and magnitudes
    # Returns [rmax1_mag_y, rmax1_loc_y, amax_mag_y, amax_loc_y, rmax2_mag_y, rmax2_loc_y]
    def getRadonTransform3Params(self):
        # Open image
        img = cv2.imread('z500_r7_0_d8_aligned.tiff', 0)

        # resize image
        scale_percent = 20 # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        print(dim)
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
        print(absmax_loc)
        return absmax_loc

    # Ye boi
    def getRadonTransform4Params(self):
        # Open image
        img = cv2.imread('z500_r7_0_d8_aligned.tiff', 0)

        # resize image
        scale_percent = 20 # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        print(dim)
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
        vals = [peaks, absmax_sinogram[peaks]]
        return vals

    # Evaluate cost function based on the three sinograms to be generated from image
    def eval_cost_function(self):
        # Values needed for evaluation of cost function
        # TO DO: FILL IN 0 with proper values from radon transforms

        xparams = self.getRadonTransform2Params()
        yparams = self.getRadonTransform4Params()
        print(xparams)
        print(yparams)
        
        zdisp = 0 - self.getRadonTransform1Params()
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
        

        
        s1 = np.sqrt(np.square(self.IDEAL_Z_DISP - zdisp))
        s2 = np.sqrt(np.square(self.X_MIDPOINT - amax_loc_x))
        s3 = np.sqrt(np.square(self.Y_MIDPOINT - amax_loc_y))
        s4 = np.sqrt(np.square(self.X_QPOINT - rmax1_loc_x))
        s5 = np.sqrt(np.square(self.X_MIDPOINT + self.X_QPOINT - rmax2_loc_x))
        s6 = np.sqrt(np.square(self.Y_QPOINT - rmax1_loc_y))
        s7 = np.sqrt(np.square(self.Y_MIDPOINT + self.Y_QPOINT - rmax2_loc_y))
        s8 = np.sqrt(np.square(rmax1_mag_x - rmax2_mag_x))
        s9 = np.sqrt(np.square(rmax1_mag_y - rmax2_mag_y))
        s10 = np.sqrt(np.square(amax_mag_x - rmax1_mag_x - rmax2_mag_x))
        s11 = np.sqrt(np.square(amax_mag_y - rmax1_mag_y - rmax2_mag_y))
        print(str(s1) + ',' + str(s2) + ',' + str(s3) + ',' + str(s4) + ',' + str(s5) + ',' + str(s6))
        costFunction = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10 + s11
        
        return costFunction

        
    # 
    def gradientDescent(self):
        # Initiliaze variables to keep track of number of steps and the step size
        numSteps = 0
        stepSize = 1

        # Take a picture
        # evaluate cost function based on the picture
        # while (cf > EPSILON && numSteps < MAX_STEPS)
            # Pick a motor randomly to move in random direction
            # numSteps++
            # Take a picture & evaluate new_cf
            # while (new_cf < cf)
                # Tweak same motor in same direction
                # numSteps++
                # cf = new_cf
                # new_cf = eval_cf
                

leggo = imageGradientDescent()
print(leggo.eval_cost_function())


    


