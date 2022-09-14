'''EXERCISE:
Create a program that
- takes an  int as input
- uses this int as a countdown
- visibly counts down
- prints begin time, end time and countdown int'''

import time
def countdown(t):

 while t: # while t > 0 for clarity 
        mins = t//60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
t = int(input('enter the time in seconds here:'))
start_time = time.time
end_time =time.time
countdown(int(t))

print('Countdown is finished')

