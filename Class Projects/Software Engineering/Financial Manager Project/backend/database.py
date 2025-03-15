import sqlite3


conn = sqlite3.connect('database')

cur = conn.cursor()


cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        pass TEXT NOT NULL
    )
''')


cur.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        type TEXT NOT NULL CHECK(type IN ('Income', 'Expense')),
        category TEXT NOT NULL,
        amount REAL NOT NULL,
        date TEXT NOT NULL,
        notes TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE
    )
''')


cur.execute('''
    CREATE TABLE IF NOT EXISTS budgets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        category TEXT NOT NULL,
        amount_limit REAL NOT NULL,
        start_date TEXT NOT NULL,
        end_date TEXT NOT NULL,
        spent REAL NOT NULL,
        notes TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE
    )
''')


users_data = [
    ('john_doe', 'test'),
    ('jane_smith', 'test'),
    ('mike_jones', 'test')
]

cur.executemany('''
    INSERT INTO users (username, pass) VALUES (?, ?)
''', users_data)


transactions_data = [
  
    (1, 'Income', 'Salary', 5000.00, '2024-03-01', 'March salary'),
    (1, 'Income', 'Freelance Project', 1200.50, '2024-03-15', 'Website development project'),
  
    (1, 'Expense', 'Rent', 1500.00, '2024-03-05', 'March rent payment'),
    (1, 'Expense', 'Groceries', 350.25, '2024-03-10', 'Weekly groceries'),
    (1, 'Expense', 'Utilities', 120.75, '2024-03-15', 'Electricity bill'),
 
    (2, 'Income', 'Salary', 4800.00, '2024-03-01', 'March salary'),
    (2, 'Income', 'Side Job', 600.00, '2024-03-18', 'Part-time work'),

    (2, 'Expense', 'Rent', 1400.00, '2024-03-05', 'March rent payment'),
    (2, 'Expense', 'Entertainment', 200.00, '2024-03-12', 'Concert tickets'),
    (2, 'Expense', 'Groceries', 300.00, '2024-03-10', 'Weekly groceries'),
  
    (3, 'Income', 'Salary', 5500.00, '2024-03-01', 'March salary'),
    (3, 'Income', 'Investment', 300.75, '2024-03-20', 'Stock dividends'),
  
    (3, 'Expense', 'Rent', 1600.00, '2024-03-05', 'March rent payment'),
    (3, 'Expense', 'Dining Out', 150.50, '2024-03-12', 'Dinner with friends'),
    (3, 'Expense', 'Groceries', 400.00, '2024-03-10', 'Weekly groceries')
]

cur.executemany('''
    INSERT INTO transactions (user_id, type, category, amount, date, notes)
    VALUES (?, ?, ?, ?, ?, ?)
''', transactions_data)


budgets_data = [
    (1, 'Rent', 1600.00, '2024-03-01', '2024-03-31', 0.00, 'Monthly rent budget'),
    (1, 'Groceries', 400.00, '2024-03-01', '2024-03-31', 0.00, 'Monthly grocery budget'),
    (2, 'Rent', 1500.00, '2024-03-01', '2024-03-31', 0.00, 'Monthly rent budget'),
    (2, 'Entertainment', 250.00, '2024-03-01', '2024-03-31', 0.00, 'Entertainment budget'),
    (3, 'Rent', 1700.00, '2024-03-01', '2024-03-31', 0.00, 'Monthly rent budget'),
    (3, 'Dining Out', 200.00, '2024-03-01', '2024-03-31', 0.00, 'Dining out budget')
]

cur.executemany('''
    INSERT INTO budgets (user_id, category, amount_limit, start_date, end_date, spent, notes)
    VALUES (?, ?, ?, ?, ?, ?, ?)
''', budgets_data)


query = '''
    SELECT 
        users.username,
        transactions.type,
        transactions.category,
        transactions.amount,
        transactions.date,
        transactions.notes
    FROM transactions
    INNER JOIN users ON transactions.user_id = users.id
    WHERE users.username = 'john_doe';
'''

cur.execute(query)

rows = cur.fetchall()

for row in rows:
    print(row)


conn.commit()
conn.close()
