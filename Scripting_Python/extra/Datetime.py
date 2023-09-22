from datetime import datetime, timedelta

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Start Time =", current_time)

now2 = datetime.now()

print(now2 - now)