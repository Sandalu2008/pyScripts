import datetime

now =datetime.datetime.now()

formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted datetime: {formatted_date_time}")

formatted_date = now.strftime("%A, %B %d, %Y")
print(f"Formatted date: {formatted_date}")

formatted_time = now.strftime("%I:%M %p") # 12 -hour format with AM/PM
print(f"Formatted time: {formatted_time}")