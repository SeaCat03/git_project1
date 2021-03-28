import sqlalchemy


def config(db):
    class User(db.Model):
        def __init__(self, id, name, email, phone_number):
            self.id = id
            self.name = name
            self. email = email
            self.phone_number = phone_number
        person_id = sqlalchemy.Column(
            sqlalchemy.Integer, primary_key=True, autoincrement=True)
        person_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
        person_email = sqlalchemy.Column(sqlalchemy.String, nullable=True)
        person_id_in_vk = sqlalchemy.Column(sqlalchemy.Integer)
        person_phone_number = sqlalchemy.Column(
            sqlalchemy.Integer, nullable=True)
    return User
