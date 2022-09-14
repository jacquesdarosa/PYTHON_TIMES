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

"""Peers's solution: import os       # import os
import time     # import time
​
os.system("clear")  # clear terminal
​
print("Yeah, some funky download ...")  # print the heck out of things!
n=4
for i in range(0, 101, n):                      # start loop
    line = ("-" * ((100//n) - (i//n)))          # create ----- line 100 - "#" times
    bar = "#" * (i//n)                          # create ##### line "#" * i times
    
    fullbar = "|" +bar+line  + "| " + str(i) + "%"      # build progress bar
    print(fullbar + "\r", end="")                       # print progress bar
    time.sleep(0.1)                                     # sleep for 0,1 seconds
​
print("done!" + " " * 50)                               # print done" 
"""