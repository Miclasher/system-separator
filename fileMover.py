from operator import le
import os
import shutil
from unipath import Path
dir = Path(r"C:\Users\Miclasher\Desktop\testconfig")
target = dir.parent
tempArray = os.listdir(dir)
for i in range(len(tempArray)):
    shutil.move(dir + '\\' + tempArray[i], target)