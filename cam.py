import thorlabs_tsi_sdk
from thorlabs_tsi_sdk.tl_camera import TLCameraSDK, TLCamera, Frame
from thorlabs_tsi_sdk.tl_camera_enums import SENSOR_TYPE
from thorlabs_tsi_sdk.tl_mono_to_color_processor import MonoToColorProcessorSDK
import numpy as np
from PIL import Image
import threading
import time

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
        self.cam.operation_mode = thorlabs_tsi_sdk.tl_camera_enums.OPERATION_MODE.SOFTWARE_TRIGGERED
        # Set camera exposure in units of microseconds
        expose_time = 36
        self.cam.exposure_time_us = expose_time
        self.cam.frames_per_trigger_zero_for_unlimited = 1
        self.isStreaming = False

    # Call destructors for SDK and Camera objects 
    def __del__(self):
        self.cam.dispose()
        self.camSesh.dispose()

        
    # Takes a picture and returns an np.array of the image
    def takePicture(self):
        self.cam.frames_per_trigger_zero_for_unlimited = 1
        self.cam.arm(1)
        self.cam.issue_software_trigger()
        temp = self.cam.get_pending_frame_or_null()
        image = np.copy(temp.image_buffer)
        # Extract middle of x coordinates to get square photo (photos are 4096x2160)
        image = image[:, 968:3128]
        self.cam.disarm()
        return image


    # Initialize camera for video recording
    def startVideoStream(self):
        if self.isStreaming:
            print("Video is already streaming")
            return None
        self.isStreaming = True
        self.cam.frames_per_trigger_zero_for_unlimited = 0
        self.cam.arm(1)
        self.cam.issue_software_trigger()
        self.vidThread = threading.Thread(target=self.getVideoStream)
        self.vidThread.start()
        return self
        
    
    # Start 
    def getVideoStream(self):
        temp = self.cam.get_pending_frame_or_null()
        image = np.copy(temp.image_buffer)
        image = image[:, 968:3128]
        return image


    # End a video feed for a camera
    def endVideoStream(self):
        self.isStreaming = False
        self.vidThread.join()
        self.cam.frames_per_trigger_zero_for_unlimited = 1
        self.cam.disarm()


   



