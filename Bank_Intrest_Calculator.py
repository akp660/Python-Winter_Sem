#14/02/24
#Calculate interest rate based on type deposit
#if saving intrest rate will be 4%
#


def calculate_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

def main():
    print("Welcome to the interest rate calculator!")

    # Taking input from the user
    principal = float(input("Enter the principal amount: "))
    rate = 0.0  # initializing rate variable

    account_type = input("Enter the account type (Savings/Current/Another): ").lower()

    # Adjusting interest rate based on account type
    if account_type == "savings":
        rate = 5.0  # Adjust the rate for savings account
    elif account_type == "current":
        rate = 2.5  # Adjust the rate for current account
    elif account_type == "another":
        rate = 7.0  # Adjust the rate for another account
    else:
        print("Invalid account type entered.")
        return

    time = float(input("Enter the time period (in years): "))

    # Calculating interest based on the selected account type
    interest = calculate_interest(principal, rate, time)

    # Displaying result
    print("\nInterest calculated for {} Account: {:.2f}".format(account_type.capitalize(), interest))

if __name__ == "__main__":
    main()
