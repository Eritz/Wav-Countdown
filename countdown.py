#! python3
# This program begins a countdown starting at a specified time
# Once the timer is complete, it will open the media player and play a specified .wav file

import time, subprocess, wave, contextlib
import os, msvcrt

print('This program starts a countdown at a specified time')
print('Press CTRL-C to exit')
print()

#Put inside the quotations below
media_exe = r'PATH TO YOUR MEDIA PLAYER HERE'
alarm = r'PATH TO YOUR .wav FILE HERE'

# User inputs the time
while True:
    try:
        timeLeft1 = int(input('How many seconds do you want to countdown from? '))
        print()
        # Set the variables
        timeLeft2 = timeLeft1
        # Read the length of the wav file
        with contextlib.closing(wave.open(alarm, 'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
            
        # The main program
        while True:
            try:
                print()
                print('Press ENTER to start the countdown.')
                input()
                while timeLeft2 > 0:
                    print('Time left: ', timeLeft2)
                    time.sleep(1)
                    timeLeft2 -= 1   
            # Opens the alarm
                subprocess.Popen([media_exe, alarm], shell = True)
                time.sleep(duration+1)
                timeLeft2 = timeLeft1
                #Edit the 'CHANGETHISWORD' into your mediaplayer's .exe below, e.g "foobar2000.exe"
                os.system('TASKKILL /F /IM CHANGETHISWORD')
                
            except KeyboardInterrupt:
                print('\nDone.')
                print()
                break
    except ValueError:
        print('Error! Please enter an integer value.')
        print()