# X-Ray-DPC-auto-align

# Dependencies, Equipment, and Setup
  This repository utilizes numpy, scipy, pyUSB, PIL, Tkinter, ThorCam Python API, and the Newport USB Driver for much of the serious implementation of the program. I plan on attaching a text file full of the pip commands necessary to install all necessary dependencies for the project. The equipment needed to perform the alignment are the ThorCam CS895MU, Newport 8742 Motor Controller, 6 Newport 8742 Picomotors, a HeNe laser, a grating, and a fiducial mark. An image of the entire setup will be shown below

# Starting the GUI
  In order to use this code, clone the repo and install the necessary dependencies. After the proper dependencies are installed, one must plug in the ThorCam CS895MU and the Newport 8742 Controller into the computer that you will be running the GUI from. If these components are not plugged in, as of now the program will crash. 
 
# Using the GUI
  Once the GUI is running, the user can perform a variety of different commands. The user can command an individual to move a desired distance in a desired direction. Distances are measured in nanometers(nm) and the directions are established using standard coordinates for optics, with the positive z direction being defined as moving away from the x-ray setup. 
