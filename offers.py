import sqlalchemy

def config_offer(db):
    class Offer(db.Model):
        def __init__(self, id, always_cost, actually_cost, about, can_be):
            self.id = id
            self.actually_cost = actually_cost
            self.always_cost = always_cost
            self. about = about
            self.can_be = can_be
        offer_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
        actually_cost = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
        always_cost = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
        about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
        can_be = sqlalchemy.Column(sqlalchemy.TEXT)
    return Offer