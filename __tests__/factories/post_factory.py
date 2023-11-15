import factory
from faker import Faker
from app.extensions import db
from app.models import Post

faker = Faker()


class PostFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Post
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"
    
    title = faker.paragraph()
    text = faker.text()
    published = True
    category_id = 'Something'