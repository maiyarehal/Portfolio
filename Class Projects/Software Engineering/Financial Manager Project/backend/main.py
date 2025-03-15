from flask import Flask, jsonify, request
import util


app = Flask(__name__)


@app.route('/api/signup', methods = ['POST'])
def signup():

    con, cur = util.connect_to_db()

    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    user_exists = util.select_query("users", cur, conditions=f"username = '{username}'")

    if user_exists:
        return_msg = False
        
    else:
        return_msg = util.insert_record("users", {'username' : username, 'pass' : password}, cur)
        con.commit()

    util.disconnect_from_db(con, cur)
    return jsonify({'user_signup' : return_msg})

@app.route('/api/login', methods = ['POST'])
def login():
    con, cur = util.connect_to_db()
    data = request.get_json()

    print(data)
    username = data.get('username')
    password = data.get('password')

    result = util.select_query("users", cur, conditions=f"username = '{username}' AND pass = '{password}'")

    user_login = result != []

    util.disconnect_from_db(con, cur)
    return jsonify({'user_login': user_login})

@app.route('/api/check-account', methods = ['POST'])
def check_account():
    con, cur = util.connect_to_db()
    data = request.get_json()

    username = data.get('username')

    condition = f"username = '{username}'"

    result = util.select_query("users", cur, conditions=condition)

    print(result)

    user_exists = result != []
    util.disconnect_from_db(con, cur)
    return jsonify({'userExists': user_exists})


@app.route('/api/transactions', methods = ['POST', 'GET', 'DELETE'])
def transactions():
    con, cur = util.connect_to_db()
    if request.method == 'POST':

        username = request.args.get('username')

        user = util.select_query("users", cur, columns="id", conditions=f"username = '{username}'")

        user_id = user[0][0]
        data = request.get_json() 
        del data['id']
        data['user_id'] = user_id
        result = util.insert_record('transactions', data, cur)

        con.commit()
        return_msg = {'message': result}

    elif request.method == 'GET':
        username = request.args.get('username')

        user = util.select_query("users", cur, columns="id", conditions=f"username = '{username}'")

        user_id = user[0][0]
        trans = util.select_query("transactions", cur, columns="id, type, category, amount, date", conditions=f"user_id = '{user_id}'")


        transactions = []
        for transaction in trans:
            transactions.append({
                'id': transaction[0],
                'type': transaction[1],
                'category': transaction[2],
                'amount': transaction[3],
                'date': transaction[4],
            })

  
        transaction_data = {
        'username': username,
        'transactions': transactions
        }

        return_msg = {'message': 'Retrieved transaction data', 'data': transaction_data}

    elif request.method == 'DELETE':
        id = request.args.get('id')


        result = util.delete_record('transactions', id, cur)

        con.commit()

        return_msg = {'message': result}

    util.disconnect_from_db(con, cur)
    return jsonify({'success' : return_msg})



@app.route('/api/budgets', methods = ['POST', 'GET', 'DELETE', 'PUT'])
def budget():
    con, cur = util.connect_to_db()

    if request.method == 'POST':
        username = request.args.get('username')
        user = util.select_query("users", cur, columns="id", conditions=f"username = '{username}'")
        if not user:
            return jsonify({'error': 'User not found'}), 404

        user_id = user[0][0]
        data = request.get_json()
        data['user_id'] = user_id  

       
        data.pop('id', None)

        
        result = util.insert_record('budgets', data, cur)

        con.commit()
        return_msg = {'message': result}


    elif request.method == 'GET':
        username = request.args.get('username')

        user = util.select_query("users", cur, columns="id", conditions=f"username = '{username}'")

        user_id = user[0][0]

        budg = util.select_query("budgets", cur, columns="id, category, amount_limit, spent, start_date, end_date", conditions=f"user_id = '{user_id}'")


        budgets = []

        for budget in budg:
            budgets.append({
                'id': budget[0],
                'category': budget[1],
                'amount_limit': budget[2],
                'spent': budget[3],
                'start_date': budget[4],
                'end_date': budget[5],
            })

        budgets_data = {
            'username': username,
            'budgets': budgets
        }
        return_msg = {'message': 'Retrieved budget data', 'data': budgets_data}

    elif request.method == 'PUT':
        data = request.get_json()
        budget_id = data.get('id')

        if not budget_id:
            return jsonify({'error': 'Missing budget ID for update'})

        result = util.update_record('budgets',budget_id, data, cur, )



        con.commit()

        return_msg = {'message': result}


    elif request.method == 'DELETE':
        budget_id = request.args.get('id')
        if not budget_id:
            return jsonify({'error': 'Missing budget ID for deletion'})

        result = util.delete_record('budgets', budget_id, cur)
        con.commit()
        return_msg = {'message': result}
        
    util.disconnect_from_db(con, cur)
    return jsonify({'success' : return_msg}) 


@app.route('/api/trans', methods = ['GET'])
def trans():
    username = request.args.get('username')
    cat = request.args.get('type')

    con, cur = util.connect_to_db()
    user = util.select_query("users", cur, columns="id", conditions=f"username = '{username}'")

    user_id = user[0][0]

    result = util.select_query("transactions", cur, columns="id, type, category, amount, date", conditions=f"user_id = '{user_id}' AND type = '{cat}'")

    transactions = []
    for transaction in result:
        transactions.append({
            'id': transaction[0],
            'type': transaction[1],
            'category': transaction[2],
            'amount': transaction[3],
            'date': transaction[4],
        })

    transaction_data = {
        'username': username,
        'transactions': transactions
    }
    
    util.disconnect_from_db(con, cur)

    return jsonify(transaction_data)


if __name__ == '__main__':
    app.debug = True
    ip = '127.0.0.1'
    app.run(host=ip, port=5000)