# Spendid
Spend smartly, live splendidly. A personal expense and cash flow tracker.
# Spendid 💰

**Spendid** is a lightweight, terminal-based Expense Tracker built in Python. It helps you manage your personal finances by tracking your income outflows, categorizing your expenses, and providing quick breakdowns of your spending habits—all from the comfort of your command line.

---

## ✨ Features

- **Add Expenses:** Easily log a spending amount, assign a category, and include a brief description.
- **View History:** Display a clean, organized list of all your recorded expenses.
- **Financial Analytics:** 
  - Instantly calculate your total overall spending.
  - View a broken-down total of your spending by specific categories (e.g., Food, Transport, Rent).
- **Manage Entries:** Delete accidental or outdated expense records using a simple index number.
- **Data Persistence:** Your data automatically saves to a file and reloads every time you start the app, ensuring you never lose track of your progress.

---

## 🛠️ Tech Stack & Concepts Used

- **Language:** Python 3
- **Data Structures:** Lists (to manage collections) and Dictionaries (for individual expense models).
- **Data Persistence:** JSON (JavaScript Object Notation) file handling via Python's built-in `json` module.
- **Control Flow:** `while` loops for the interactive CLI menu, `for` loops for analytical parsing, and conditional statement routing.
- **Error Handling:** `try/except` blocks to handle invalid user input (e.g., text inputs instead of numbers) and safely handle missing files at startup.

---

## 🚀 How It Works (Example Data Model)

Every expense logged into **Spendid** follows this structured format:

```python
{
    "date": "2026-11-05 12:03",
    "amount": 5000,
    "category": "Food",
    "description": "Lunch"
}
```

---

## 🔧 Installation & Usage

1. **Clone or save the script:**
   Save the main file as `tracker.py`.

2. **Run the application:**
   Open your terminal or command prompt and run:
   ```bash
   python tracker.py
   ```

3. **Navigate the Menu:**
   Follow the numerical on-screen prompts to add, view, analyze, or delete your expenses!
