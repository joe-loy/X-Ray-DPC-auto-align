import os
from ctypes import*
from thorlabs_tsi_sdk.tl_camera import TLCameraSDK, TLCamera, Frame
from thorlabs_tsi_sdk.tl_camera_enums import SENSOR_TYPE
from thorlabs_tsi_sdk.tl_mono_to_color_processor import MonoToColorProcessorSDK
import numpy as np

"""
Camera

This class is used to control the CS895MU compact scientific camera
in order to send over images of the fiducial images produced by the
laser. 

"""
class Camera():

    # Initialize SDK and Camera objects in order to use ThorLabs API functions
    def __init__(self):
        self.camSesh = TLCameraSDK()
        camList = self.camSesh.discover_available_cameras()
        camSerialNum = '08153'
        self.cam = self.camSesh.open_camera(camSerialNum)
        self.cam.operation_mode = SOFTWARE_TRIGGERED
        

    # Call destructors for SDK and Camera objects 
    def closeCamera(self):
        self.cam.dispose()
        self.camSesh.dispose()

        
    # Takes a picture and returns an np.array of the image
    def takePicture(self):
        frames_per_trigger = 1
        self.cam.arm(frames_per_trigger)
        self.cam.issue_software_trigger()
        temp = self.cam.get_pending_frame_or_null()
        print(temp.image_buffer)
        image = np.copy(temp.image_buffer)
        return image

cam = Camera()
image = cam.takePicture()
print(image)
        



