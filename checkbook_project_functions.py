import os
import json 

import os
import json

def get_or_create_user_profile(first_name, last_name):
    user_profiles = []

    if os.path.exists('user_profiles.json'):
        with open('user_profiles.json', 'r') as profiles_file:
            user_profiles = json.load(profiles_file)

    for user_profile in user_profiles:
        if user_profile.get("first_name") == first_name and user_profile.get("last_name") == last_name:
            return user_profile

    new_user_profile = {
        "first_name": first_name,
        "last_name": last_name,
    }

    user_profiles.append(new_user_profile)

    with open('user_profiles.json', 'w') as profiles_file:
        json.dump(user_profiles, profiles_file)

    balance_filename = f"{first_name}_{last_name}_balance.txt"
    with open(balance_filename, 'w') as balance_file:
        balance_file.write("0.00")

    return new_user_profile
    
def get_balance():
    with open('balance.txt', 'r') as ledger_file:
        lines = ledger_file.readlines()

    balance = 0.0  
    for line in reversed(lines):
        if line.startswith("Balance: $"):
            balance_str = line.split('$')[1] 
            balance = float(balance_str) 
            break  

    return balance


def add_debit(amount):
    balance = get_balance()
    new_balance = balance - amount
    with open('balance.txt', 'a') as ledger_file:
        ledger_file.write(f"-${amount:.2f}\n")
        ledger_file.write(f"Balance: ${new_balance:.2f}\n")

def add_credit(amount):
    balance = get_balance()
    new_balance = balance + amount
    with open('balance.txt', 'a') as ledger_file:
        ledger_file.write(f"+${amount:.2f}\n")
        ledger_file.write(f"Balance: ${new_balance:.2f}\n")
