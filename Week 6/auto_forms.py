import pyautogui as j

#print(jfk.position)
#jfk.click(100, 20)

import time, sys

j.FAILSAFE = True # Fling mouse to top left to abort
print("Move the mouse to the left or press Ctrl C to abort")

def pointer_location():
    try:
        while True:
            j.click(2176,996)
            j.click(2187,1169)
            time.sleep(.2)
            j.click(2263,242)

    except KeyboardInterrupt:
        print("\nDone")

pointer_location()


#             x, y = j.position()
#             sys.stdout.write(f"\r(x, y) = ({x:4d}, {y:4f})")
#             sys.stdout.flush()
#             time.sleep(0.05) # 20 updates per second