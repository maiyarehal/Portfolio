import util

import sqlite3


conn = sqlite3.connect('database')


cur = conn.cursor()



# util.insert_record('users', {'username': 'test_user', 'pass': 'test'}, cur)

# conn.commit()
test = util.select_query("users", cur, conditions="username = 'john_doe' AND pass = 't'")

if not test:
    print("yes")


"""util.delete_record('users', 4, cur)"""
"""
def insert_record(table_name, data, cursor):
def update_record(table_name, record_id, fields, cursor):

def delete_record(table_name, record_id, cursor):

def select_query(table_name, cursor, columns="*", conditions=None):
"""