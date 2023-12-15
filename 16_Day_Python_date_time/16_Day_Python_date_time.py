from datetime import datetime, timedelta

# Exercise 1: Get the current day, month, year, hour, minute, and timestamp
current_datetime = datetime.now()
current_day = current_datetime.day
current_month = current_datetime.month
current_year = current_datetime.year
current_hour = current_datetime.hour
current_minute = current_datetime.minute
current_timestamp = current_datetime.timestamp()

# Exercise 2: Format the current date
formatted_date = current_datetime.strftime("%m/%d/%Y, %H:%M:%S")

# Exercise 3: Change the time string to time
time_string = "5 December, 2019"
converted_time = datetime.strptime(time_string, "%d %B, %Y").time()

# Exercise 4: Calculate the time difference between now and New Year
new_year = datetime(current_year + 1, 1, 1)
time_until_new_year = new_year - current_datetime

# Exercise 5: Calculate the time difference between 1 January 1970 and now
epoch_start = datetime(1970, 1, 1)
time_since_epoch = current_datetime - epoch_start

# Displaying results
print(f"Current Date and Time: {current_datetime}")
print(f"Current Day: {current_day}, Month: {current_month}, Year: {current_year}")
print(f"Current Time: {current_hour}:{current_minute}")
print(f"Timestamp: {current_timestamp}")
print(f"Formatted Date: {formatted_date}")
print(f"Converted Time from String: {converted_time}")
print(f"Time Until New Year: {time_until_new_year}")
print(f"Time Since Epoch: {time_since_epoch}")

