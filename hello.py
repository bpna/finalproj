from flask import Flask, abort, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('mybutt'))

@app.route('/mybutt')
def mybutt():
    abort(401)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
    else:
        error = 'Invalid username/password'
    return render_template('login.html', error=error)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')

@app.route('/user/<uname>')
def profile(uname):
    # show the user profile for that user
    return '{}\'s profile'.format(uname)

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % subpath
























with app.test_request_context():
    print(url_for('index'))
    print(url_for('hello'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', uname='Patty K'))

