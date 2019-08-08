import thorlabs_tsi_sdk
from thorlabs_tsi_sdk.tl_camera import TLCameraSDK, TLCamera, Frame
from thorlabs_tsi_sdk.tl_camera_enums import SENSOR_TYPE
from thorlabs_tsi_sdk.tl_mono_to_color_processor import MonoToColorProcessorSDK
import numpy as np
#from PIL import Image

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
        print('operation mode is ' + str(self.cam.operation_mode))

    # Call destructors for SDK and Camera objects 
    def closeCamera(self):
        self.cam.dispose()
        self.camSesh.dispose()

        
    # Takes a picture and returns an np.array of the image
    def takePicture(self):
        self.cam.frames_per_trigger_zero_for_unlimited = 1
        self.cam.arm(1)
        print('is armed' + str(self.cam.is_armed))
        self.cam.issue_software_trigger()
        temp = self.cam.get_pending_frame_or_null()
        image = np.copy(temp.image_buffer)
        self.cam.disarm()
        return image

cam = Camera()
image = cam.takePicture()
print(image)
        



