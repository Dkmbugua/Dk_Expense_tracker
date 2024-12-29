import sqlite3

DB_NAME = 'finance.db'

def create_tables():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create the expenses table
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      amount REAL NOT NULL
                      )''')

    # Create the incomes table
    cursor.execute('''CREATE TABLE IF NOT EXISTS incomes (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      amount REAL NOT NULL
                      )''')

    # Create the profile table
    cursor.execute('''CREATE TABLE IF NOT EXISTS profile (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT,
                      age INTEGER,
                      occupation TEXT
                      )''')

    conn.commit()
    conn.close()

def insert_expense(amount):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (amount) VALUES (?)", (amount,))
    conn.commit()
    conn.close()

def insert_income(amount):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO incomes (amount) VALUES (?)", (amount,))
    conn.commit()
    conn.close()

def get_all_expenses():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, amount FROM expenses")
    expenses = cursor.fetchall()
    conn.close()
    return expenses

def get_all_incomes():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, amount FROM incomes")
    incomes = cursor.fetchall()
    conn.close()
    return incomes

def delete_expense(expense_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()

def update_expense(expense_id, amount):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE expenses SET amount = ? WHERE id = ?", (amount, expense_id))
    conn.commit()
    conn.close()

def get_expense(expense_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, amount FROM expenses WHERE id = ?", (expense_id,))
    expense = cursor.fetchone()
    conn.close()
    return expense

def delete_income(income_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM incomes WHERE id = ?", (income_id,))
    conn.commit()
    conn.close()

def update_income(income_id, amount):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE incomes SET amount = ? WHERE id = ?", (amount, income_id))
    conn.commit()
    conn.close()

def update_profile(name, age, occupation):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Clear existing profile data
    cursor.execute("DELETE FROM profile")
    # Insert the new profile data
    cursor.execute("INSERT INTO profile (name, age, occupation) VALUES (?, ?, ?)", (name, age, occupation))
    conn.commit()
    conn.close()


def get_profile():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT name, age, occupation FROM profile LIMIT 1")
    profile = cursor.fetchone()
    conn.close()
    return profile

def update_profile(name, age, occupation):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Clear existing profile data
    cursor.execute("DELETE FROM profile")
    # Insert the new profile data
    cursor.execute("INSERT INTO profile (name, age, occupation) VALUES (?, ?, ?)", (name, age, occupation))
    conn.commit()
    conn.close()
