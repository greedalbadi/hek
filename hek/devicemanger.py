import psutil, os


class System:


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
system = System()
