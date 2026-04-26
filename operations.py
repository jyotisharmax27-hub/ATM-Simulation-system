import data

def display_balance():
    print(f"\nCurrent Balance: ₹{data.balance}")

def deposit():
    amount = float(input("Enter amount to deposit: "))
    
    if amount > 0:
        data.balance += amount
        data.transactions.append(f"Deposited: ₹{amount}")
        print(f"₹{amount} deposited successfully.")
    else:
        print("Invalid amount.")

def withdraw():
    amount = float(input("Enter amount to withdraw: "))
    
    if amount <= 0:
        print("Invalid amount.")
    elif amount > data.balance:
        print("Insufficient balance.")
    else:
        data.balance -= amount
        data.transactions.append(f"Withdrawn: ₹{amount}")
        print(f"₹{amount} withdrawn successfully.")

def statement():
    print("\nTransaction Statement:")
    
    if not data.transactions:
        print("No transactions yet.")
    else:
        for t in data.transactions:
            print("-", t)