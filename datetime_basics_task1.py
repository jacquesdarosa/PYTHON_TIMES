# Tasks

### Task 1

'''Using the variable called `current_datetime`, subtract 15 days from the current time.

- If today is 8/07/2021, your result should look like this:

Hint: use `.strtime()` method to reformat the time

2021-06-23'''


from datetime import datetime, timedelta

time_now = datetime.now() # using current time

print('initial date', str(time_now)) # print initial date

final_date = time_now + timedelta(days = -15)

print('Final time is:', final_date )

