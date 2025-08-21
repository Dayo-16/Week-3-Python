def calculate_discount(price, discount_percent):
    """
    Return the final price after applying a discount only if discount_percent >= 20.
    Otherwise, return the original price unchanged.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt the user for input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Print result
if discount_percent >= 20:
    print(f"Discount applied! The final price is: {final_price}")
else:
    print(f"No discount applied. The price remains: {final_price}")


