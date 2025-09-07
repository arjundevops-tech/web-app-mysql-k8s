from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Temporary in-memory "database"
users = {}  # key = email, value = dict(username, password_hash)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if email in users:
            return "Email already registered. Please log in."

        hashed_password = generate_password_hash(password, method='sha256')
        users[email] = {
            'username': username,
            'password': hashed_password
        }
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = users.get(email)

        if user and check_password_hash(user['password'], password):
            return redirect(url_for('dashboard', username=user['username']))
        else:
            return "Invalid email or password."

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    # In a real app, you'd check login state, but here we just show a simple page
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
