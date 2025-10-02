def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.

    Args:
      price: The original price.
      discount_percent: The discount percentage.

    Returns:
      The final price after applying the discount, or the original price if the
      discount is less than 20%.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount)

    if final_price == original_price:
        print(f"No discount applied. The price is: ${final_price:.2f}")
    else:
        print(f"The final price after applying the discount is: ${final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter a valid number for the price and discount.")