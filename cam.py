import os
from ctypes import*
from thorlabs_tsi_sdk.tl_camera import TLCameraSDK, TLCamera, Frame
from thorlabs_tsi_sdk.tl_camera_enums import SENSOR_TYPE
from thorlabs_tsi_sdk.tl_mono_to_color_processor import MonoToColorProcessorSDK

"""
Camera

This class is used to control the CS895MU compact scientific camera
in order to send over images of the fiducial images produced by the
laser. 

"""
class Camera():

    def __init__(self, camSesh, cam):

        # Create instance of SDK in order to construct a camera
        self.camSesh = TLCameraSDK()
        camList = camSesh.discover_available_cameras()
        self.cam = camSesh.open_camera('08153')

    # Call destructors for SDK and Camera objects 
    def closeCamera(self):
        self.cam.dispose()
        self.camSesh.dispose()
    # Takes a picture and returns an np.array of the image
    def takePicture(self):
        self.cam.arm()
        temp = self.cam.get_pending_frame_or_null()
        image = np.copy(temp)
        return image
        



