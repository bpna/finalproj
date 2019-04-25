from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login
from hashlib import md5

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    entries = db.relationship('Entry', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
                digest, size)

    def all_entries(self):
        return Entry.query.filter_by(user_id=self.id)
#        return Entry.query.order_by(Entry.time.desc()).filter(
#                Entry.user_id == self.id).limit(3).all()

    def entry(self, key):
        return entries

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), index=True, default='untitled')
    entry = db.Column(db.Text)
    time = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Entry {}\n{}\n\n{}>\n'.format(self.time, self.title, self.entry)

    def set_title(self, new_title):
        self.title = new_title

    def set_entry(self, new_entry):
        self.entry = new_entry

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
