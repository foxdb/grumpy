import os
import subprocess
from datetime import datetime

import pygame.camera
import pygame.image

# local configuration
PICTURES_DIRECTORY = '/home/ben/.gitshots'

branch_name = subprocess.check_output(
    ['git', 'status']).split('\n')[0].replace('On branch ', '').replace('/', '')

filename = PICTURES_DIRECTORY + '/' + \
    datetime.now().strftime('%Y%m%d_%H-%M-%S') + '-' + branch_name + '.jpg'

pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
cam.start()
img = cam.get_image()
pygame.image.save(img, filename)
pygame.camera.quit()
