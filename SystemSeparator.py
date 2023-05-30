from fileMover import moveFiles
from wallpaperSetter import setWallpaper
from fileDeMover import demoveFiles
from os import listdir, getlogin
username = getlogin()
myfile = open(r'C:\Users\\{0}\Documents\SystemSeparatorCfgs\last.txt'.format(username))
lastConfig = myfile.read()
demoveFiles(lastConfig)
myfile.close()
myfile = open(r'C:\Users\\{0}\Documents\SystemSeparatorCfgs\last.txt'.format(username), 'w')
myfile.close()
configList = listdir(r'C:\Users\\{0}\Documents\SystemSeparatorCfgs'.format(username))
configList.remove("last.txt")
a = True
while a == True:
    WantedConfig = input("What config do you want to load?({0})".format(configList))
    if WantedConfig in configList:
        myfile = open(r'C:\Users\\{0}\Documents\SystemSeparatorCfgs\last.txt'.format(username), 'w')
        myfile.write('{0}'.format(WantedConfig))
        myfile.close
        moveFiles(WantedConfig)
        setWallpaper(WantedConfig)
        a = False
    else:
        print("Config not found")
        a = True
