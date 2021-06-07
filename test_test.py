import test


#connect
db = test.connect_to_database()

#create cursor
cursor = db.cursor(dictionary=True)
print("test")
id1 = test.get_id_if_not_exist_add(cursor, "nations", "nation", "x")
id2 = test.get_id_if_not_exist_add(cursor, "nations", "nation", "x")
print(id1, id2)
db.commit()
cursor.close()