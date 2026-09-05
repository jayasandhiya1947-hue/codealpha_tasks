import csv
from datetime import datetime

# Stock prices (sample prices for the project)
stocks = {
    "AAPL": 227.16,
    "MSFT": 506.69,
    "GOOGL": 211.45,
    "AMZN": 231.48,
    "TSLA": 333.87,
    "NVDA": 174.18,
    "META": 521.88
}

portfolio = {}


def display_stocks():
    print("\n" + "=" * 55)
    print("              AVAILABLE STOCKS")
    print("=" * 55)
    print(f"{'Symbol':<10}{'Company':<20}{'Price ($)':>15}")
    print("-" * 55)

    company_names = {
        "AAPL": "Apple Inc.",
        "MSFT": "Microsoft",
        "GOOGL": "Alphabet",
        "AMZN": "Amazon",
        "TSLA": "Tesla",
        "NVDA": "NVIDIA",
        "META": "Meta Platforms"
    }

    for symbol, price in stocks.items():
        print(f"{symbol:<10}{company_names[symbol]:<20}{price:>15.2f}")


def add_stock():
    display_stocks()

    symbol = input("\nEnter stock symbol: ").upper()

    if symbol not in stocks:
        print("❌ Invalid stock symbol.")
        return

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("❌ Quantity must be greater than zero.")
            return

        if symbol in portfolio:
            portfolio[symbol] += quantity
        else:
            portfolio[symbol] = quantity

        investment = stocks[symbol] * quantity

        print("\n✅ Stock added successfully!")
        print(f"Stock      : {symbol}")
        print(f"Quantity   : {quantity}")
        print(f"Price      : ${stocks[symbol]:.2f}")
        print(f"Investment : ${investment:.2f}")

    except ValueError:
        print("❌ Please enter a valid quantity.")


def display_portfolio():
    if not portfolio:
        print("\n⚠️ Your portfolio is empty.")
        return

    print("\n" + "=" * 75)
    print("                    MY STOCK PORTFOLIO")
    print("=" * 75)

    print(f"{'Stock':<10}{'Quantity':<12}{'Price':<15}"
          f"{'Investment':<18}{'Current Value':<15}")

    print("-" * 75)

    total_investment = 0
    current_value = 0

    for symbol, quantity in portfolio.items():

        purchase_price = stocks[symbol]

        # Simulated current price for demonstration
        current_price = purchase_price * 1.08

        investment = purchase_price * quantity
        value = current_price * quantity

        total_investment += investment
        current_value += value

        print(
            f"{symbol:<10}"
            f"{quantity:<12}"
            f"${purchase_price:<14.2f}"
            f"${investment:<17.2f}"
            f"${value:<14.2f}"
        )

    profit = current_value - total_investment

    print("-" * 75)
    print(f"Total Investment : ${total_investment:.2f}")
    print(f"Current Value    : ${current_value:.2f}")
    print(f"Profit/Loss      : ${profit:.2f}")

    if profit > 0:
        print("Status           : 📈 PROFIT")
    elif profit < 0:
        print("Status           : 📉 LOSS")
    else:
        print("Status           : ➖ NO PROFIT/LOSS")

    print("=" * 75)


def save_portfolio():
    if not portfolio:
        print("\n⚠️ Nothing to save.")
        return

    filename = "portfolio_report.csv"

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Stock",
            "Quantity",
            "Price",
            "Investment"
        ])

        for symbol, quantity in portfolio.items():

            investment = stocks[symbol] * quantity

            writer.writerow([
                symbol,
                quantity,
                f"{stocks[symbol]:.2f}",
                f"{investment:.2f}"
            ])

    print(f"\n✅ Portfolio saved successfully to {filename}")


def main():

    print("\n" + "=" * 55)
    print("        STOCK PORTFOLIO TRACKER")
    print("=" * 55)

    date_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")

    print("Date & Time:", date_time)

    while True:

        print("\n------------ MENU ------------")
        print("1. View Available Stocks")
        print("2. Add Stock")
        print("3. View Portfolio")
        print("4. Save Portfolio")
        print("5. Exit")
        print("------------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_stocks()

        elif choice == "2":
            add_stock()

        elif choice == "3":
            display_portfolio()

        elif choice == "4":
            save_portfolio()

        elif choice == "5":
            print("\nThank you for using Stock Portfolio Tracker!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


main()