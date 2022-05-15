import os
import shutil
dir = r"C:\Users\Miclasher\Desktop\testconfig"
target = r"C:\Users\Miclasher\Desktop"
tempArray = os.listdir(dir)
tempArray.remove("wallpaper.jpg")
for i in range(len(tempArray)):
    shutil.move(dir + '\\' + tempArray[i], target)