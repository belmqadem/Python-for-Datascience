import time
from datetime import date

# Get the current time in seconds since January 1, 1970
current_time = time.time()

# Format the current time for display
formatted_time = "{:,.4f}".format(current_time)

# Print the formatted time in regular and scientific notations
print("Seconds since January 1, 1970:", formatted_time, "or {:.2e} in scientific notation".format(current_time))

# Print Current date
today = date.today()
print(today.strftime("%b %d %Y"))