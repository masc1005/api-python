from flask import Flask


def init_app(app: Flask):

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:root123@localhost:5432/shipay'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
