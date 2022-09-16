from datetime import datetime, date 

# get current date
today = datetime.now().date()
# get weekday
print(f"{today.strftime('week = %w day_week = %A'):}")

