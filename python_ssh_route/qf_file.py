# Combining the code to create a file with the current timestamp and write the date 5 days ago into it

from datetime import datetime, timedelta

# Current date and time
now = datetime.now()

# Format the date and time for the filename
filename = now.strftime("%Y-%m-%d_%H-%M-%S.txt")

# Calculate the date and time for 5 days ago
five_days_ago = now - timedelta(days=5)

# Format the date and time as specified for writing into the file
formatted_date_time = five_days_ago.strftime("%Y-%m-%d %H:%M:%S.%f")

# Create the file and write the formatted date and time into it
with open(filename, 'w') as file:
    file.write(formatted_date_time)





