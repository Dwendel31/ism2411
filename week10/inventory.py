# Reflection:
# 1. The most surprising thing about lists is that you can change them after creating them.
# I expected them to stay the same, but you can add, remove, and rearrange items.
#
# 2. At my job, a Python list could have saved time keeping track of inventory or customer orders.
# Instead of manually organizing everything in Excel, Python could automatically sort and filter the information.

# Exercise 1: Build a List

print("--- Exercise 1: Build a List ---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))


# Exercise 2: Index Practice

print("--- Exercise 2: Index Practice ---")

print(inventory[0])
print(inventory[-1])

middle = len(inventory) // 2
print(inventory[middle])


# Exercise 3: List Slicing

print("--- Exercise 3: List Slicing ---")

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])


# Exercise 4: List Methods

print("--- Exercise 4: List Methods ---")

inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)


# Exercise 5: Tuple Comparison

print("--- Exercise 5: Tuple Comparison ---")

coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates from being changed by accident")

print(coords)


# Exercise 6: Average Sales

print("--- Exercise 6: Average Sales ---")

sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count

print(f"Total sales: {total}")
print(f"Number of sales: {count}")
print(f"Average sales: {average}")
print(f"Best Sale: {max(sales)}")
print(f"Worst Sale: {min(sales)}")

best = sales[0]
worst = sales[0]

for sale in sales:
    if sale > best:
        best = sale
    if sale < worst:
        worst = sale

print(f"Best Sale (loop): {best}")
print(f"Worst Sale (loop): {worst}")


# Exercise 7: Accumulator Pattern

print("--- Exercise 7: Accumulator Pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []

for price in prices:
    discounted.append(round(price * 0.9, 2))

print(prices)
print(discounted)


# Exercise 8: Filter Above Threshold

print("--- Exercise 8: Filter Above Threshold ---")

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales)/len(high_sales)}")