from webbrowser import register_X_browsers

from flask import Flask, request, abort, redirect, url_for, render_template
from markupsafe import escape
from database import Database

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        login_btn = request.form['login']
        if login_btn == '1':
            return login_get()
        register_btn = request.form['register']
        if register_btn == '2':
            return register_get()

    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return login_post()
    else:
        return login_get()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return register_post()
    else:
        return register_get()

def register_get():
    return render_template('register.html')

def register_post():
    reg_email = request.form['reg_email']
    reg_password = request.form['reg_password']
    db.insert_user(reg_email, reg_password)
    return render_template('profile.html')

def login_get():
    return render_template('login.html')

def login_post():
    user_login = request.form['log_name']
    user_password = request.form['log_password']
    data = db.select_user(user_login)
    print(data)
    valid_password = data['password']
    db.select_user(user_login)
    error = "Неверный логин или пароль!"
    message = f"Добро пожаловать, {data['name']}"
    print(str(valid_password), str(user_password))
    if str(user_password) == str(valid_password):
        return render_template('profile.html', message=message)
    else:
        return render_template('login', error=error)

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

# with app.test_request_context():
#     print(url_for('hello'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))

if __name__ == "__main__":
    db = Database('localhost', 'root', '', 'academy')
    app.run(host='0.0.0.0', port=15000, debug=True)