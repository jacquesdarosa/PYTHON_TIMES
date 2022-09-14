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
        mins = mins % 60
        print(timer = '{0}:{1}:{2}'.format(int(hours), int(mins), sec))
        '''print(timer, end="\r")'''
        time.sleep(1)
        t-= 1
t = int(input('enter the time in seconds here:'))
start_time = time.time
end_time =time.time

print('Start time:', start_time)
print('End_time:', end_time)
print('Countdown is finished')

