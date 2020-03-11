#chromium-browser --kiosk --noerrors --disable-session-crashed-bubble --disable-infobars --disable-restore-session-state https://duo.google.com/
#pip install vext
#pip install vext.gi
#pip install PyUserInput
#pip install pillow
#pip install pytesseract
#sudo apt-get install tesseract-ocr
#https://askubuntu.com/questions/1048774/disabling-lock-screen-18-04

from pymouse import PyMouse
from time import sleep
from gi.repository import Gdk
import sys

from PIL import Image
import pytesseract
import argparse
import cv2
import os

import os.path
from os import path

filename = "/home/fd/screenshot.png"
filename1 = "/home/fd/screenshot1.png"

def screenshotocr(filename, x1, y1, x2, y2):
	win = Gdk.get_default_root_window()
	h = win.get_height()
	w = win.get_width()
	#pb = Gdk.pixbuf_get_from_window(win, 593, 110, 486, 150)
	pb = Gdk.pixbuf_get_from_window(win, x1, y1, x2, y2)

	if (pb != None):
		#if(path.exists(filename)):
		#	os.remove(filename)

		pb.savev(filename,"png", (), ())
		print("Screenshot saved to screenshot.png.")

		# load the example image and convert it to grayscale
		image = cv2.imread(filename)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		gray = cv2.medianBlur(gray, 3)
		# write the grayscale image to disk as a temporary file so we can
		# apply OCR to it
		filename = "{}.png".format(os.getpid())
		cv2.imwrite(filename, gray)

		# load the image as a PIL/Pillow image, apply OCR, and then delete
		# the temporary file
		text = pytesseract.image_to_string(Image.open(filename))
		os.remove(filename)
		return text

	else:
		print("Unable to get the screenshot.")


def PixelAt(x, y):
  w = Gdk.get_default_root_window()
  pb = Gdk.pixbuf_get_from_window(w, x, y, 1, 1)
  x = int.from_bytes(pb.get_pixels(), "big")    
  return x
 
m = PyMouse()
ft = 0

while True:

    k = screenshotocr(filename, 593, 60, 486, 60)
    print(k)

    if(k == "Duo video call" or k == "Duo voice call"):
    	print("Ahoy")
    	if(ft == 0):
    		ft = 1
    		b = screenshotocr(filename1, 593, 110, 486, 150);
    		print(b)
		
		#check if caller is valid contact
    		if b == "AAAA" or b == "BBBB" or b == "ILT":
    			print("Valid call")
    			#answer call
    			m.click(894, 1102)
    else:
    	ft = 0


    sleep(2.5)
