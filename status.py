def config(db):
    class status(db.Model):
        def __init__(self, num, status, post_id):
            self.num = num
            self.status = status
            self.post_id = post_id
        num = db.Column(db.String(100), primary_key=True)
        status = db.Column(db.String(500))
        post_id = db.Column(db.String(500))
    return status
