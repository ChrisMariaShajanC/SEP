from datetime import datetime
# Get the current date
now=datetime.now()
# Format the current date as a string   
formatted=now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)
# Print the formatted date