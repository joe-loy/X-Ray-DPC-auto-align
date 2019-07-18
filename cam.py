import os
from ctypes import*
from thorlabs_tsi_sdk.tl_camera import TLCameraSDK, TLCamera, Frame
from thorlabs_tsi_sdk.tl_camera_enums import SENSOR_TYPE
from thorlabs_tsi_sdk.tl_mono_to_color_processor import MonoToColorProcessorSDK

class Camera():

    def __init__(self, camSesh, cam):

        # Create instance of SDK in order to construct a camera
        self.camSesh = TLCameraSDK()
        camList = camSesh.discover_available_cameras()
        self.cam = camSesh.open_camera('08153')

    def closeCamera(self):
        self.cam.dispose()
        self.camSesh.dispose()

    def takePicture(self):
        self.cam.arm()
        temp = self.cam.get_pending_frame_or_null()
        image = np.copy(temp)
        return image
        



