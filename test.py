import mysql.connector
from mysql.connector import errorcode


def connect_to_database():
    # placeholders, default values
    host = "127.0.0.1"
    port = "3306"
    user = "root"
    password = "root"
    database = "cyganeria"

    database = mysql.connector.connect(
        host=host,
        user=user,
        passwd=password,
        port=port,
        database=database
    )
    print("Connection successful")

    return database


def get_id_if_not_exist_add(cursor, table_name, column_name, value):
    try:
        # try to get id
        query = "select ID from " + table_name + " where " + column_name + " like \"" + value + "\";"
        print("execute: " + query)
        cursor.execute(query)
    except mysql.connector.Error as err:
        # connection error
        print("Something went wrong: {}".format(err))
        exit(1)

    x = cursor.fetchall()
    if cursor.rowcount == 0:
        # value not in table
        # insert new row
        print("new row")
        query = "insert into " + table_name + "(" + column_name + ") values(\"" + value + "\");"
        print("execute: " + query)
        cursor.execute(query)
        return cursor.lastrowid
    else:
        # value in table
        return x[0]['ID']


# nation test
def get_nation(cursor, nation):
    return get_id_if_not_exist_add(cursor, "nations", "nation", nation)


# league test
def leagueExist(cursor, league):
    return get_id_if_not_exist_add(cursor, "leagues", "league", league)


# clubs test
def clubsExist(cursor, club):
    return get_id_if_not_exist_add(cursor, "clubs", "club", club)


# new player row
def newPlayer(cursor, name, national_id, club_id, league_id, file_name, rating, position, rare):
    query = "insert into players(name, national_id, club_id, league_id, file_name, rating, position, rare) " \
            "values(\"" + name + "\", " + str(national_id) + ", " + str(club_id) + ", " + str(league_id) + ", \"" +\
            file_name + "\", " + rating + ", \"" + position + "\", \"" + rare + "\");"
    print("execute: " + query)
    cursor.execute(query)
