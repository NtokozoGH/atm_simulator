"""
Mini Project: Simple ATM Simulator
------------------------------------
Complete each function below.
Do NOT change the function names or parameters.
"""


def check_balance(balance):
    """
    Display the current balance to the user.

    Parameters:
        balance (float): the current account balance

    Returns:
        None
    """
    print(f"Your current balance is: R{balance:.2f}")


def deposit(balance, amount):
    """
    Add money to the balance.

    Parameters:
        balance (float): the current account balance
        amount (float): the amount to deposit

    Returns:
        float: the updated balance
    """

    if amount > 0:
        balance += amount
        print(f"Successfully deposited R{amount:.2f}.")
        print(f"New balance: R{balance:.2f}")

    else:
        print("Invalid deposit amount. Please enter a positive value.")

    return balance


def withdraw(balance, amount):
    """
    Remove money from the balance.

    Parameters:
        balance (float): the current account balance
        amount (float): the amount to withdraw

    Returns:
        float: the updated balance
    """

    if amount <= 0:
        print("Invalid withdrawal amount. Please enter a positive value.")

    elif amount > balance:
        print("Insufficient funds.")

    else:
        balance -= amount
        print(f"Successfully withdrew R{amount:.2f}.")
        print(f"Remaining balance: R{balance:.2f}")

    return balance


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

    return correct_pin == entered_pin


def get_10_digits():
    """
    Ask the user to enter exactly 10 digits.

    The number must:
    - Contain exactly 10 characters
    - Contain numbers only
    - Not contain letters or other characters
    """

    while True:
        number = input("Enter cellphone number (10 digits): ")

        if number.isdigit() and len(number) == 10:
            return number

        print("Invalid input. Please enter exactly 10 digits.")


# ------------------- MAIN PROGRAM -------------------

def main():

    balance = 1000.00

    print("=== Welcome to the Simple ATM ===")

    while True:

        print("\nWhat would you like to do?")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Send money")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")


        # ---------------- OPTION 1 ----------------

        if choice == "1":

            check_balance(balance)


        # ---------------- OPTION 2 ----------------

        elif choice == "2":

            try:
                amount = float(input("Enter amount to deposit: R"))
                balance = deposit(balance, amount)

            except ValueError:
                print("Invalid input. Please enter a number.")


        # ---------------- OPTION 3 ----------------

        elif choice == "3":

            try:
                amount = float(input("Enter amount to withdraw: R"))
                balance = withdraw(balance, amount)

            except ValueError:
                print("Invalid input. Please enter a number.")


        # ---------------- OPTION 4 ----------------

        elif choice == "4":

            print("\n=== Send Money ===")

            # Get the cellphone number
            number = get_10_digits()

            print("You entered:", number)

            try:
                # Ask for the amount
                amount = float(input("Enter amount to send: R"))

                # Check if amount is valid
                if amount <= 0:

                    print("Invalid amount. Please enter a positive value.")

                # Check if enough money is available
                elif amount > balance:

                    print("Insufficient funds. Money was not sent.")

                # Send the money
                else:

                    balance -= amount

                    print("\nMoney sent successfully!")
                    print(f"Cellphone number: {number}")
                    print(f"Amount sent: R{amount:.2f}")
                    print(f"Remaining balance: R{balance:.2f}")

            except ValueError:

                print("Invalid input. Please enter a number.")


        # ---------------- OPTION 5 ----------------

        elif choice == "5":

            print("Thank you for banking with us. Goodbye!")
            break


        # ---------------- INVALID OPTION ----------------

        else:

            print("Invalid choice, please try again.")


# ------------------- RUN PROGRAM -------------------

if __name__ == "__main__":
    main()
