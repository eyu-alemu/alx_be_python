class BankAccount:
    """
    Simple BankAccount class with basic encapsulation and operations.
    """

    def __init__(self, initial_balance: float = 0.0):
        # internal (encapsulated) balance
        self._account_balance = float(initial_balance)

    def deposit(self, amount: float) -> None:
        """Add amount to the account balance. Negative deposits are ignored."""
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            raise ValueError("Deposit amount must be a number.")

        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._account_balance += amount

    def withdraw(self, amount: float) -> bool:
        """
        Attempt to withdraw amount from the account.
        Returns True if successful, False if insufficient funds.
        Negative withdrawals are not allowed (raises ValueError).
        """
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            raise ValueError("Withdraw amount must be a number.")

        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")

        if amount <= self._account_balance:
            self._account_balance -= amount
            return True
        else:
            return False

    def display_balance(self) -> None:
        """Print the current balance in a user-friendly format."""
        # Format with two decimal places
        print(f"Current Balance: ${self._account_balance:.2f}")

    # Optional: property to read balance if needed by other code
    @property
    def account_balance(self) -> float:
        return float(self._account_balance)


#!/usr/bin/env python3
import sys
from bank_account import BankAccount

def print_usage():
    print("Usage: python main-0.py <command>[:<amount>]")
    print("Commands:")
    print("  deposit:<amount>   - deposit the amount into the account")
    print("  withdraw:<amount>  - withdraw the amount from the account")
    print("  display            - display current balance")

def main():
    # Example starting balance; change if you want a different starting point
    account = BankAccount(100.0)

    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    # support commands like "deposit:50" or "display"
    raw = sys.argv[1]
    parts = raw.split(":", 1)
    command = parts[0].strip().lower()
    amount = None

    if len(parts) == 2 and parts[1].strip() != "":
        try:
            amount = float(parts[1])
        except ValueError:
            print("Invalid amount. Amount must be a number.")
            sys.exit(1)

    try:
        if command == "deposit" and amount is not None:
            account.deposit(amount)
            # show deposited amount as integer if whole, otherwise two decimals
            if amount.is_integer():
                print(f"Deposited: ${int(amount)}")
            else:
                print(f"Deposited: ${amount:.2f}")

        elif command == "withdraw" and amount is not None:
            if account.withdraw(amount):
                if amount.is_integer():
                    print(f"Withdrew: ${int(amount)}")
                else:
                    print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")

        elif command == "display":
            account.display_balance()

        else:
            print("Invalid command or missing amount.")
            print_usage()
            sys.exit(1)

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
