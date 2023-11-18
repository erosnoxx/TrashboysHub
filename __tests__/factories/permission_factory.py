import factory   # type: ignore
from app.extensions import db
from app.models import Permissions


class PermissionFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Permissions
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"

    level = factory.Sequence(lambda n: f'Permission {n}')