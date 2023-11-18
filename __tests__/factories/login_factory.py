# login_factory.py
import factory
from app.extensions import db
from app.models import User
from .permission_factory import PermissionFactory
from faker import Faker


class LoginFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"

    @factory.post_generation
    def permissions(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for permission in extracted:
                self.permissions.append(permission)
        else:
            default_permissions = [PermissionFactory.create() for _ in range(2)]
            self.permissions.extend(default_permissions)

    fullname = Faker().name()
    username = Faker().user_name()
    email = Faker().email()
    password = Faker().password()
    salt = Faker().random_int(min=1, max=10)
    gender = Faker().random_element(elements=('male', 'female'))
    birth = Faker().date_of_birth(minimum_age=18, maximum_age=90)
    reg_date = Faker().date_this_decade(before_today=True, after_today=False)
