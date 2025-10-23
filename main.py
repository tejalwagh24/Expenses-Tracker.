# Expense Tracker
# Author: Tejal
# Date: 2025-10-23
# Description: Simple program to track daily expenses

# Function to add an expense
def add_expense(expenses):
    print("\n--- Add New Expense ---")
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter category (Food/Travel/Bills/Other): ")
    expenses.append({"name": name, "amount": amount, "category": category})
    print(f"Expense '{name}' of {amount} added under {category} category.\n")

# Function to view all expenses
def view_expenses(expenses):
    print("\n--- All Expenses ---")
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    total = 0
    category_totals = {}
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - {expense['amount']} - {expense['category']}")
        total += expense['amount']
        cat = expense['category']
        category_totals[cat] = category_totals.get(cat, 0) + expense['amount']
    print(f"\nTotal Expenses: {total}")
    print("Expenses by Category:")
    for cat, amt in category_totals.items():
        print(f"  {cat}: {amt}")
    print()

# Function to delete an expense
def delete_expense(expenses):
    print("\n--- Delete Expense ---")
    if not expenses:
        print("No expenses to delete.\n")
        return
    view_expenses(expenses)
    index = int(input("Enter the number of the expense to delete: "))
    if 1 <= index <= len(expenses):
        removed = expenses.pop(index - 1)
        print(f"Removed expense '{removed['name']}' of {removed['amount']}.\n")
    else:
        print("Invalid index! Try again.\n")

# Main program loop
def main():
    expenses = []
    while True:
        print("=== Expense Tracker Menu ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-4.\n")

if _name_ == "_main_":
    main()
