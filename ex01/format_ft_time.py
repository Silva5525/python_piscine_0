
# Import the 'time' module to access time-related functions.
import time

# Import the 'datetime' class from the 'datetime' module to handle date and time.
from datetime import datetime

# 'time.time()' calls the 'time()' function from the time module.
# It returns the current time in seconds since January 1, 1970 (called the Unix epoch).
# This value is a floating-point number, useful for precise time calculations.
epoch_time = time.time()

# Print the number of seconds since the Unix epoch.
# Display it both as a standard float and in scientific notation.
# The f before the string creates an "f-string", which allows embedding variables and expressions
# - directly inside the string using curly braces {}. It's a simple way to format output.
# :, — tells Python to format the number with commas (e.g., 1,000,000)
# .4f — shows 4 digits after the decimal point
# .2e — formats the number in scientific notation with 2 digits after the decimal
print(f"Seconds since January 1, 1970: {epoch_time:,.4f} or {epoch_time:.2e} in scientific notation")

# 'datetime.now()' gets the current local date and time with .now() as a datetime object
# - from the datetime module 
# '.strftime("%b %d %y")' formats that datetime into a string:
#   %b = abbreviated month name (e.g., Jul)
#   %d = day of the month (e.g., 07)
#   %Y = last two digits with y or Y for the exakt year (e.g., 2025)
formatted_date = datetime.now().strftime("%b %d %Y")

# Print the formatted date.
print(formatted_date)

# USAGE:
# python3 format_ft_time.py | cat -e
