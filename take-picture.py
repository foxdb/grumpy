import os
import cv2
import subprocess
import ConfigParser
from datetime import datetime

config = ConfigParser.ConfigParser()
config.read("config.ini")

branch_name = subprocess.check_output(
    ['git', 'status']).split('\n')[0].replace('On branch ', '').replace('/', '')

filename = config.get('folders', 'pictures_directory') + '/' + \
    datetime.now().strftime('%Y%m%d_%H-%M-%S') + '-' + branch_name + '.jpg'

cam = cv2.VideoCapture(0)
return_value, image = cam.read()
cv2.imwrite(filename, image)
cam.release()
