from app import db

class Data(db.Model):
    __tablename__ = 'dados'
    id = db.Column(db.Integer, primary_key=True)
    char_num = db.Column(db.Integer)
    timedelta = db.Column(db.Float)
    age_id = db.Column(db.Integer)

    def __repr__(self):
        return "<Data {}>".format(self.id)