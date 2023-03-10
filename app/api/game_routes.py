from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Game

game_routes = Blueprint('games', __name__)

@game_routes.route('')
def all_games():
    """
    Query for all games and return them in a dictionary
    """

    games = Game.query.all()
    return { 'games': [ game.to_dict() for game in games ] }
    # return [ game.to_dict() for game in games ] 

@game_routes.route('/<int:game_id>')
def one_game(game_id):
    """
    Query for one game by gameId in the url
    """
    return Game.query.get(game_id).to_dict()