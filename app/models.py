from app.extensions import db
from flask_login import UserMixin


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    published = db.Column(db.Boolean, default=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    image = db.Column(db.String(255), nullable=True)
    text = db.Column(db.String, nullable=False)

    def __repr__(self):
        return self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    posts = db.relationship('Post', backref='category', uselist=True)

    def __repr__(self):
        return self.name


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    salt = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String, nullable=False)
    birth = db.Column(db.Date, nullable=False)
    reg_date = db.Column(db.Date, nullable=False)
    permissions = db.relationship('Permissions', secondary='user_permissions',
                                  backref=db.backref('users', lazy='dynamic'))

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)

    def __init__(self, fullname, username, email, password, salt, gender,
                 birth, reg_date):
        self.fullname = fullname
        self.username = username
        self.email = email
        self.password = password
        self.salt = salt
        self.gender = gender
        self.birth = birth
        self.reg_date = reg_date

    def __repr__(self):
        return self.username


class Permissions(db.Model):
    __tablename__ = 'permissions'
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String, nullable=False)

    def __init__(self, level):
        self.level = level
    
    def __repr__(self):
        return self.level


class User_Permissions(db.Model):
    __tablename__ = 'user_permissions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    permission_id = db.Column(db.Integer, db.ForeignKey('permissions.id'),
                              nullable=False)
