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
    rate = float(input("Enter the annual interest rate (in percentage): "))
    time = float(input("Enter the time period (in years): "))

    # Calculating interest for different account types
    savings_interest = calculate_interest(principal, rate, time)
    current_interest = calculate_interest(principal, rate * 0.5, time)  # Assuming current account interest is half of the given rate
    another_interest = calculate_interest(principal, rate * 1.5, time)  # Assuming another account interest is 1.5 times the given rate

    # Displaying results
    print("\nInterest calculated for different account types:")
    print("Savings Account: ${:.2f}".format(savings_interest))
    print("Current Account: ${:.2f}".format(current_interest))
    print("Another Account: ${:.2f}".format(another_interest))

if __name__ == "__main__":
    main()
