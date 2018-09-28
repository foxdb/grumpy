import os

import pygame.camera
import pygame.image
from datetime import datetime
import boto3

s3 = boto3.resource('s3')

BUCKET_NAME = 'grumpy-ben'
FILE_PREFIX = 'grumpy'

filename = datetime.now().strftime('%Y%m%d_%H-%M-%S') + '.jpg'

pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
cam.start()
img = cam.get_image()
pygame.image.save(img, filename)
pygame.camera.quit()

print "Nice shot!!"

try:
    data = open(filename, 'rb')
    s3.Bucket(BUCKET_NAME).put_object(Key=FILE_PREFIX +
                                      '/' + filename, Body=data)
    os.remove(filename)
except:
    print 'Upload issue!'
