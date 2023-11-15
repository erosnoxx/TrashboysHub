from app import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    published = db.Column(db.Boolean, default=False)
    text = db.Column(db.String, nullable=False)

    def __init__(self, title, published, text):
        self.title = title
        self.published = published
        self.text = text


    def __repr__(self):
        return self.title