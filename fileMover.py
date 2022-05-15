import os
import shutil
USER_NAME = os.getlogin()
dir = r"C:\Users\\{0}\Desktop\testconfig".format(USER_NAME)
target = r"C:\Users\\{0}\Desktop".format(USER_NAME)
tempArray = os.listdir(dir)
tempArray.remove("wallpaper.jpg")
for i in range(len(tempArray)):
    shutil.move(dir + '\\' + tempArray[i], target)