from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(64))

    def __self(self):
        return f'<User>'
