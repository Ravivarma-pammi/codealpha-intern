# Hardcoded stock prices dictionary
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

# Store user portfolio
portfolio = {}

# Get user input
print("Enter your stock portfolio. Type 'done' to finish.")

while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found in price list. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = quantity
    except ValueError:
        print("Please enter a valid number.")

# Calculate total investment
total_value = 0
print("\n--- Portfolio Summary ---")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_value += value
    print(f"{stock}: {quantity} shares × ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_value}")

# Optional: Save to file
save_option = input("Do you want to save this to a file? (yes/no): ").lower()
if save_option == 'yes':
    filename = input("Enter filename (with .txt or .csv): ")
    with open(filename, 'w') as f:
        f.write("Stock,Quantity,Price,Total\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            total = price * quantity
            f.write(f"{stock},{quantity},{price},{total}\n")
        f.write(f"\nTotal Investment Value: ${total_value}\n")
    print(f"Portfolio saved to {filename}")
