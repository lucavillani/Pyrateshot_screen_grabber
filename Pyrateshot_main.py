from datetime import datetime
from PIL import ImageGrab
import time
import schedule

def take_screenshot():

    print("Pyrateshot is taking a screenshot... \n")

    image_timestamp = str(datetime.now().replace(microsecond=0))

    image_name = image_timestamp.replace(" ", "-").replace(":","-")

    screenshot = ImageGrab.grab()

    file_path = f"C:/Users/lucvillani/Visual Studio Code/Python/Screenshots/{image_name}.png"

    screenshot.save(file_path)

    return(file_path)
    
print("\n WELCOME TO PYRATESHOT \n")

take_screenshot()

print("\n Pyrashot has saved a screenshot \n")

quit()