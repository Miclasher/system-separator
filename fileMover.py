import os
import shutil
def moveFiles(configName="testconfig"):
    USER_NAME = os.getlogin()
    dir = r"C:\Users\\{0}\Documents\SystemSeparatorCfgs\\{1}".format(USER_NAME, configName)
    target = r"C:\Users\\{0}\Desktop".format(USER_NAME)
    tempArray = os.listdir(dir)
    tempArray.remove("wallpaper.jpg")
    for i in range(len(tempArray)):
        shutil.move(dir + '\\' + tempArray[i], target)
if __name__ == "__main__":
    moveFiles()
else:
    pass