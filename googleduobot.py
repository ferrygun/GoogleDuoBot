from pymouse import PyMouse
from time import sleep
from gi.repository import Gdk
import sys

from PIL import Image
import pytesseract
import argparse
import cv2
import os

filename = "/home/xx/screenshot.png"

def screenshotocr(filename):
	win = Gdk.get_default_root_window()
	h = win.get_height()
	w = win.get_width()
	pb = Gdk.pixbuf_get_from_window(win, 593, 110, 486, 150)
	if (pb != None):
		os.remove(filename)

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
		print(text)
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
    
    #print(m.position())
    #d = PixelAt(int(m.position()[0]), int(m.position()[1]))
    d = PixelAt(388, 626)
    #print(d)

    if d == 2503224:
    	print("Ahoy")

    	if(ft == 0):
    		ft = 1
    		k = screenshotocr(filename);
    		if k == "XXXX":
    			print("Valid call")
    			m.click(894, 1102)


    	#m.click(894, 1102) 
    else:
    	ft = 0

    sleep(0.5)
