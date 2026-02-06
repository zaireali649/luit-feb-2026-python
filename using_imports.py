# Import common Python libraries
import random                     # Used to generate random numbers
import math                       # Provides math functions like square root
import datetime                   # Lets us work with dates and times
import statistics                 # Helps calculate stats like mean and median
import matplotlib.pyplot as plt   # Used to create charts and graphs

# 1️⃣ Generate random numbers
# Create a list of 20 random integers between 1 and 100
numbers = [random.randint(1, 100) for _ in range(20)]

print("Random numbers:")
print(numbers)  # Print the list of random numbers

# 2️⃣ Do some math
# Create a new list containing the square root of each number
square_roots = [math.sqrt(num) for num in numbers]

print("\nSquare roots of numbers:")
print(square_roots)  # Print the square root results

# 3️⃣ Get current date/time
# Get the current date and time from the computer
now = datetime.datetime.now()

print("\nCurrent date and time:")
print(now)  # Print the current date/time

# 4️⃣ Use statistics
# Calculate useful statistics from our random number list
mean_value = statistics.mean(numbers)     # Average value
median_value = statistics.median(numbers) # Middle value when sorted
max_value = max(numbers)                  # Largest number
min_value = min(numbers)                  # Smallest number

print("\nStatistics:")
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Max: {max_value}")
print(f"Min: {min_value}")

# 5️⃣ Create a chart with matplotlib
# Create a histogram (bar chart showing distribution of values)
plt.hist(numbers, bins=10)  # Split numbers into 10 buckets

# Add labels and title to make the chart readable
plt.title("Histogram of Random Numbers")
plt.xlabel("Number Range")
plt.ylabel("Frequency")

# Draw a vertical line showing the mean (average) value
plt.axvline(mean_value)

# Display the chart on screen
plt.show()
