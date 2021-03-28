import sqlalchemy


def config(db):
    class Order(db.Model):
        def __init__(self, status, who_id, when, what_offer):
            self.who_id = who_id
            self.status = status
            self. when = when
            self.what_offer = what_offer
        status = sqlalchemy.Column(sqlalchemy.BOOLEAN)
        who_id = sqlalchemy.Column(
            sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
        when = sqlalchemy.Column(sqlalchemy.DATE)
        what_offer = sqlalchemy.Column(
            sqlalchemy.String, sqlalchemy.ForeignKey("offers.id"))
    return Order
