from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sementara: data user dummy
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home.html')
def home():
    return render_template('home.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/checkout.html')
def checkout():
    return render_template('checkout.html')


@app.route('/profile.html')
def profile():
    return render_template('profile.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/logout', methods=['POST'])
def logout():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
