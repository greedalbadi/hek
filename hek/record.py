import datetime
import cv2
import numpy
import numpy as np
from PIL import ImageGrab
import os.path
import warnings
from .info import webcam_info
import pyautogui
class _webcam:
    def __init__(self):
        # shared record class is class that contains functions that multiple functions needs or neither
        self._shared_record = _shared_recored()
    def get_frame(self, camera: int=webcam_info.DEFAULT_CAMERA_NUM, capturing=False):
        # camera argument is which camera will capture
        # camera variable is to capture picture
        if capturing == False:
            camera = cv2.VideoCapture(camera)
        else:
            camera = self.camera
        # read picture frame
        ret, frame = camera.read()
        # return captured frame
        _ = frame
        return frame

    '''
    def _listfiles(self, path: str='.'):
        # return list of files/images in folder
        return glob.glob(path)
    '''
    def frame_to_image(self, filename: str, frame: numpy.ndarray):
        # check if file exists before writing if it's exists It'll just throw a warning
        '''
        if _webcam._isfile(self, filename) == True:
            warnings.warn(f"WARNING: {filename} already exists.")
        '''
        # write image
        return cv2.imwrite(filename, frame)




    def webcamshot(self, filename: str, camera: int=webcam_info.DEFAULT_CAMERA_NUM):
        frame = _webcam.get_frame(self, camera=camera)

        return _webcam.frame_to_image(self, filename=filename, frame=frame)
    def capture_video(self,filename: str, seconds: int, camera: int=webcam_info.DEFAULT_CAMERA_NUM, size=None, fps: int=int(webcam_info.DEFAULT_FPS)):
        # check if file exists before writing if it's exists It'll just throw a warning
        if _webcam._isfile(self, filename) == True:
            warnings.warn(f"WARNING: {filename} already exists.")
        self.captures = []
        # prepare camera
        self.camera = cv2.VideoCapture(camera)
        # process time to be able to control the while loop run time
        entered_time = datetime.datetime.now() + datetime.timedelta(seconds=seconds)

        # basically It'll run until the entered end's
        while datetime.datetime.now() < entered_time:
            '''
            Now It'll keep saving camera frames until the time end's
            capturing is true because already prepared the camera
            '''
            frame = _webcam.get_frame(self, camera=camera, capturing=True)
            '''
            saving camera frames in self.captures
            '''
            self.captures.append(frame)

        '''
         writer is the function that used to write the videos frames
         frame is the last entered frame in self.captures
        '''
        writer = self._shared_record.write_video(filename, frame=self.captures[-1], size=size, fps=fps)
        for frame in range(len(self.captures)):
            writer.write(self.captures[frame])

        # just like releasing a pen from the paper
        return writer.release()
    def _isfile(self, filename: str):
        # check if path exists
        return os.path.exists(filename)


class _shared_recored:
    # shared record class is class that contains functions that multiple functions needs or neither
    def colorframe(self, frame):

        # color frame
        return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    def write_video(self,filename: str='', frame=None, size=None, fps: int=int(webcam_info.DEFAULT_FPS)):

        # get frame size
        height, width, layers = frame.shape

        # making sure to get frame size
        if size == None:
            size = (width, height)
        # process frame to video file
        return cv2.VideoWriter(filename,
                                  cv2.VideoWriter_fourcc(*'DIVX'),
                                  int(fps),
                                  size
                                  )

class _screen:
    def __init__(self):
        # shared record class is class that contains functions that multiple functions needs or neither
        self._shared_record = _shared_recored()


    def screen_frame(self):
        # grab screen size
        width, height = pyautogui.size()
        '''
        apply the screen size to tuple object
        '''
        siz = (0, 0, int(width), int(height))
        # screenshot frame
        frame = ImageGrab.grab(siz)
        # turn the frame to ndarray data type
        frame = np.array(frame)

        '''
        return fixed color frame
        '''
        return self._shared_record.colorframe(frame)


    def screenshot(self, filename: str):
        frame = _screen.screen_frame(self)
        '''
        get screen frame and write it to file
        '''
        return cv2.imwrite(filename, frame)


    def capture_video(self, filename: str, seconds: int, fps: int=int(webcam_info.DEFAULT_FPS), size=None):
        self.captures = []

        # process time to be able to control the while loop run time
        entered_time = datetime.datetime.now() + datetime.timedelta(seconds=seconds)

        # basically It'll run until the entered end's
        while datetime.datetime.now() < entered_time:

            frame = _screen.screen_frame(self)
            '''
            append the screenshot data to captures list
            '''
            self.captures.append(frame)
        '''
         writer is the function that used to write the videos frames
         frame is the last entered frame in self.captures
        '''
        writer = self._shared_record.write_video(filename, frame=self.captures[-1], size=size, fps=fps)
        for frame in range(len(self.captures)):
            writer.write(self.captures[frame])
        return writer.release()



screen = _screen()
webcam = _webcam()
record = _shared_recored()