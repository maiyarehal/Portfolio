from flask import Flask, render_template_string
from util import get_db_connection

app = Flask(__name__)

# Database configuration
app.config['DB_NAME'] = 'fruits_db'           
app.config['DB_USER'] = 'postgres'            
app.config['DB_PASSWORD'] = '123'             
app.config['DB_HOST'] = 'localhost'           

# Route to update basket_a 
@app.route('/api/update_basket_a')
def update_basket_a():
    conn = get_db_connection()
    if conn is None:
        return "Error connecting to the database"

    try:
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO basket_a (a, fruit_a) VALUES (%s, %s)
        ON CONFLICT (a) DO NOTHING
        """, (5, 'Cherry'))
        #cur.execute("INSERT INTO basket_a (a, fruit_a) VALUES (%s, %s)", (5, 'Cherry'))
        conn.commit()
        cur.close()
        conn.close()
        return "Success!"
    except Exception as e:
        return f"Error: {e}"
    


# Route to display unique fruits 
@app.route('/api/unique')
def unique_fruits():
    conn = get_db_connection()
    if conn is None:
        return "Error connecting to the database"

    try:
        cur = conn.cursor()
        cur.execute("SELECT DISTINCT fruit_a FROM basket_a")
        unique_a = [row[0] for row in cur.fetchall()]

        cur.execute("SELECT DISTINCT fruit_b FROM basket_b")
        unique_b = [row[0] for row in cur.fetchall()]

        cur.close()
        conn.close()

        # HTML table
        html_template = '''
        <html>
            <body>
                <h2>Unique Fruits in Basket A and Basket B</h2>
                <table border="1">
                    <tr><th>Unique Fruits in Basket A</th><th>Unique Fruits in Basket B</th></tr>
                    <tr>
                        <td>{{ unique_a }}</td>
                        <td>{{ unique_b }}</td>
                    </tr>
                </table>
            </body>
        </html>
        '''
        return render_template_string(html_template, unique_a=", ".join(unique_a), unique_b=", ".join(unique_b))

    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
