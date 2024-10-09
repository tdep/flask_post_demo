import flask
from flask import (Flask)
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "blorpland"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    age = db.Column(db.Integer)


def save(data):
    db.session.add(data)
    db.session.commit()
    return data


@app.route('/users/create_user', methods=['POST'])
def create_user():
    data = flask.request.get_json()
    name = data["name"]
    age = data["age"]

    if not name:
        return flask.jsonify(message={'Error': 'Name cannot be empty'}, status=400), 400
    elif not age:
        return flask.jsonify(message={'Error': 'Age cannot be empty'}, status=400), 400
    elif len(name) > 32:
        return flask.jsonify(message={'Error': 'Name cannot be longer than 32 characters.'}, status=400), 400
    elif type(age) != int:
        return flask.jsonify(message={'Error': 'Age must be a number'}, satus=400), 400
    elif age <= 15:
        return flask.jsonify(message={'Error': 'Age must be 16 or older'}, status=400), 400
    else:
        user = User(name=name, age=age)
        save(user)
        return flask.jsonify(data, 201), 201


with app.app_context():
    db.drop_all()
    db.create_all()