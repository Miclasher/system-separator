import os
import shutil
def demoveFiles(configName="testconfig"):
    USER_NAME = os.getlogin()
    target = r"C:\Users\\{0}\Documents\SystemSeparatorCfgs\\{1}".format(USER_NAME, configName)
    dir = r"C:\Users\\{0}\Desktop".format(USER_NAME)
    tempArray = os.listdir(dir)
    for i in range(len(tempArray)):
        shutil.move(dir + '\\' + tempArray[i], target)
if __name__ == "__main__":
    demoveFiles()
else:
    pass