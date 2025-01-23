def supermarket():
    # Define product prices
    prices = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]
    total_sum = 0

    print("Supermarket")
    print("===========")

    while True:
        # Ask the user to select a product
        try:
            product_number = int(input("Please select product (1-10) 0 to Quit: ").strip())
            if product_number == 0:  # Quit condition
                break
            elif 1 <= product_number <= 10:
                product_price = prices[product_number - 1]
                total_sum += product_price
                print(f"Product: {product_number} Price: {product_price}")
            else:
                print("Invalid product number. Please select between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10 or 0 to quit.")

    # Display the total sum
    print(f"Total: {total_sum}")

    # Ask for payment and calculate change
    while True:
        try:
            payment = float(input("Payment: ").strip())
            if payment >= total_sum:
                change = payment - total_sum
                print(f"Change: {change:.2f}")
                break
            else:
                print(f"Insufficient payment. You still owe: {total_sum - payment:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid payment amount.")

if __name__ == "__main__":
    supermarket()
