import fileMover
import wallpaperSetter
import fileDeMover
from os import listdir, getlogin
username = getlogin()
myfile = open(r'C:\Users\\{0}\Documents\SystemSeparatorCfgs\last.txt'.format(username))
lastConfig = myfile.read()
fileDeMover.demoveFiles(lastConfig)
myfile.close()
myfile = open(r'C:\Users\\{0}\Documents\SystemSeparatorCfgs\last.txt'.format(username), 'w')
myfile.close()
configList = listdir(r'C:\Users\\{0}\Documents\SystemSeparatorCfgs'.format(username))
configList.remove("last.txt")
a = 1
while a > 0:
    WantedConfig = input("What do you want to do?({0})".format(configList))
    if WantedConfig in configList:
        myfile = open(r'C:\Users\\{0}\Documents\SystemSeparatorCfgs\last.txt'.format(username), 'w')
        myfile.write('{0}'.format(WantedConfig))
        myfile.close
        fileMover.moveFiles(WantedConfig)
        wallpaperSetter.setWallpaper(WantedConfig)
        a = 0
    else:
        print("Config not found")
        a = 1
