# Import common Python libraries
import random
import math
import datetime
import statistics
import matplotlib.pyplot as plt

# 1️⃣ Generate random numbers
numbers = [random.randint(1, 100) for _ in range(20)]

print("Random numbers:")
print(numbers)

# 2️⃣ Do some math
square_roots = [math.sqrt(num) for num in numbers]

print("\nSquare roots of numbers:")
print(square_roots)

# 3️⃣ Get current date/time
now = datetime.datetime.now()
print("\nCurrent date and time:")
print(now)

# 4️⃣ Use statistics
mean_value = statistics.mean(numbers)
median_value = statistics.median(numbers)
max_value = max(numbers)
min_value = min(numbers)

print("\nStatistics:")
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Max: {max_value}")
print(f"Min: {min_value}")

# 5️⃣ Create a chart with matplotlib
plt.hist(numbers, bins=10)
plt.title("Histogram of Random Numbers")
plt.xlabel("Number Range")
plt.ylabel("Frequency")

# Draw a vertical line for the mean
plt.axvline(mean_value)

plt.show()
