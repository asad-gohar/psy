try:
    import os

    from flask import Flask, render_template, request, redirect, url_for, session, jsonify, json, g, send_file
    from flask_sqlalchemy import SQLAlchemy
    from sqlalchemy import and_
    from sqlalchemy import or_
    import random


    print("found")
except:
    print("not found d")

print("aaa")
myApp = Flask(__name__)
myApp.secret_key = os.urandom(24)
project_dir = os.path.abspath(os.path.dirname(__file__))
print("=" * 100)

database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))
myApp.config["SQLALCHEMY_DATABASE_URI"] = database_file
myApp.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(myApp)


class MCQS(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    answer = db.Column(db.String(40), unique=False, nullable=False)
    question = db.Column(db.String(40), unique=False, nullable=False)



db.create_all()
@myApp.route('/')
def home():
    data=MCQS.query.all()
    return render_template("index.html" ,data=data)


if __name__ == "__main__":
    myApp.run(debug=True)