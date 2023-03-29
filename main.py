import cv2 as cv
from OpenCV import take_photo
from inter import invok_ui

if '__main__' == __name__:
    callback = invok_ui(lambda name: take_photo(name))
    print(callback)