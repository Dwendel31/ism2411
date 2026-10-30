
# Self-Assessment
# 1. The first bugs I noticed were syntax errors and incorrect
# variable assignments. AI helped me understand the problems.
# I learned that I should read tracebacks and use print statements
# to trace values and identify bugs before changing code.
#
# 2. apply_discount(price, tier) takes a price and a discount tier.
# It returns the price after the appropriate discount: 15% for gold,
# 10% for silver, 5% for bronze, or no discount for other tiers.
# A colleague can use it by passing a price and a tier.
#
# 3. AI disclosure: I used ChatGPT to help debug and correct my code.
# I reviewed the corrections to understand functions, loops, syntax,
# and variable scope.

# --- Exercise 1 ---

def calculate_tax(price, rate):
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")


# --- Exercise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")


# --- Exercise 3 ---

def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

discounted = apply_discount(200, "gold")
print(f"After gold discount: ${discounted:.2f}")

taxed_price = discounted + calculate_tax(discounted, 0.07)
print(f"After tax: ${taxed_price:.2f}")

print(
    f'final_price(200, "gold", 0.07) = '
    f'${final_price(200, "gold", 0.07):.2f}'
)


# --- Exercise 4 ---

orders = [
    (200, "gold"),
    (150, "silver"),
    (80, "bronze"),
    (500, "none")
]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f} | Tier: {tier} | Final: ${total:.2f}")


# --- Exercise 5 ---

# Bug 1 fixed: += adds each sale to the running total.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

# Bug 2 fixed: Added the missing colon after the for statement.
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

# Bug 3 fixed: < prevents accessing an index outside the list.
i = 0
while i < len(sales):
    print(sales[i])
    i += 1


# --- Exercise 6 ---

x = 100  # Global variable

def double_it():
    x = 999  # Local variable, separate from global x
    return x * 2

# Scope explanation:
# A local variable is defined inside a function and is separate
# from a global variable with the same name. double_it() uses its
# local x, so the global x remains 100.

print(x)
print(double_it())
print(x)