from progressbar import ProgressBar
pbar = ProgressBar()
a = ['b','c','d','e','f','g', 'h']
from time import sleep
for i in pbar(a):
    sleep(0.50)
    print(i, sep="")

'''EXERCISE:
Create a program that
- saves current time and prints it
- saves another time moment and prints it
- prints the time that has passed in between'''

