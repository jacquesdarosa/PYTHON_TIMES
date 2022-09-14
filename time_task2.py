import time

def time_convert(sec):
    mins = sec//60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print('Start_time ={0}:{1}:{2}'.format(int(hours), int(mins), sec), start_time)
    print('End_time ={0}:{1}:{2}'.format(int(hours), int(mins), sec), end_time)
    print('Time lapsed = {0}:{1}:{2}'.format(int(hours), int(mins), sec))

input('Press enter to start')
start_time = time.time()

input('Press enter to stop')
end_time = time.time()

time_lapsed = end_time - start_time
time_convert(time_lapsed)





'''EXERCISE:
Create a program that
- saves current time and prints it
- saves another time moment and prints it
- prints the time that has passed in between'''


   