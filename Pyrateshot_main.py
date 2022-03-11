from datetime import datetime
from PIL import ImageGrab
import time
import schedule

def take_screenshot():

    global screenshot_count

    image_timestamp = str(datetime.now().replace(microsecond=0))

    image_name = image_timestamp.replace(" ", "-").replace(":","-")

    screenshot = ImageGrab.grab()

    # DEFINE FOLDER FOR SAVING SCREENSHOTS
    file_path = f"C:/Users/lucvillani/Visual Studio Code/Python/Screenshots/{image_name}.png"

    screenshot.save(file_path)
    
    # SCREENSHOT COUNTER
    screenshot_count += 1

    print(f"Pyrashot has captured a screenshot. Running total: {screenshot_count} \n")

    return(file_path)
    
def main():
        
    # USER INPUT
    frequency = (input("How frenquently you want Pyrateshot to capture a screenshot? [hh:mm:ss] ---> "))

    print(f" \n Thank you - Pyrateshot will capture a screenshot every {frequency} hours \n")

    # TIME CONVERTER
    x = 0
    total_seconds = list()
    frequency_format = [3600, 60, 1]

    for t in frequency.split(":"):
        partial = frequency_format[0 + x] * int(t)
        x = x + 1
        total_seconds.append(partial)
    
    # MAIN FUNCTION
    schedule.every(sum(total_seconds)).seconds.do(take_screenshot)

    while True:
        schedule.run_pending()
        time.sleep(1)


print("\n WELCOME TO PYRATESHOT \n")

screenshot_count = 0

main()

