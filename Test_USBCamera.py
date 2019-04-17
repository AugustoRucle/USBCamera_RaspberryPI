# Libraries 

import time 
import os 

# Main Code

os.system('fswebcam -r 1280x720 --no-banner /home/pi/Documents/Img/ByUSBCamera/img2.jpg') # uses Fswebcam to take picture

time.sleep(15) # this line creates a 15 second delay before repeating the loop
