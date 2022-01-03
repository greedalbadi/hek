from PIL import Image as Im
from PIL.ExifTags import TAGS
import os.path
from exceptions import *



class Image:
    def isfile(self, filename):

        result =  os.path.exists(filename) # checking if file exist

        if result == False:
            raise FileNotFound(f"file not found: {filename}") # file exception

        elif result == True:
            return result


    def extracexif(self, filename: str):
        if Image.isfile(filename) != False: # making sure that file exist
            try:
                image = Im.open(filename) # process image with pillow
                image_data = {} # creating data dict
                for key, value in image._getexif().items(): # extracting exif data from image
                    if key in TAGS: # checking data
                        image_data[TAGS[key]] = value # adding keys and values to the dict
                return image_data
            except Exception as error:
                raise ExifExtractError(f"exif error : {error}")
Image = Image()