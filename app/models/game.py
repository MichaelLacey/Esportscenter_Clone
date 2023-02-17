from .db import db, environment, SCHEMA, add_prefix_for_prod

class Game(db.Model):

    
    __tablename__ = 'games'


    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }