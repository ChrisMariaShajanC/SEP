from datetime import datetime,timedelta
# Get the current date and time
today=datetime.now()
# Get the date 7 days ago
ten_days_ago=today- timedelta(days=10)
three_hours_later=today+timedelta(hours=3)
# Print the results
print("10 days ago:", ten_days_ago.strftime("%d-%m-%Y"))
print("3 hours later:", three_hours_later.strftime(" %H:%M"))