<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ExpenseTracker.py - README</title>
</head>
<body>
    <h1>💸 ExpenseTracker.py</h1>
    
<p><strong>ExpenseTracker.py</strong> is a simple, user-friendly command-line application to track and manage your personal expenses. This tool allows you to add expenses, view a summary of expenses, visualize spending habits, and generate expense reports.</p>

<h2>📋 Features</h2>
<ul>
    <li>✅ Add new expenses with details like date, category, amount, and description.</li>
    <li>📄 View all your recorded expenses in a tabular format.</li>
    <li>📊 Visualize expenses by category using a pie chart.</li>
    <li>📈 Generate a detailed expense report with total expenses and a category breakdown.</li>
</ul>

<h2>🛠️ Installation</h2>
<ol>
    <li>Ensure you have <strong>Python 3.x</strong> installed on your system.</li>
    <li>Install the required libraries using the following command:
        <pre><code>pip install pandas matplotlib</code></pre>
    </li>
    <li>Download the <strong>ExpenseTracker.py</strong> file and place it in your desired directory.</li>
</ol>

<h2>🚀 Usage</h2>
<ol>
    <li>Run the script with the following command:
        <pre><code>python ExpenseTracker.py</code></pre>
        </li>
        <li>Use the menu to navigate through the available options:
            <ul>
                <li>1️⃣ Add Expense</li>
                <li>2️⃣ View Expenses</li>
                <li>3️⃣ Visualize Expenses</li>
                <li>4️⃣ Generate Report</li>
                <li>5️⃣ Exit</li>
            </ul>
        </li>
    </ol>

<h2>📚 Example</h2>
    <pre>
    Personal Expense Tracker 
    1. Add Expense
    2. View Expenses
    3. Visualize Expenses
    4. Generate Report
    5. Exit
    
Enter your choice (1-5): 1
    Enter date (YYYY-MM-DD): 2024-12-18
    Enter category (e.g., Food, Transport, Rent): Food
    Enter amount: $15.50
    Enter description (optional): Lunch at cafe
    ✅ Expense added successfully!
    </pre>

<h2>📂 File Structure</h2>
    <pre>
    └── ExpenseTracker.py   # Main script file
        └── expense.csv      # CSV file where your expenses are stored (auto-created if it does not exist)
    </pre>

<h2>🛠️ Methods</h2>
    <ul>
        <li><strong>add_expense(date, category, amount, description)</strong>: Adds a new expense entry.</li>
        <li><strong>view_expenses()</strong>: Displays all expenses recorded in the CSV file.</li>
        <li><strong>visualise_expenses()</strong>: Generates a pie chart to visualize expenses by category.</li>
        <li><strong>generate_report()</strong>: Provides a detailed summary of expenses by category and total expenses.</li>
    </ul>

<h2>📋 CSV File Format</h2>
    <p>The expenses are stored in a CSV file named <strong>expense.csv</strong> in the following format:</p>
    <pre>
    Date,Category,Amount,Description
    2024-12-18,Food,15.50,Lunch at cafe
    2024-12-17,Transport,50.00,Uber ride
    2024-12-16,Groceries,120.30,Weekly shopping
    </pre>

<h2>📢 Important Notes</h2>
    <ul>
        <li>Make sure the <strong>expense.csv</strong> file is in the same directory as the <strong>ExpenseTracker.py</strong> script.</li>
        <li>The CSV file is auto-generated if it does not exist, so no manual setup is required.</li>
    </ul>

<h2>🤝 Contributing</h2>
    <p>Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.</p>


<h2>📞 Contact</h2>
    <p>If you have any questions or issues, feel free to open an issue on the repository or reach out to the developer.</p>
</body>
</html>
