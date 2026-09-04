"""
Mini Project: Simple ATM Simulator
------------------------------------
Complete each function below (replace the `pass` with your code).
Do NOT change the function names or parameters - the main program
depends on them.
"""


def check_balance(balance):
    """
    Display the current balance to the user.

    Parameters:
        balance (float): the current account balance

    Returns:
        None
    """
    # TODO: print a friendly message showing the balance
    pass


def deposit(balance, amount):
    """
    Add money to the balance.

    Parameters:
        balance (float): the current account balance
        amount (float): the amount to deposit

    Returns:
        float: the updated balance
    """
    # TODO: check that amount > 0
    # TODO: if valid, add amount to balance
    # TODO: if invalid, print an error and return balance unchanged
    pass


def withdraw(balance, amount):
    """
    Remove money from the balance.

    Parameters:
        balance (float): the current account balance
        amount (float): the amount to withdraw

    Returns:
        float: the updated balance
    """
    # TODO: check that amount > 0 and amount <= balance
    # TODO: if valid, subtract amount from balance
    # TODO: if invalid (insufficient funds), print an error and return balance unchanged
    pass


# ------------------- BONUS (optional) -------------------
def pin_check(correct_pin, entered_pin):
    """
    Check whether the entered PIN matches the correct PIN.

    Parameters:
        correct_pin (str): the actual PIN
        entered_pin (str): the PIN entered by the user

    Returns:
        bool: True if match, False otherwise
    """
    # TODO: compare correct_pin and entered_pin
    pass


# ------------------- MAIN PROGRAM -------------------
def main():
    balance = 1000.00

    print("=== Welcome to the Simple ATM ===")

    while True:
        print("\nWhat would you like to do?")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            check_balance(balance)

        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            balance = deposit(balance, amount)

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            balance = withdraw(balance, amount)

        elif choice == "4":
            print("Thank you for banking with us. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
