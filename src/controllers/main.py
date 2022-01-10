from flask.json import jsonify
import psycopg
from src.models.users import Users
from src.models.roles import Roles
from src.models.claims import Claims


def topic1():

    db_link = 'postgres://postgres:root123@localhost:5432/shipay'
    connection = psycopg.connect(conninfo=db_link)

    query = connection.execute('select * from users')
    list_data = query.fetchall()
    print(list_data)

    return jsonify(list_data)


def topic2():

    users = Users.query.all()

    if not users:
        return {"error": "no data found"}, 404
    else:
        return jsonify(users), 200


def topic3():

    roles = Roles.query.all()

    if not roles:
        return {"error": "no data found"}, 404
    else:
        return jsonify(roles), 200

