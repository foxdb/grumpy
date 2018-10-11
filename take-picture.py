import os
import subprocess
from datetime import datetime

import cv2

# local configuration
PICTURES_DIRECTORY = '/home/ben/.gitshots'

branch_name = subprocess.check_output(
    ['git', 'status']).split('\n')[0].replace('On branch ', '').replace('/', '')

filename = PICTURES_DIRECTORY + '/' + \
    datetime.now().strftime('%Y%m%d_%H-%M-%S') + '-' + branch_name + '.jpg'

cam = cv2.VideoCapture(0)
return_value, image = cam.read()
cv2.imwrite(filename, image)
cam.release()
