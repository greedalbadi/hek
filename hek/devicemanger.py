import psutil, os, sys
from .info import system as si
import urllib.request

class System:

    def oname(self, what: str = None):
        if what:
            platform = what
        else:
            platform = sys.platform

        for key, value in si._SYS_PLATFORMS.items():
            if isinstance(value, list):
                for v in value:
                    if v == platform:
                        return key
            else:
                if value == platform:
                    return key
        else:
            return platform


    # get current username
    def username(self, fix=True):

        # get username data
        data = psutil.Process().username()

        # checking os
        if os.name == "nt":
            # if fix is False It'll return devicename\username
            if fix == True:
                if '\\' in data:
                    # split username from devicename
                    user = data.split("\\")[1]
                    return user
            else:
                # return all data without spliting
                return data
        else:
            # if is not windows os It'll just return data
            return data

    def download_content(self, url: str, path: str = None):
        # download link content

        # checking if given path
        if path != None:
            # checking if path containing folder
            if "\\" in path:
                # extract file name from path
                filename = url.split('\\')[-1]
            else:
                # if the path doesn't contain folders
                filename = path
        else:
            # if path is not given It'll just extract the file name from the url
            filename = url.split('/')[-1]
        # download content ..
        urllib.request.urlretrieve(url, filename)

        return True


system = System()
