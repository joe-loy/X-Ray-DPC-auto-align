import serial
import os
import ctypes

"""
MotorController

This class is used to control a rig containing five picomotors which can be used to adjust five different
degrees of freedom of movement for the gratings. This class uses the axis convention usually applied in optics
of making the z axis the direction in which the x-rays pass through the gratings. Thus, the X axis controls
side to side movement of the grating.

"""

motdll = ctypes.CDLL("./usbdll.dll")
print(motdll)
result = motdll.newp_usb_open_devices(4000, True)
result2 = motdll.newp_usb_init_system()
print(result)
print(result2)



"""
class MotorController():

    
    # Establish serial connection with motors and setup controller
    def __init__():
        # Load dll to use USB driver API
        motdll = windll.LoadLibrary("C:\\usbdll.dll")
        # Open all picomotor controllers using the product ID(4000)

        open_motors = motdll.newp_usb_open_devices(4000, False)
        open_momtors.argtypes = (ctypes.c_int, ctypes.c_bool, ctypes.POINTER(ctypes.int))
        # After all devices have been opened and Device Keys are known,
        # initialize the system to be ready for serial commands.
        initMotor = motdll.lib.newp_usb_init_system(0, address of device state changed function)
        initMotor.argtypes = (ctypes.c_init, ctypes.POINTER(c_void))
        
        
    # Close serial connection with the MotorController when finished
    def closeMotorController():
        motdll.newp_usb_uninit_system()
        

    # Used to translationally move grating in X-axis relative to current position
    def moveX(direction, distance):
        # Using the distance and the direction, create proper ascii command
        
        # Send usb serial command to translation motor in X-axis
        send_command = motdll.newp_usb_send_ascii(deviceID, command, strlen(command))
        send_command.argtypes = (ctypes.c_long, ctypes.POINTER(ctypes.c_char), ctypes.c_ulong)

    # Used to translationally move grating in Z-axis relative to current position
    def moveZ(direction, distance):
        # Using the distance and the direction, create proper ascii command
        
        # Send usb serial command to translation motor in Z-axis
        send_command = motdll.newp_usb_send_ascii(deviceID, command, strlen(command))
        send_command.argtypes = (ctypes.c_long, ctypes.POINTER(ctypes.c_char), ctypes.c_ulong)    
        
    # Used to turn grating about X-axis relative to current orientation
    def turnX(direction, theta):
        # Using the direction and the desired angle of rotation, create proper
        # ascii command to send to controller

        # Send usb serial command to rotational motor in X-axis
        send_command = motdll.newp_usb_send_ascii(deviceID, command, strlen(command))
        send_command.argtypes = (ctypes.c_long, ctypes.POINTER(ctypes.c_char), ctypes.c_ulong)
        
    # Used to turn grating about Y-axis relative to current orientation
    def turnY(direction, theta):
        # Using the direction and the desired angle of rotation, create proper
        # ascii command to send to controller

        # Send usb serial command to rotational motor in Y-axis
        send_command = motdll.newp_usb_send_ascii(deviceID, command, strlen(command))
        send_command.argtypes = (ctypes.c_long, ctypes.POINTER(ctypes.c_char), ctypes.c_ulong)
        
    # Used to turn grating about Z-axis relative to current orientation
    def turnZ(direction, theta):
        # Using the direction and the desired angle of rotation, create proper
        # ascii command to send to controller

        # Send usb serial command to rotational motor in Z-axis
        send_command = motdll.newp_usb_send_ascii(deviceID, command, strlen(command))
        send_command.argtypes = (ctypes.c_long, ctypes.POINTER(ctypes.c_char), ctypes.c_ulong)
        
    # Used to autoalign gratings based on picture of the fiducial image
    def autoAllign():
    
"""
