# ==============================================================================
# SELF-ASSESSMENT & REFLECTION
# ==============================================================================
"""
Reflection Questions:

1. What is the most surprising thing about how lists work in Python compared to what you expected coming in?
- It is surprising that lists are mutable and support dynamic methods like append and remove seamlessly. Coming from static data structures, the flexibility of modifying elements in place without manual resizing is very efficient.

2. Describe one real business situation from a job you've had, an internship, or a class where a Python list would have saved you time compared to doing it manually in Excel.
- When tracking daily retail sales across multiple store locations, manually calculating totals, averages, and filtering high-performing days in Excel can lead to formula errors and tedious manual sorting. A Python list combined with built-in functions like sum() and list comprehensions automates the entire analytical workflow instantly.
"""

# --- Exercise 1 ---
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

print("-" * 30)

# --- Exercise 2 ---
print(inventory[0])
print(inventory[-1])
middle_index = len(inventory) // 2
print(inventory[middle_index])

print("-" * 30)

# --- Exercise 3 ---
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

print("-" * 30)

# --- Exercise 4 ---
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

print("-" * 30)

# --- Exercise 5 ---
coords = (40.7128, 74.0060)
try:
    coords[0] = 99
except TypeError:
    print("TypeError caught: Tuples are immutable and cannot be modified.")
print("Tuples are useful for fixed coordinates to ensure data integrity.")
print(coords)

print("-" * 30)

# --- Exercise 6 ---
sales = [100, 250, 75, 480, 200]
total_sales = sum(sales)
count_sales = len(sales)
avg_sales = total_sales / count_sales
best_day = max(sales)
worst_day = min(sales)

print(f"Total: {total_sales} | Average: {avg_sales} | Best: {best_day} | Worst: {worst_day}")

print("-" * 30)

# --- Exercise 7 ---
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for p in prices:
    discounted.append(round(p * 0.90, 2))
print("Original:", prices)
print("Discounted:", discounted)

print("-" * 30)

# --- Exercise 8 ---
raw_sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for s in raw_sales:
    if s > 300:
            high_sales.append(s)

avg_high = sum(high_sales) / len(high_sales)
print(high_sales)
print(f"Count: {len(high_sales)} Avg: ~{avg_high:.2f}")