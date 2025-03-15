import sqlite3

def insert_record(table_name, data, cursor):
    try:
        columns = ", ".join(data.keys())
        values = ", ".join([f"'{value}'" if isinstance(value, str) else str(value) for value in data.values()])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"


        print(query)
        cursor.execute(query)
        return True
    except Exception as e:
        print(f"Error occurred: {e}")
        return False

def update_record(table_name, record_id, fields, cursor):
    try: 
        set_clause = ", ".join([f"{key} = '{value}'" if isinstance(value, str) else f"{key} = {value}" for key, value in fields.items()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE id = {record_id}"
        cursor.execute(query)
        return True
    except Exception as e:
        print(f"Error occurred: {e}")
        return False

def delete_record(table_name, record_id, cursor):
    try:
        query = f"DELETE FROM {table_name} WHERE id = {record_id}"
        cursor.execute(query)
        return True
    except Exception as e:
        print(f"Error occurred: {e}")
        return False

def select_query(table_name, cursor, columns="*", conditions=None):

    try:
        query = f"SELECT {columns} FROM {table_name}"
        
        if conditions:
            query += f" WHERE {conditions}"
            
        cursor.execute(query)
        
    
        rows = cursor.fetchall()
        
        return rows
    

    except Exception as e:
        print(f"Error occurred: {e}")
        return False

def connect_to_db():
    con = sqlite3.connect('database', check_same_thread=False)


    cur = con.cursor()

    return con, cur


def disconnect_from_db(con, cur):
    if (con):
        cur.close()
        con.close()
    