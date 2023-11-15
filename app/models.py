from app.extensions import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    published = db.Column(db.Boolean, default=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    text = db.Column(db.String, nullable=False)


    def __init__(self, title, published, text, category_id):
        self.title = title
        self.published = published
        self.text = text
        self.category_id = category_id


    def __repr__(self):
        return self.title
    

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    posts = db.relationship('Post', backref='category', uselist=True)



    def __init__(self, name):
        self.name = name


    def __repr__(self):
        return self.name