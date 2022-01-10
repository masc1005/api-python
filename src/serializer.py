from flask_marshmallow import Marshmallow
from src.models.users import Users
from src.models.roles import Roles
from src.models.claims import Claims

ma = Marshmallow()


def config(app):
    ma.init_app(app)


class userSchema(ma.Schema):
    class Meta:
        model = Users


class rolesSchema(ma.Schema):
    class Meta:
        model = Roles


class claimsSchema(ma.Schema):
    class Mete:
        model = Claims
