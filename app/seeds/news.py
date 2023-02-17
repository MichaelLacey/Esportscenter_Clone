from app.models import db, News, environment, SCHEMA

def seed_news():

    apex1 = News(title='APEX PLAYERS WANT TO CANCEL SEASON 11', image_url='https://static.wixstatic.com/media/ddb70a_15e91a4bd238449d85de03c5c3f83fc2~mv2.jpg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/ddb70a_15e91a4bd238449d85de03c5c3f83fc2~mv2.jpg', date='Sep 27, 2021', game_id=1, user_id=1)    
    apex2 = News(title='When is Apex Legends Season 11? Start date, Season 10 end date, more', image_url='https://static.wixstatic.com/media/ddb70a_b609ba211c9d40e3b51300d732a51038~mv2.jpg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/ddb70a_b609ba211c9d40e3b51300d732a51038~mv2.jpg', date='Sep 27, 2021', game_id=1, user_id=1)    
    apex3 = News(title="How to watch today's ALGS Pro League qualifiers", image_url='https://static.wixstatic.com/media/ddb70a_4e3c5d1ee36e4bc0b5d77834dd5a9b0f~mv2.jpg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/ddb70a_4e3c5d1ee36e4bc0b5d77834dd5a9b0f~mv2.jpg', date='Sep 27, 2021', game_id=1, user_id=1)    
    apex4 = News(title='Apex Legends Mobile has a pack system that needs to come to the main game', image_url='https://static.wixstatic.com/media/ddb70a_031b91a00b2e40c799a481a57d2770e6~mv2.jpg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/ddb70a_031b91a00b2e40c799a481a57d2770e6~mv2.jpg', date='Oct 11, 2021', game_id=1, user_id=1)    
    apex5 = News(title='Apex Legends players plan to boycott Halloween even in hopes of a "health" update', image_url='https://static.wixstatic.com/media/ddb70a_bd6c313f281643a893096bcaa0e05b2b~mv2.jpg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/ddb70a_bd6c313f281643a893096bcaa0e05b2b~mv2.jpg', date='Oct 12, 2021', game_id=1, user_id=1)    
    apex6 = News(title='Apex Legends Leaker shows possible Crypto Buff in Season 12', image_url='https://static.wixstatic.com/media/a3e85a_b17fef0002494d949781ff84157a4eac~mv2.png/v1/fill/w_233,h_132,fp_0.50_0.50,q_95,enc_auto/a3e85a_b17fef0002494d949781ff84157a4eac~mv2.png', date='Jan 31, 2022', game_id=1, user_id=1)    
    apex7 = News(title="Apex Legend's new legend 'Mad Maggie' will be a top tier legend", image_url='https://static.wixstatic.com/media/d09a5f_9123ecac7cab41cca94e6197316c6a70~mv2.jpg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/d09a5f_9123ecac7cab41cca94e6197316c6a70~mv2.jpg', date='Feb 7, 2022', game_id=1, user_id=1)    
    apex8 = News(title='Apex Legends Finally Adds Next-gen Console Update', image_url='https://static.wixstatic.com/media/ddb70a_0cce53986ce649eea9b87bb55f290bcf~mv2.png/v1/fill/w_233,h_132,fp_0.50_0.50,q_95,enc_auto/ddb70a_0cce53986ce649eea9b87bb55f290bcf~mv2.png', date='Mar 29, 2022', game_id=1, user_id=1)    

    db.session.add(apex1)
    db.session.add(apex2)
    db.session.add(apex3)
    db.session.add(apex4)
    db.session.add(apex5)
    db.session.add(apex6)
    db.session.add(apex7)
    db.session.add(apex8)
    db.session.commit()

def undo_news():
    
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.news RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM news")
        
    db.session.commit()