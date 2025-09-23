import pyautogui as jfk

#print(jfk.position)
#jfk.click(100, 20)

import time, sys

jfk.FAILSAFE = True # Fling mouse to top left to abort
print("Move the mouse to the left or press Ctrl C to abort")

def pointer_location():
    try:
        while True:
            x, y = jfk.position()
            sys.stdout.write(f"\r(x, y) = ({x:4d}, {y:4f})")
            sys.stdout.flush()
            time.sleep(0.05) # 20 updates per second

    except KeyboardInterrupt:
        print("\nDone")
# while True:
#     jfk.click(840,620)
#     time.sleep(.005)

# pointer_location()

def send_email():
    EMAIL_URL = "https://mail.google.com"
    EMAIL_TO = "michael.sekol@mahoningctc.com"
    SUBJECT = "Hi"
    BODY = "hi"
    jfk.moveTo(1250, 1051)
    time.sleep(.05)
    jfk.click
    jfk.moveTo(1250, 64)
    time.sleep(.05)
    jfk.click
    jfk.click
    jfk.click
    jfk.sleep(.1)
    jfk.write(EMAIL_URL)
    time.sleep(1)
    jfk.press("enter")
    jfk.sleep(3)
    jfk.moveTo(1120, 620)
    time.sleep(.05)
    jfk.click

send_email()