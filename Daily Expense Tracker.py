import os
import pickle

File_Name = 'Expense.dat'

def load_expense():
    if os.path.exists(File_Name):
        try:
            with open(File_Name, 'rb') as f:
                return pickle.load(f)
        except (pickle.PickleError, EOFError, AttributeError):
            print("Error: The data file is corrupted or has been manually modified.")
            print("The list has been cleared. Please re-enter your data.")
            return []
        except Exception:
            print("Error: Unknown error. The list has been cleared. Please re-enter your data.")
            return []
    return []

def save_expense(expense):
    try:
        with open(File_Name, 'wb') as f:
            pickle.dump(expense, f)
    except IOError:
        print("Error saving data")

print("Welcome to the Daily Expense Tracker!")

exp = load_expense()

while True:

    print("\nMenu:\n"
          "1. Add a new expense\n"
          "2. View all expenses\n"
          "3. Calculate total and average expense\n"
          "4. Clear all expenses\n"
          "5. Exit")

    try:
        user = int(input("\nEnter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if user == 1:
        try:
            add = float(input("Enter your expense amount: "))
            exp.append(add)
            print("Expense added successfully!")
        except ValueError:
            print("Invalid amount. Please enter a number.")

    elif user == 2:
        if not exp:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for index, expens in enumerate(exp, start = 1):
                print(f"{index}. {expens}")

    elif user == 3:
        if not exp:
            print("No expenses recorded yet.")
        else:
            total = sum(exp)
            avg = total / len(exp)
            print(f"Total expense: {total:.2f}")
            print(f"Average expense: {avg:.2f}")

    elif user == 4:
        exp.clear()
        save_expense(exp)
        print("All expenses cleared.")

    elif user == 5:
        save_expense(exp)
        print("Data saved successfully!")
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
