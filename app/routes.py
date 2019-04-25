from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from datetime import datetime
from app import app
from app import db
from app.forms import RegistrationForm, LoginForm, EditProfileForm, WriteForm
from app.models import User, Entry

@app.route('/')
@app.route('/index')
@login_required
def index():
    if current_user.is_authenticated:
        return redirect(url_for('write', username=current_user.username))
    return redirect(url_for('login'))

@app.route('/nowit/<username>/<id>')
def nowit(username, id):
    user = User.query.filter_by(username=username).first()
    if user == None:
        return render_template('user_dne.html', u=username)
    entry = User.query.filter_by(username=username, id=id).first()
    print(entry)
    wits = entry.witnesses
    return render_template('no_wit_left_for_this_content.html', wits=wits)

@app.route('/read/<username>/<id>')
@login_required
def read(username, id):
    entry = Entry.query.get(id)
    author = entry.author.username
    if username != author:
        return redirect(url_for('user', username=current_user.username))
    return render_template('entry.html', entry=entry)

@app.route('/user/<username>', methods=['GET', 'POST'])
@login_required
def user(username):
    entries = current_user.all_entries()
    return render_template('user_page.html', user=current_user, entries=entries)

@app.route('/write/<username>', methods=['GET', 'POST'])
@login_required
def write(username):
    user = User.query.filter_by(username=username).first_or_404()
    form = WriteForm()
    if form.validate_on_submit():
        entry = Entry(title=form.title.data, entry=form.entry.data, author=user)
        db.session.add(entry)
        db.session.commit()

    entries = current_user.all_entries()
    return render_template('write.html', title='Write', user=user, form=form,
                            entries=entries)

@app.route('/edit/<username>/<id>', methods=['GET', 'POST'])
@login_required
def edit(username, id):
    user = User.query.filter_by(username=username).first_or_404()
    form = WriteForm()
    entry = Entry.query.get(id)
    author = entry.author.username
    if username != author or username != current_user.username:
        return redirect(url_for('user', username=current_user.username))
    if form.validate_on_submit():
        entry.set_title(form.title.data)
        entry.set_entry(form.entry.data)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('read', username=current_user.username, id=id))
    elif request.method == 'GET':
        form.title.data = entry.title
        form.entry.data = entry.entry
    return render_template('edit.html', title='Edit Entry', form=form)

@app.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
