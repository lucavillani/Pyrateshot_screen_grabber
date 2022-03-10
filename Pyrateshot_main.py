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

    print("Pyrashot has captured a screenshot \n")

    return(file_path)
    
def main():
    frequency = float(input("How frenquently you want Pyrateshot to capture a screenshot? [insert seconds] ---> "))
    schedule.every(frequency).seconds.do(take_screenshot)
    while True:
        schedule.run_pending()
        time.sleep(1)

print("\n WELCOME TO PYRATESHOT \n")

main()
