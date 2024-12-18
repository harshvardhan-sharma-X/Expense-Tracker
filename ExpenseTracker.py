import pandas as pd       
import matplotlib.pyplot as plt  
import os    

class ExpenseTracker:
    def __init__(self, filename='expense.csv'):   
        self.filename = filename
        if os.path.exists(filename):
            self.expenses = pd.read_csv(filename)   
        else:
            self.expenses = pd.DataFrame(columns = ['Data','Category','Amount','Description'])

    def add_expense(self, date, category, amount, description=''):
        new_expense = {'Date': date, 'Category': category, 'Amount': float(amount), 'Description': description}
        self.expenses = self.expenses.append(new_expense ,ignore_index=True)
        self.expenses.to_csv(self.filename, index=False)
        print("✅ Expense added succesfully!")      

    def view_expenses(self): 
        print("\n Your Expenses:")
        print(self.expenses)

    def visualise_expenses(self):
        if self.expenses.empty:
            print("No expenses to visualise")
            return 
        
        category_totals = self.expenses.groupby('Category')['Amount'].sum()
        plt.figure(figsize = (6, 6))
        plt.pie(category_totals, labels = category_totals.index, )
        plt.title('Expenses by category')
        plt.show()

    def generate_report(self):
        if self.expenses.empty:
            print("No expenses to generate a report")
            return 
        
        total_expenses = self.expenses['Amount'].sum()
        category_totals = self.expenses.groupby('Category')['Amount'].sum()
        print("\n Expense report")
        print("-"*30)
        print(f"Total Expenses: ${total_expenses:.2f}\n")
        print("Expenses by category:")
        print(category_totals) 

def main():
    tracker = ExpenseTracker()
    while True:
        print("\n Personal expense tracker ")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. visualize Expenses")
        print("4. Generate Report")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD)")
            category = input("Enter category (e.g., Food, Transport, Rent): ")
            amount = float(input("Enter amount: $"))
            description = input("Enter description(optional): ")
            tracker.add_expense(date, category.title() , amount, description.title())

        elif choice == '2':
            tracker.view_expenses()

        elif choice == '3':
            tracker.visualise_expenses()

        elif choice == '4':
            tracker.generate_report()

        elif choice == '5':
            print("Exiting the expense tracker. goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 


