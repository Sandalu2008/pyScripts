import datetime

now = datetime.datetime.now()

print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")
print(f"Hour: {now.hour}")
print(f"Minute: {now.minute}")
print(f"Second: {now.second}")
print(f"Microsecond: {now.microsecond}")
print(f"Weekday: (Monday=0, Sunday=6: {now.weekday()}")