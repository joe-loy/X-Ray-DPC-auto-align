import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

from skimage.io import imread
from skimage.data import shepp_logan_phantom
from skimage.transform import radon, rescale

from PIL import Image


"""
fiducialImageGradientDescent.py
This script is used to implement the functions necessary to perform the
gradient descent which will be used by the motor controller in order to
automatically align gratings. The gradient descent will be based on
two seperate images of radon transforms of the fiducial images, which will
be used as components of a cost function that will be used to implement
the gradient descent.
"""


image = shepp_logan_phantom()
image = rescale(image, scale=0.4, mode='reflect', multichannel=False)

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


