<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Expense Tracker - README</title>
</head>
<body>

<h1>📊 Expense Tracker</h1>

<p>The <strong>Expense Tracker</strong> is a simple Python-based tool to manage personal expenses. It allows users to track, view, visualize, and generate reports of their expenses.</p>

<hr>

<h2>📦 Features</h2>
<ul>
    <li>📝 <strong>Add Expense:</strong> Add new expenses with date, category, amount, and optional description.</li>
    <li>📄 <strong>View Expenses:</strong> View a list of all recorded expenses.</li>
    <li>📊 <strong>Visualize Expenses:</strong> View a pie chart of expenses categorized by type.</li>
    <li>📈 <strong>Generate Report:</strong> View a summary report of total expenses and breakdown by category.</li>
</ul>

<hr>

<h2>📂 Prerequisites</h2>
<p>Make sure you have Python installed on your system. You will also need the following Python libraries:</p>
<ul>
    <li><code>pandas</code></li>
    <li><code>matplotlib</code></li>
</ul>

<p>You can install the required libraries using pip:</p>
<pre><code>pip install pandas matplotlib</code></pre>

<hr>

<h2>🚀 How to Run</h2>
<ol>
    <li>Clone the repository or copy the <code>ExpenseTracker</code> script.</li>
    <li>Open a terminal or command prompt and navigate to the directory where the script is saved.</li>
    <li>Run the script using the following command:</li>
</ol>
<pre><code>python expense_tracker.py</code></pre>

<p>Follow the on-screen prompts to add, view, visualize, or generate reports of your expenses.</p>

<hr>

<h2>📘 Usage</h2>

<ol>
    <li>Upon running, you will see the following menu options:
        <ul>
            <li>1️⃣ <strong>Add Expense</strong> - Add a new expense.</li>
            <li>2️⃣ <strong>View Expenses</strong> - View all your expenses in a tabular format.</li>
            <li>3️⃣ <strong>Visualize Expenses</strong> - View a pie chart of expenses categorized by type.</li>
            <li>4️⃣ <strong>Generate Report</strong> - Generate a summary of your total expenses and category-wise breakdown.</li>
            <li>5️⃣ <strong>Exit</strong> - Exit the program.</li>
        </ul>
    </li>
    <li>Enter the corresponding number to choose an option.</li>
</ol>

<hr>

<h2>📄 Code Structure</h2>
<pre><code>.
├── expense.csv  # CSV file where all expenses are stored (auto-created)
└── expense_tracker.py  # Main Python script for the Expense Tracker
</code></pre>

<p>The script consists of the following key components:</p>
<ul>
    <li><strong>ExpenseTracker Class</strong>: Manages adding, viewing, visualizing, and generating reports for expenses.</li>
    <li><strong>Main Function</strong>: Provides the user interface for interacting with the expense tracker.</li>
</ul>

<hr>

<h2>🔧 Methods</h2>

<h3>1. <code>add_expense(date, category, amount, description='')</code></h3>
<p>Adds a new expense to the CSV file and updates the DataFrame.</p>

<h3>2. <code>view_expenses()</code></h3>
<p>Displays all expenses in a tabular format.</p>

<h3>3. <code>visualise_expenses()</code></h3>
<p>Generates a pie chart of expenses categorized by type.</p>

<h3>4. <code>generate_report()</code></h3>
<p>Displays the total expenses and a breakdown by category.</p>

<hr>

<h2>📸 Screenshots</h2>
<p><em>Example of Visualization (Pie Chart):</em></p>
<img src="screenshot.png" alt="Expense Visualization Pie Chart" style="width:100%; max-width:600px;">

<hr>

<h2>💡 Possible Improvements</h2>
<ul>
    <li>✅ Add error handling for invalid inputs.</li>
    <li>✅ Add ability to delete or edit expenses.</li>
    <li>✅ Export reports in PDF or Excel format.</li>
</ul>

<hr>

<h2>📜 License</h2>
<p>This project is open-source and available under the <strong>MIT License</strong>.</p>

<hr>

<h2>📞 Contact</h2>
<p>Have any questions or feedback? Feel free to reach out!</p>

</body>
</html>
