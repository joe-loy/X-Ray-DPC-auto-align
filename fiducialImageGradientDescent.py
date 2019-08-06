import numpy as np
import scipy as sp
import matplotlib.pylab as plt
from skimage.io import imread
import cv2
from skimage.transform import radon, rescale


"""

fiducialImageGradientDescent.py

This script is used to implement the functions necessary to perform the
gradient descent which will be used by the motor controller in order to
automatically align gratings. The gradient descent will be based on
two seperate images of radon transforms of the fiducial images, which will
be used as components of a cost function that will be used to implement
the gradient descent.

"""



image = cv2.imread('phantom.png', 0)  # read image in grayscale
I = image - np.mean(image)
sinogram = radon(I)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.5))

ax1.set_title("Original")
ax1.imshow(image, cmap=plt.cm.Greys_r)

theta = np.linspace(0., 180., max(image.shape), endpoint=False)
sinogram = radon(image, theta=theta, circle=True)
ax2.set_title("Radon transform\n(Sinogram)")
ax2.set_xlabel("Projection angle (deg)")
ax2.set_ylabel("Projection position (pixels)")
ax2.imshow(sinogram, cmap=plt.cm.Greys_r,
           extent=(0, 180, 0, sinogram.shape[0]), aspect='auto')

fig.tight_layout()
plt.show()

class imageGradientDescent():
    # Image dimensions of image to be radon transformed
    X_PIXELS = 100
    Y_PIXELS = 100
    X_MIDPOINT = X_PIXELS / 2
    Y _MIDPOINT = Y_PIXELS / 2
    
    
    def __init__(self):

    # Plot radon transform of Intensity vs projection angle and return sinogram
    def plot_radon_angle(self, image):
        print(0)

    # Plot radon transform of Intensity vs x-pixels and return sinogram
    def plot_radon_x_pixels(self, image):
        print(0)

    # Plot radon transform of Intensity vs y-pixels and return sinogram
    def plot_radon_y_pixels(self, image):
        print(0)

    # Evaluate cost function based on the three sinograms to be generated from image
    def cost_function(self):
        print(0)



    


