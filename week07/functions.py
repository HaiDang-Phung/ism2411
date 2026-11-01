# ==============================================================================
# SELF-ASSESSMENT & DISCLOSURE
# ==============================================================================
"""
Self-Assessment Questions:

1. In Exercise 5 (Debug First, Then Ask), what was the first bug you spotted?
   - The first bug spotted was a NameError caused by a misspelled variable name.
   - It was identified directly from the Python traceback line number.
   - This shows that reading error tracebacks carefully is the most efficient 
     first instinct when debugging syntax or scope issues.

2. Explain apply_discount(price, tier) in plain English:
   - Function Purpose: Calculates the reduced price of an item based on a 
     customer's membership status tier.
   - Inputs: 
     * price (float or int): The original price before discount.
     * tier (str): Membership level ('gold', 'silver', 'bronze', or 'none').
   - Output: Returns a float representing the price after applying the tier percentage.
   - Documentation Quality: Yes, a colleague can use it seamlessly via its 
     Google-style docstring without needing to inspect the implementation logic.

3. AI Disclosure:
   - Disclosure: AI was used as a thought partner to structure solutions, 
     generate tests, and refine explanatory docstrings.
   - Reflection: The AI helped deepen my understanding of modular function 
     design and scope behavior rather than taking shortcuts.
"""
# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate
print("--- Exercise 1 ---")
tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)
print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")
print()

# --- Exercise 2 ---
def apply_discount(price, tier):
    tier_lower = tier.lower()
    if tier_lower == "gold":
        discount_rate = 0.15
    elif tier_lower == "silver":
        discount_rate = 0.10
    elif tier_lower == "bronze":
        discount_rate = 0.05
    else:
        discount_rate = 0.0
    return price * (1 - discount_rate)
print("--- Exercise 2 ---")
base_price = 200
print(f"gold:   ${apply_discount(base_price, 'gold'):.2f}")
print(f"silver: ${apply_discount(base_price, 'silver'):.2f}")
print(f"bronze: ${apply_discount(base_price, 'bronze'):.2f}")
print(f"none:   ${apply_discount(base_price, 'none'):.2f}")
print()

# --- Exercise 3 ---
def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax
print("--- Exercise 3 ---")
gold_discounted = apply_discount(200, "gold")
after_tax_manual = gold_discounted + calculate_tax(gold_discounted, 0.07)
print(f"After gold discount: ${gold_discounted:.2f}")
print(f"After tax: ${after_tax_manual:.2f}")
calc_final = final_price(200, "gold", 0.07)
print(f'final_price(200, "gold", 0.07) = ${calc_final:.2f}')
print()

# --- Exercise 4 ---
print("--- Exercise 4 ---")
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier:<6} | Final: ${total:.2f}")
print()

# --- Exercise 5 ---
print("--- Exercise 5 ---")
def fixed_sales_processor(orders_list, tax_rate=0.07):
    report = []
    for item_price, item_tier in orders_list:
        total_cost = final_price(item_price, item_tier, tax_rate)
        report.append(
            f"Item (${item_price}, {item_tier}) -> Total: ${total_cost:.2f}"
        )
    return report
sample_orders = [(100, "GOLD"), (250, "Silver")]
for line in fixed_sales_processor(sample_orders):
    print(line)
print()

# --- Exercise 6 ---
print("--- Exercise 6 ---")
x = 100  # Global variable
def double_it():
    x = 999  # Local variable
    return x * 2
# Scope Explanation:
# Defining 'x = 999' inside double_it() creates a local variable 'x' inside the function scope.
# It does not change the global variable 'x' defined outside the function.
print(x)
print(double_it())
print(x)