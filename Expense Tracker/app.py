from flask import Flask, render_template, request, redirect, url_for
import database as db  # Import the database module
from database import get_profile  # Import get_profile utility function from database.py

app = Flask(__name__)

# Create the database tables when the app starts
db.create_tables()

@app.route('/')
def index():
    try:
        # Fetch data for expenses, incomes, and user profile
        expenses = db.get_all_expenses()
        incomes = db.get_all_incomes()
        profile = get_profile()
        return render_template('index.html', expenses=expenses, incomes=incomes, profile=profile)
    except Exception as e:
        print(f"Error loading index page: {e}")
        return "An error occurred while loading the homepage.", 500

@app.route('/add_expense', methods=['POST'])
def add_expense():
    try:
        amount = float(request.form['amount'])
        db.insert_expense(amount)
        return redirect(url_for('index'))
    except Exception as e:
        print(f"Error adding expense: {e}")
        return "An error occurred while adding the expense.", 500

@app.route('/add_income', methods=['POST'])
def add_income():
    try:
        amount = float(request.form['amount'])
        db.insert_income(amount)
        return redirect(url_for('index'))
    except Exception as e:
        print(f"Error adding income: {e}")
        return "An error occurred while adding the income.", 500

@app.route('/delete_expense/<int:id>')
def delete_expense(id):
    try:
        expense = db.get_expense(id)
        if expense is None:
            return "Expense not found", 404
        db.delete_expense(id)
        print(f"Deleted expense ID {id}")
        return redirect(url_for('index'))
    except Exception as e:
        print(f"Error deleting expense ID {id}: {e}")
        return "An error occurred while deleting the expense.", 500

@app.route('/delete_income/<int:id>')
def delete_income(id):
    try:
        income = db.get_income(id)
        if income is None:
            return "Income not found", 404
        db.delete_income(id)
        print(f"Deleted income ID {id}")
        return redirect(url_for('index'))
    except Exception as e:
        print(f"Error deleting income ID {id}: {e}")
        return "An error occurred while deleting the income.", 500

@app.route('/edit_income/<int:id>', methods=['GET', 'POST'])
def edit_income(id):
    try:
        if request.method == 'POST':
            amount = float(request.form['amount'])
            db.update_income(id, amount)
            return redirect(url_for('index'))
        income = db.get_income(id)
        if income is None:
            return "Income not found", 404
        return render_template('edit_income.html', income=income)
    except Exception as e:
        print(f"Error editing income: {e}")
        return "An error occurred while editing the income.", 500

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    try:
        if request.method == 'POST':
            name = request.form['name']
            age = int(request.form['age'])
            occupation = request.form['occupation']
            db.update_profile(name, age, occupation)
            return redirect(url_for('index'))
        profile = get_profile()
        if not profile:
            return "Profile not found. Please create one.", 404
        return render_template('edit_profile.html', profile=profile)
    except Exception as e:
        print(f"Error editing profile: {e}")
        return "An error occurred while editing the profile.", 500

@app.route('/analytics')
def analytics():
    try:
        return render_template('analytics.html', expenses=db.get_all_expenses(), incomes=db.get_all_incomes())
    except Exception as e:
        print(f"Error loading analytics: {e}")
        return "An error occurred while loading the analytics page.", 500

if __name__ == '__main__':
    app.run(debug=True)
