from app.models import db, Game, environment, SCHEMA

def seed_games():

    apex_legends = Game(name='Apex Legends')
    battlefield = Game(name='Battlefield')
    call_of_duty = Game(name='Call of Duty')
    fortnite = Game(name='Fortnite')
    gta = Game(name='GTA')
    halo = Game(name='HALO')
    rainbow6 = Game(name='Rainbow Six')
    rocket_league = Game(name='Rocket League')
    valorant = Game(name='Valorant')

    db.session.add(apex_legends)
    db.session.add(battlefield)
    db.session.add(call_of_duty)
    db.session.add(fortnite)
    db.session.add(gta)
    db.session.add(halo)
    db.session.add(rainbow6)
    db.session.add(rocket_league)
    db.session.add(valorant)
    db.session.commit()


def undo_games():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.games RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM games")
        
    db.session.commit()
