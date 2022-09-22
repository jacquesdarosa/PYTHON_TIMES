### Task 2

'''Using the variable called `current_datetime`, add 7 days to your current day.

- Your result should look like this, if today is 8/07/2021:

2021-07-15 '''

from datetime import datetime, timedelta

time_now = datetime.now() # using current time

print('initial date', str(time_now)) # print initial date

final_date = time_now + timedelta(days = +7)

print('Final time is:', final_date )


