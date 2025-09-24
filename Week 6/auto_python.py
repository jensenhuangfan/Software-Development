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
    EMAIL_URL = "sender"
    EMAIL_TO = "resipeint"
    SUBJECT = "subject"
    BODY = "my body is ready"
    jfk.moveTo(1250, 1051)
    time.sleep(.05)
    jfk.click
    jfk.moveTo(1250, 64)
    jfk.click(1250, 64)
    time.sleep(.05)
    jfk.sleep(.1)
    jfk.write(EMAIL_URL)
    time.sleep(1)
    jfk.press("enter")
    jfk.sleep(3)
    jfk.moveTo(157, 188)
    time.sleep(.05)
    jfk.click(157, 188)
    jfk.moveTo(1494, 469)
    time.sleep(.05)
    jfk.click(1494, 469)
    jfk.write(EMAIL_TO)
    jfk.moveTo(1284, 510)
    time.sleep(.05)
    jfk.click(1284, 510)
    jfk.write(SUBJECT)
    jfk.moveTo(1284, 832)
    time.sleep(.05)
    jfk.click(1284, 832)
    jfk.write(BODY)
    jfk.moveTo(1322, 999)
    time.sleep(.05)
    jfk.click(1322, 999)

send_email()