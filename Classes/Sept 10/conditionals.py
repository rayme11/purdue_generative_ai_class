
# To-do Tasks:
# 1.
# Discount rules for retail customer
# 1. 10% discount for orders over $100 if the customer is a member. Hint: if is_member == True and order_amount > 100
# 2. 5% discount for orders over $50 if the customer is a member. Hint: if is_member == True and order_amount > 50
# 3. No discount for orders under $50 if the customer is a member. Hint: if is_member == True and order_amount < 50
# 4. 5% discount for orders over $100 if the customer is not a member. Hint: if is_member == False and order_amount > 100

is_member = input("Are you a member? (yes/no): ").strip().lower() == "yes"
order_amount = float(input("Enter the order amount: "))

if is_member:
    if order_amount > 100:
        discount = 0.10
    elif order_amount > 50:
        discount = 0.05
    else:
        discount = 0
else:
    if order_amount > 100:
        discount = 0.05
    else:
        discount = 0

final_price = order_amount * (1 - discount)
print(f"Final price after discount: ${final_price:.2f}")
