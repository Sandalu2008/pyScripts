import datetime

now =datetime.datetime.now()

# Add 7 days
future_date = now + datetime.timedelta(days=7)
print(f"7 days from now: {future_date}")

# Substract 3 hours
past_time = now - datetime.timedelta(hours=3)
print(f"3 hours ago : {past_time}")

# Calculate the difference between two datetimes
date1 = datetime.datetime(2024, 1, 1)
date2 = datetime.datetime(2024, 7, 24)
difference = date2 - date1
print(f"Difference between dates: {difference}")
print(f"Difference in days :{difference.days}")
