
from datetime import datetime
import time 

date = 'September 15, 2022 16:55:20'
now = datetime.now()
convert_date = datetime.strptime(date, '%B %d, %Y %H:%M:%S')
print(convert_date)
