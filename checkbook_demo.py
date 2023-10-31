import os
import json
import checkbook_project_functions as cpf

while True:
    print("Welcome to your terminal checkbook.")
    print("1. View current balance")
    print("2. Add a debit (withdrawal)")
    print("3. Add a credit (deposit)")
    print("4. Exit")
        
    choice = input("Please select an action (1/2/3/4): ")
        
    if choice == '1':
        balance = cpf.get_balance()
        print(f"Current balance: ${balance}")
    elif choice == '2':
        try:
            debit_amount = float(input("Enter the debit amount: $"))
            cpf.add_debit(debit_amount)
            print(f"${debit_amount} debited successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
    elif choice == '3':
        try:
            credit_amount = float(input("Enter the credit amount: $"))
            cpf.add_credit(credit_amount)
            print(f"${credit_amount} credited successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
    elif choice == '4':
        print("Exiting the application.")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")