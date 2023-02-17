from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import News

news_routes = Blueprint('news', __name__)

@news_routes.route('/<int:game_id>')
def news_for_game(game_id):
    """
    Query for all the news/articles in a particular game by gameId
    """

    news = News.query.filter(News.game_id == game_id).order_by(News.id.desc())
    return { 'News': [ news.to_dict() for news in news ] }
    # return [ news.to_dict() for news in news ] 