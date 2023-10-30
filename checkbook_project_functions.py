{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fe8fe512",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "~~~~ Welcome to your terminal checkbook! ~~~~~\n"
     ]
    }
   ],
   "source": [
    "def create_user_profile(first_name, last_name, birthday):\n",
    "    user_profile = {\n",
    "        \"first_name\": first_name,\n",
    "        \"last_name\": last_name,\n",
    "        \"birthday\": birthday,\n",
    "    }\n",
    "    with open('user_profile.json', 'w') as profile_file:\n",
    "        json.dump(user_profile, profile_file)\n",
    "\n",
    "def get_user_profile():\n",
    "    if os.path.exists('user_profile.json'):\n",
    "        with open('user_profile.json', 'r') as profile_file:\n",
    "            user_profile = json.load(profile_file)\n",
    "        return user_profile\n",
    "    return None\n",
    "\n",
    "\n",
    "def create_ledger_file(user_id):\n",
    "    ledger_filename = f\"{user_id}_ledger.txt\"\n",
    "    if not os.path.exists(ledger_filename):\n",
    "        with open(ledger_filename, 'w') as ledger_file:\n",
    "            ledger_file.write(\"0.0\")\n",
    "\n",
    "\n",
    "def get_balance():\n",
    "    with open('ledger.txt', 'r') as ledger_file:\n",
    "        return float(ledger_file.read())\n",
    "\n",
    "def add_debit(amount):\n",
    "    balance = get_balance()\n",
    "    balance -= amount\n",
    "    with open('ledger.txt', 'w') as ledger_file:\n",
    "        ledger_file.write(str(balance)\n",
    "\n",
    "def add_credit(amount):\n",
    "    balance = get_balance()\n",
    "    balance += amount\n",
    "    with open('ledger.txt', 'w') as ledger_file:\n",
    "        ledger_file.write(str(balance))\n",
    "\n",
    "                          \n",
    "def add_debit(amount):\n",
    "    amount = -amount  # Make the amount negative for debits\n",
    "    balance = get_balance()\n",
    "    balance += amount  # Subtract the debit amount from the balance\n",
    "    with open('ledger.txt', 'a') as ledger_file:\n",
    "        ledger_file.write(f\"{amount:.2f}\\n\")\n",
    "        ledger_file.write(f\"Balance: ${balance:.2f}\\n\")\n",
    "\n",
    "def add_credit(amount):\n",
    "    balance = get_balance()\n",
    "    balance += amount  # Add the credit amount to the balance\n",
    "    with open('ledger.txt', 'a') as ledger_file:\n",
    "        ledger_file.write(f\"{amount:.2f}\\n\")\n",
    "        ledger_file.write(f\"Balance: ${balance:.2f}\\n\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
