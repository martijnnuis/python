import sys
import time

def slowtext(msg):
    for char in msg:
        print(char, end='', flush=True)

        time.sleep(.2)
slowtext("hallo luitjes")