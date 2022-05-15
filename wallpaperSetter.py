import ctypes
dir = r'C:\Users\Miclasher\Desktop\testconfig\wallpaper.jpg'
ctypes.windll.user32.SystemParametersInfoW(20, 0, dir, 0)