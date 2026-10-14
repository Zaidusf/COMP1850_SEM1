# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

numbers = read_numbers()

if len(numbers) == 0:
    print("Error: no numbers provided", file=sys.stderr)
    sys.exit(1)

minimum = min(numbers)
maximum = max(numbers)
mean = sum(numbers) / len(numbers)

sorted_numbers = sorted(numbers)
middle = len(sorted_numbers) // 2

if len(sorted_numbers) % 2 == 1:
    median = sorted_numbers[middle]
else:
    median = (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2

print(f"Minimum = {minimum}")
print(f"Maximum = {maximum}")
print(f"Mean = {mean}")
print(f"Median = {median}")