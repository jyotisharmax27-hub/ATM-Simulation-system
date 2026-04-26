import operations

while True:
    print("\n====== ATM MENU ======")
    print("1. Display Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Statement")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        operations.display_balance()

    elif choice == '2':
        operations.deposit()

    elif choice == '3':
        operations.withdraw()

    elif choice == '4':
        operations.statement()

    elif choice == '5':
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid choice. Try again.")