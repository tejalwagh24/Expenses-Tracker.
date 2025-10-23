# Expense Tracker
# Author: Your Name
# Date: 2025-10-23
# Description: Simple program to track daily expenses

# Function to add an expense
def add_expense(expenses):
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter category (Food/Travel/Bills/Other): ")
    expenses.append({"name": name, "amount": amount, "category": category})
    print("Expense added successfully!\n")

# Function to view all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    print("\n--- Your Expenses ---")
    total = 0
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - {expense['amount']} - {expense['category']}")
        total += expense['amount']
    print(f"Total Expenses: {total}\n")

# Main program loop
def main():
    expenses = []
    while True:
        print("Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")

if _name_ == "_main_":
    main()
