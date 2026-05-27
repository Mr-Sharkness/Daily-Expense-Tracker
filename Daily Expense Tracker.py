print("Welcome to the Daily Expense Tracker!\n")
print(
    "Menu:\n1. Add a new expense\n2. View all expenses\n3. Calculate total and average expense\n4. Clear all expenses\n5. Exit")
exp = []
total = 0
while True:
    user = int(input())
    if user == 1:
        add = float(input())
        exp.append(add)
        print("Expense added successfully!")
    elif user == 2:
        if not exp:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for index, expens in enumerate(exp, start=1):
                print(f"{index}. {expens}")
    elif user == 3:
        if not exp:
            print("No expenses recorded yet.")
        else:
            for i in exp:
                total += i
                avg = total / len(exp)
            print(f"Total expense: {total}")
            print(f"Average expense: {avg}")
    elif user == 4:
        exp.clear()
        print("All expenses cleared.")
    elif user == 5:
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
