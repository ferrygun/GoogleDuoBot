from time import sleep
from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()

m.click(870,348) # Click in the Duo text box
sleep(0.5)
#k.tap_key('Delete',n=6,interval=0.05) # Delete existing characters
k.press_key( k.control_key )
k.tap_key("a")
k.release_key ( k.control_key )
sleep(0.5)
k.tap_key('Delete',n=6,interval=0.05)

k.type_string("AAAA") # Type name of Duo contact
sleep(0.2)
k.tap_key('Return') # Hit Return to select contact
sleep(1.5)
m.click(874,854) # Click on Video Call button
