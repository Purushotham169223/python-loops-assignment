import numpy as np
import time

# =========================
# Task 1: Temperature Data
# =========================

# Create NumPy array
temps_celsius = np.array([22, 25, 28, 24, 26])

# Convert to Fahrenheit
temps_fahrenheit = temps_celsius * 1.8 + 32

# Calculate average Fahrenheit temperature
avg_fahrenheit = round(np.mean(temps_fahrenheit), 1)

# Print results
print("Celsius:", temps_celsius)
print("Fahrenheit:", temps_fahrenheit)
print("Average Fahrenheit:", avg_fahrenheit)

print("\n" + "="*40 + "\n")

# =========================
# Task 2: Array Shape & Statistics
# =========================

scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])

print("Shape:", scores.shape)
print("Total elements:", scores.size)

highest = np.max(scores)
lowest = np.min(scores)
score_range = highest - lowest

print("Highest score:", highest)
print("Lowest score:", lowest)
print("Range:", score_range)

print("\n" + "="*40 + "\n")

# =========================
# Task 3: Performance Comparison
# =========================

# Create data
numpy_array = np.arange(1, 50001)
python_list = list(range(1, 50001))

# NumPy sum timing
start_numpy = time.time()
numpy_sum = np.sum(numpy_array)
end_numpy = time.time()

# Python sum timing
start_python = time.time()
python_sum = sum(python_list)
end_python = time.time()

numpy_time = end_numpy - start_numpy
python_time = end_python - start_python

# Speed comparison
speed_factor = python_time / numpy_time

# Print results
print("NumPy sum:", numpy_sum)
print("Python sum:", python_sum)
print(f"NumPy time: {numpy_time:.4f} seconds")
print(f"Python time: {python_time:.4f} seconds")
print(f"NumPy is {speed_factor:.1f}x faster")