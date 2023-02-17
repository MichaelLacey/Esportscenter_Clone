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

    battlefield1 = News(title="Battlefield 2042 players upset over features missing from the beta", image_url='https://static.wixstatic.com/media/ddb70a_619b3c07aa7c4c899373d82385f7118a~mv2.png/v1/fill/w_233,h_132,fp_0.50_0.50,q_95,enc_auto/ddb70a_619b3c07aa7c4c899373d82385f7118a~mv2.png',date='Oct 11, 2021', game_id=2, user_id=1)
    battlefield2 = News(title="Battlefield 2042 Next Patch Features 'Hundreds of changes' ", image_url='https://static.wixstatic.com/media/d09a5f_3b346d975cf54d51be959895aec7945c~mv2.png/v1/fill/w_233,h_132,fp_0.50_0.50,q_95,enc_auto/d09a5f_3b346d975cf54d51be959895aec7945c~mv2.png',date='Mar 31, 2022', game_id=2, user_id=1)
    battlefield3 = News(title="Battlefield 2042 Players Might Be Getting A Refund", image_url='https://static.wixstatic.com/media/bcb21c_3f0fbd88117045a285f529d1543a4e50~mv2.jpeg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/bcb21c_3f0fbd88117045a285f529d1543a4e50~mv2.jpeg',date='Apr 19, 2022', game_id=2, user_id=1)
    battlefield4 = News(title="Battlefield 2042 players upset over features missing from the beta", image_url='https://static.wixstatic.com/media/ddb70a_619b3c07aa7c4c899373d82385f7118a~mv2.png/v1/fill/w_233,h_132,fp_0.50_0.50,q_95,enc_auto/ddb70a_619b3c07aa7c4c899373d82385f7118a~mv2.png',date='Oct 11, 2021', game_id=2, user_id=1)
    
    db.session.add(battlefield1)
    db.session.add(battlefield2)
    db.session.add(battlefield3)
    db.session.add(battlefield4)

    cod1 = News(title="WHAT BATTLEFIELD 2042's DELAY MEANS FOR CALL OF DUTY VANGUARD", image_url='https://static.wixstatic.com/media/ddb70a_4904a9268c584eefb9cd2dc70c895cd6~mv2.png/v1/fill/w_233,h_132,fp_0.50_0.50,q_95,enc_auto/ddb70a_4904a9268c584eefb9cd2dc70c895cd6~mv2.png', date='Sep 27, 2021', game_id=3, user_id=1)
    cod2 = News(title="Here's what 'Call of Duty' 2022 will likely be names", image_url='https://static.wixstatic.com/media/ddb70a_8b26df9ffd994294a1c6a4382610c0e0~mv2.jpg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/ddb70a_8b26df9ffd994294a1c6a4382610c0e0~mv2.jpg', date='Oct 11, 2021', game_id=3, user_id=1)
    cod3 = News(title="Call of Duty Anti-Cheat likely arriving earlier than expected", image_url='https://static.wixstatic.com/media/ddb70a_1906a34e0a6a4e4d8407cf800d491ad7~mv2.jpg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/ddb70a_1906a34e0a6a4e4d8407cf800d491ad7~mv2.jpg', date='Oct 12, 2021', game_id=3, user_id=1)
    cod4 = News(title="Xbox CEO Phil Spencer decides to 'keep Call of Duty on Playstation'", image_url='https://static.wixstatic.com/media/a3e85a_bb6b9071efbb40bab2bf79cb4f711f75~mv2.jpg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/a3e85a_bb6b9071efbb40bab2bf79cb4f711f75~mv2.jpg', date='Jan 21, 2022', game_id=3, user_id=1)
    cod5 = News(title="Microsoft is Acquiring Activision Blizzard in a Record Deal", image_url='https://static.wixstatic.com/media/ddb70a_e01124b787ef4147bdad6e39bd3c92f8~mv2.jpg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/ddb70a_e01124b787ef4147bdad6e39bd3c92f8~mv2.jpg', date='Jan 22, 2022', game_id=3, user_id=1)
    cod6 = News(title="Warzone Season 2 Is Bringing More Than You Expect", image_url='https://static.wixstatic.com/media/d09a5f_dee7cdfec40445b0a31b4da09c04b43e~mv2.jpg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/d09a5f_dee7cdfec40445b0a31b4da09c04b43e~mv2.jpg', date='Feb 7, 2022', game_id=3, user_id=1)
    cod7 = News(title="Call of Duty 2022 Reveal Gets Leaked", image_url='https://static.wixstatic.com/media/bcb21c_2367932ebf1f4421802e7972133ea242~mv2.jpg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/bcb21c_2367932ebf1f4421802e7972133ea242~mv2.jpg', date='Apr 16, 2022', game_id=3, user_id=1)
    cod8 = News(title="Snoop Dogg Drops in Warzone and Vanguard", image_url='https://static.wixstatic.com/media/bcb21c_e5f9bdd6d8874d1e96d1fffc1128d8b1~mv2.jpeg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/bcb21c_e5f9bdd6d8874d1e96d1fffc1128d8b1~mv2.jpeg', date='May 1, 2022', game_id=3, user_id=1)
    cod9 = News(title="Call of Duty Reveals Modern Warfare 2 Logo Intro", image_url='https://static.wixstatic.com/media/bcb21c_7a8bf9f8722d475199a8864c973b87e2~mv2.jpg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/bcb21c_7a8bf9f8722d475199a8864c973b87e2~mv2.jpg_', date='May 1, 2022', game_id=3, user_id=1)
    cod10 = News(title="Elden Ring Surpasses Call of Duty Vanguard in Sales, Best Selling Game of Last Year", image_url='https://static.wixstatic.com/media/bcb21c_0defd35dac4240c6a3b449fc8cf1ec13~mv2.jpg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/bcb21c_0defd35dac4240c6a3b449fc8cf1ec13~mv2.jpg', date='May 15, 2022', game_id=3, user_id=1)
    cod11 = News(title="Modern Warfare 2 Releases October 28!!!", image_url='https://static.wixstatic.com/media/bcb21c_53abedbfab944adb9611e99c23c512d3~mv2.png/v1/fill/w_233,h_132,fp_0.50_0.50,q_95,enc_auto/bcb21c_53abedbfab944adb9611e99c23c512d3~mv2.png', date='Jun 1, 2022', game_id=3, user_id=1)

    db.session.add(cod1)
    db.session.add(cod2)
    db.session.add(cod3)
    db.session.add(cod4)
    db.session.add(cod5)
    db.session.add(cod6)
    db.session.add(cod7)
    db.session.add(cod8)
    db.session.add(cod9)
    db.session.add(cod10)
    db.session.add(cod11)

    fortnite1 = News(title="Epic Games considering a Fortnite movie as it launches entertainment division", image_url='https://static.wixstatic.com/media/ddb70a_fd92dd026122482aac7aa670b9eaac3a~mv2.jpg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/ddb70a_fd92dd026122482aac7aa670b9eaac3a~mv2.jpg', date='Oct 11, 2021', game_id=4, user_id=1)
    fortnite2 = News(title="Fortnite switches it up this season! Faster sprinting, shoulder bashing, and mantling?!", image_url='https://static.wixstatic.com/media/bcb21c_562f5801c1c14b9e95de7a4dad05a991~mv2.jpg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/bcb21c_562f5801c1c14b9e95de7a4dad05a991~mv2.jpg', date='Mar 25, 2022', game_id=4, user_id=1)
    fortnite3 = News(title="Gold Medalist Chloe Kim snows her way into Fortnite", image_url='https://static.wixstatic.com/media/bcb21c_b670a35171694e9795dd738b91f8ac4a~mv2.jpg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/bcb21c_b670a35171694e9795dd738b91f8ac4a~mv2.jpg', date='Mar 28, 2022', game_id=4, user_id=1)
    fortnite4 = News(title="Fortnite's Zero Build mode is made permanent", image_url='https://static.wixstatic.com/media/bcb21c_f6daf5fffc3d47a3aab20ef3add0e28e~mv2.jpg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/bcb21c_f6daf5fffc3d47a3aab20ef3add0e28e~mv2.jpg', date='Mar 29, 2022', game_id=4, user_id=1)
    fortnite5 = News(title="Epic Games Undergo Lawsuit Over 'It's Complicated' Fortnite Emote", image_url='https://static.wixstatic.com/media/a3e85a_443aff8a644047188a96cb7e88ef9432~mv2.jpeg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/a3e85a_443aff8a644047188a96cb7e88ef9432~mv2.jpeg', date='Mar 30, 2022', game_id=4, user_id=1)
    fortnite6 = News(title="Epic Games Is Taking The Next Step Into The Future With Unreal Engine 5", image_url='https://static.wixstatic.com/media/bcb21c_5956576d3c934f7dbbca58fcca82c8b6~mv2.jpeg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/bcb21c_5956576d3c934f7dbbca58fcca82c8b6~mv2.jpeg', date='Apr 6, 2022', game_id=4, user_id=1)

    db.session.add(fortnite1)
    db.session.add(fortnite2)
    db.session.add(fortnite3)
    db.session.add(fortnite4)
    db.session.add(fortnite5)
    db.session.add(fortnite6)

    gta1 = News(title="Rockstar officially reveals GTA trilogy: GTA III, Vice City & San Andreas", image_url='https://static.wixstatic.com/media/ddb70a_4ecc978bcf6f4b14a263ba7e0db413e2~mv2.jpeg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/ddb70a_4ecc978bcf6f4b14a263ba7e0db413e2~mv2.jpeg', date='Oct 11, 2021', game_id=5, user_id=1)
    gta2 = News(title="GTA fans outraged by rumored price of the San Andreas & Vice City remaster", image_url='https://static.wixstatic.com/media/ddb70a_44fad42b018848d3ada63d93b468cc17~mv2.jpg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/ddb70a_44fad42b018848d3ada63d93b468cc17~mv2.jpg', date='Oct 11, 2021', game_id=5, user_id=1)
    gta3 = News(title="GTA 5 And GTA Online Are Going Next Gen, With Some Great New Features!", image_url='https://static.wixstatic.com/media/d09a5f_bd656f6c86ca45fbb75c2a6d77047b22~mv2.png/v1/fill/w_233,h_132,fp_0.50_0.50,q_95,enc_auto/d09a5f_bd656f6c86ca45fbb75c2a6d77047b22~mv2.png', date='Feb 4, 2022', game_id=5, user_id=1)
    gta4 = News(title="Rockstar Set To Release Paid GTA Online Subscription With Major Benefits", image_url='https://static.wixstatic.com/media/d09a5f_35b24f40f6f341579229efa8c56b1a52~mv2.png/v1/fill/w_233,h_132,fp_0.50_0.50,q_95,enc_auto/d09a5f_35b24f40f6f341579229efa8c56b1a52~mv2.png', date='Mar 27, 2022', game_id=5, user_id=1)
    gta5 = News(title="GTA 6 Allegedly Launching in 2024!!!", image_url='https://static.wixstatic.com/media/bcb21c_d9679734a4f446ff9e0b11ad6e7bf1c1~mv2.jpeg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/bcb21c_d9679734a4f446ff9e0b11ad6e7bf1c1~mv2.jpeg', date='May 15, 2022', game_id=5, user_id=1)

    db.session.add(gta1)
    db.session.add(gta2)
    db.session.add(gta3)
    db.session.add(gta4)
    db.session.add(gta5)

    halo1 = News(title="Every Halo Infinite vehicles: Banshee, Mongoose, Warthog and more", image_url='https://static.wixstatic.com/media/ddb70a_094a67be1113407c8df29609899cfbed~mv2.jpg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/ddb70a_094a67be1113407c8df29609899cfbed~mv2.jpg', date='Oct 11, 2021', game_id=5, user_id=1)
    halo2 = News(title="Halo TV Series Premiere Date and Trailer", image_url='https://static.wixstatic.com/media/a3e85a_ed4b265615264dc4b71f90141ccec89a~mv2.jpg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/a3e85a_ed4b265615264dc4b71f90141ccec89a~mv2.jpg', date='Jan 05, 2022', game_id=5, user_id=1)
    halo3 = News(title="Every Halo Infinite vehicles: Banshee, Mongoose, Warthog and more", image_url='https://static.wixstatic.com/media/ddb70a_094a67be1113407c8df29609899cfbed~mv2.jpg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/ddb70a_094a67be1113407c8df29609899cfbed~mv2.jpg', date='Jan 11, 2022', game_id=5, user_id=1)
    halo4 = News(title="Halo TV Series Premiere Date and Trailer", image_url='https://static.wixstatic.com/media/a3e85a_ed4b265615264dc4b71f90141ccec89a~mv2.jpg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/a3e85a_ed4b265615264dc4b71f90141ccec89a~mv2.jpg', date='Jan 30, 2022', game_id=5, user_id=1)

    db.session.add(halo1)
    db.session.add(halo2)
    db.session.add(halo3)
    db.session.add(halo4)

    rainbowsix1 = News(title="Rainbow Six New Update", image_url='https://cdn-ext.fanatical.com/production/product/1280x720/2db0a1c1-3719-4270-b610-a8a1f6c6efb1.jpeg', date='January 21, 2022', game_id=7, user_id=1)
    rainbowsix2 = News(title="Rainbow Six New Update", image_url='https://cdn-ext.fanatical.com/production/product/1280x720/2db0a1c1-3719-4270-b610-a8a1f6c6efb1.jpeg', date='January 23, 2022', game_id=7, user_id=1)
    rainbowsix3 = News(title="Rainbow Six New Update", image_url='https://cdn-ext.fanatical.com/production/product/1280x720/2db0a1c1-3719-4270-b610-a8a1f6c6efb1.jpeg', date='January 25, 2022', game_id=7, user_id=1)
    rainbowsix4 = News(title="Rainbow Six New Update", image_url='https://cdn-ext.fanatical.com/production/product/1280x720/2db0a1c1-3719-4270-b610-a8a1f6c6efb1.jpeg', date='January 27, 2022', game_id=7, user_id=1)
    
    db.session.add(rainbowsix1)
    db.session.add(rainbowsix2)
    db.session.add(rainbowsix3)
    db.session.add(rainbowsix4)

    rocketleague1 = News(title="Rocket League New Update", image_url='https://cdn1.epicgames.com/offer/9773aa1aa54f4f7b80e44bef04986cea/S9_1200x1600-c1bc7211d9e671d7384e2f0247f0f77a', date='Oct 11, 2021', game_id=8, user_id=1)
    rocketleague2 = News(title="Rocket League New Update", image_url='https://cdn1.epicgames.com/offer/9773aa1aa54f4f7b80e44bef04986cea/S9_1200x1600-c1bc7211d9e671d7384e2f0247f0f77a', date='Oct 13, 2021', game_id=8, user_id=1)
    rocketleague3 = News(title="Rocket League New Update", image_url='https://cdn1.epicgames.com/offer/9773aa1aa54f4f7b80e44bef04986cea/S9_1200x1600-c1bc7211d9e671d7384e2f0247f0f77a', date='Oct 14, 2021', game_id=8, user_id=1)
    rocketleague4 = News(title="Rocket League New Update", image_url='https://cdn1.epicgames.com/offer/9773aa1aa54f4f7b80e44bef04986cea/S9_1200x1600-c1bc7211d9e671d7384e2f0247f0f77a', date='Oct 15, 2021', game_id=8, user_id=1)
    
    db.session.add(rocketleague1)
    db.session.add(rocketleague2)
    db.session.add(rocketleague3)
    db.session.add(rocketleague4)

    valorant1 = News(title="Valorant reportedly adding 'skin level selection' feature soon", image_url='https://static.wixstatic.com/media/ddb70a_6753916f52054461acf3d0c8b01068da~mv2.png/v1/fill/w_233,h_132,fp_0.50_0.50,q_95,enc_auto/ddb70a_6753916f52054461acf3d0c8b01068da~mv2.png', date='Oct 11, 2021', game_id=9, user_id=1)
    valorant2 = News(title="Riot considering “block list” to avoid playing with toxic Valorant teammates", image_url='https://static.wixstatic.com/media/ddb70a_76380999a99e4dc19ce5e30484e55226~mv2.jpg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/ddb70a_76380999a99e4dc19ce5e30484e55226~mv2.jpg', date='Oct 12, 2021', game_id=9, user_id=1)
    valorant3 = News(title="Valorant, League of Legends and other Riot games have all come to the Epic Store", image_url='https://static.wixstatic.com/media/ddb70a_33d92ae8131e46d9a47c23f9da79e645~mv2.png/v1/fill/w_233,h_132,fp_0.50_0.50,q_95,enc_auto/ddb70a_33d92ae8131e46d9a47c23f9da79e645~mv2.png', date='Nov 4, 2021', game_id=9, user_id=1)
    valorant4 = News(title="Everything You Need To Know About The New VALORANT Agent: Neon (Ability kit and Ultimate)", image_url='https://static.wixstatic.com/media/ddb70a_0775a946f951457794a0d7754cf11847~mv2.png/v1/fill/w_233,h_132,fp_0.50_0.50,q_95,enc_auto/ddb70a_0775a946f951457794a0d7754cf11847~mv2.png', date='Jan 16, 2022', game_id=9, user_id=1)
    valorant5 = News(title="Streamer IShowSpeed gets banned from Valorant following sexist rant", image_url='https://static.wixstatic.com/media/bcb21c_7ecf5c50b21541418a87e6c72f2e5d8c~mv2.jpg/v1/fill/w_233,h_132,fp_0.50_0.50,q_90,enc_auto/bcb21c_7ecf5c50b21541418a87e6c72f2e5d8c~mv2.jpg', date='Apr 8, 2022', game_id=9, user_id=1)
    valorant6 = News(title="100 Thieves Hiko Has Retired From Competitive Gaming", image_url='https://static.wixstatic.com/media/ddb70a_2eaa853d069e4b02ad949c3201804b9b~mv2.png/v1/fill/w_233,h_132,fp_0.50_0.50,q_95,enc_auto/ddb70a_2eaa853d069e4b02ad949c3201804b9b~mv2.png', date='Apr 12, 2022', game_id=9, user_id=1)

    db.session.add(valorant1)
    db.session.add(valorant2)
    db.session.add(valorant3)
    db.session.add(valorant4)
    db.session.add(valorant5)
    db.session.add(valorant6)
    
    db.session.commit()

def undo_news():
    
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.news RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM news")
        
    db.session.commit()