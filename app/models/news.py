from .db import db, environment, SCHEMA, add_prefix_for_prod

class News(db.Model):

    
    __tablename__ = 'news'


    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}


    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    # description = db.Column(db.text, nullable=False)
    image_url = db.Column(db.Text)
    date = db.Column(db.String(45) )
    game_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('games.id')))
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))


    users_to_game = db.relationship('User', backref='news')
    news_to_game = db.relationship('Game', backref='news')

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "date": self.date,
            "image_url": self.image_url,
            "game_id": self.game_id
        }