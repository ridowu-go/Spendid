import os
import json
from datetime import datetime

FILENAME = "expenses.json"

def load_expenses():
    """Loads expenses from the JSON file when the program starts."""
    if os.path.exists(FILENAME) and os.path.getsize(FILENAME) > 0:
        with open(FILENAME, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("⚠️ Warning: Data file is corrupted. Starting with an empty list.")
                return []
    return []

def save_expenses(expenses):
    """Saves the entire expenses list back to the JSON file."""
    try:
        with open(FILENAME, "w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4)
    except IOError as e:
        print(f"❌ Error saving to file: {e}")

def add_expense(expenses):
    """Prompts user for details and appends a new expense."""
    print("\n--- 📝 Add New Expense ---")
    
    # Input Amount with validation
    while True:
        try:
            amount = float(input("Enter amount (₦): "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    category = input("Enter category (e.g., Food, Transport, Utilities): ").strip()
    description = input("Enter description (optional): ").strip()

    new_expense = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "amount": amount,
        "category": category if category else "Uncategorized",
        "description": description if description else "N/A"
    }

    expenses.append(new_expense)
    save_expenses(expenses)  # Auto-save
    print(f"✅ Added ₦{amount:,.2f} under '{new_expense['category']}'!")

def view_expenses(expenses):
    """Displays all logged expenses in a clean, human-readable format."""
    print("\n--- 📋 All Expenses ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    for index, exp in enumerate(expenses, 1):
        print(f"{index}. [{exp['date']}] ₦{exp['amount']:,.2f} | {exp['category']} | Desc: {exp['description']}")

def calculate_totals(expenses):
    """Calculates overall spending and breaks it down by category."""
    print("\n--- 📊 Spending Analytics ---")
    if not expenses:
        print("No data available to calculate.")
        return

    # Total Overall
    total_overall = sum(exp["amount"] for exp in expenses)
    print(f"💰 Total Overall Spending: ₦{total_overall:,.2f}\n")

    # Grouping by Category
    category_totals = {}
    for exp in expenses:
        cat = exp["category"]
        category_totals[cat] = category_totals.get(cat, 0) + exp["amount"]

    print("🗂️ Breakdown by Category:")
    for cat, total in category_totals.items():
        percentage = (total / total_overall) * 100
        print(f"  ▪️ {cat}: ₦{total:,.2f} ({percentage:.1f}%)")

def delete_expense(expenses):
    """Deletes an expense item based on list index selection."""
    print("\n--- 🗑️ Delete an Expense ---")
    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses(expenses)
    
    while True:
        try:
            choice = input("\nEnter the line number to delete (or 'c' to cancel): ").strip()
            if choice.lower() == 'c':
                return
            
            index = int(choice) - 1
            if 0 <= index < len(expenses):
                removed = expenses.pop(index)
                save_expenses(expenses)  # Auto-save updates
                print(f"🗑️ Successfully deleted: ₦{removed['amount']:,.2f} for '{removed['category']}'.")
                break
            else:
                print("Invalid number. Choose an index from the list.")
        except ValueError:
            print("Please enter a valid row number.")

def main():
    # Load data automatically at startup
    expenses = load_expenses()
    
    while True:
        print("\n=============================")
        print("       EXPENSE TRACKER       ")
        print("=============================")
        print("1. ➕ Add Expense")
        print("2. 📋 View All Expenses")
        print("3. 📊 View Total & Category Summary")
        print("4. 🗑️ Delete Expense")
        print("5. 🚪 Exit")
        
        choice = input("\nSelect an option (1-5): ").strip()
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            calculate_totals(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Please select 1-5.")

if __name__ == "__main__":
    main()
