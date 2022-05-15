import ctypes
from os import getlogin
def setWallpaper(configName='testconfig'):
    USER_NAME = getlogin()
    dir = r'C:\Users\{0}\Documents\SystemSeparatorCfgs\{1}\wallpaper.jpg'.format(USER_NAME, configName)
    print(dir)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, dir, 0)
if __name__ == '__main__':
    setWallpaper()
else:
    pass
