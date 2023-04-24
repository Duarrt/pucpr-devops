from flask import Flask, render_template, request, redirect, flash, get_flashed_messages

app = Flask(__name__)
app.secret_key = 'chavesecreta12345'

users = {
    'admin': 'admin123',
    'joao': 'joao123'
}

@app.route('/')
def index():
    messages = get_flashed_messages(with_categories=True, category_filter=['error'])
    return render_template('index.html', messages=messages)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        return f'Seja bem vindo, {username}!'
    else:
        flash('Usuário ou senha inválido!', 'error')
        return redirect('/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8085 debug=True)