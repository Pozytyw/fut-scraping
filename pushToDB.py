import os
import test
import json
# connect
db = test.connect_to_database()
# create cursor
cursor = db.cursor(dictionary=True)
# path to folder
path = "E:\\python projects\\fut scraping\\players"

for filename in os.listdir(path):
    with open(os.path.join(path, filename), 'r') as f:
        player = json.load(f)
        nation_id = test.get_nation(cursor, player['nationality'])
        league_id = test.leagueExist(cursor, player['league'])
        club_id = test.clubsExist(cursor,  player['club'])
        test.newPlayer(cursor, player['name'], nation_id, club_id, league_id, player['file_name'], player['rating'],
                       player['position'], player['rare'])
        print("added new player : " + player['name'])
db.commit()
cursor.close()
