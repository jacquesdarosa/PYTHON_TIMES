from datetime import datetime, date

today = date.today()

# dd/mm/yy

current_datetime_1 = today.strftime('%d/%m/%Y')

print('current_date1:', current_datetime_1)


#Textual month, day and year	
current_datetime_2 = today.strftime("%B %d, %Y")
print("current_date2:", current_datetime_2)

# mm/dd/y
current_datetime_3 = today.strftime("%m/%d/%y")
print("current_date3:", current_datetime_3)

# Month abbreviation, day and year	
current_datetime_4 = today.strftime("%b-%d-%Y")
print("current_date4:", current_datetime_4)


current_datetime_year = today.year
print('current_year:', current_datetime_year)


