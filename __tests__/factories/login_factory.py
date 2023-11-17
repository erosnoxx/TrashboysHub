import factory
from app.extensions import db
from app.models import User
from datetime import datetime


class LoginFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"
    
    fullname = 'eros gabriel vieira'
    username = 'erosnox'
    email = 'eros@gmail.com'
    password = 'prachedes'
    salt = '123'
    gender = 'male'
    birth = datetime.strptime('11/10/2001', '%d/%m/%Y')
    reg_date = datetime.strptime('10/10/2001', '%d/%m/%Y')
