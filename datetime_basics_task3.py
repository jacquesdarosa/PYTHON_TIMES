### Task 3

'''Your task is to determine when rent is due for a customer, we shall make assumption that tenant always pays 25 days from the first day of a month. 
Create a string that stores a message to a customer called Friedrich, print out the message to the terminal.

Start by creating a datetime instance with 25 January, 2021.

`start_date = datetime(year=2020, month=1, day=1)`

- Your result should look like this:

```
Hello Friedrich, your rent of 300 € is due on 25 January, 2021.'''

# I will change the dates: my choice

from datetime import datetime, date, timedelta

# today = date.today()

start_date = date(year=2022, month= 10, day=1)

Pay_by = start_date + timedelta(days = +29)

print('Hello Joseph, your rent of 1000 €  is due on:' + str(Pay_by))

