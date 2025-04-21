#!/usr/bin/python3
floor = ['B', '1', '2', '3', '4', '5', '6', '7', '8']
wing = ['N', 'S', 'E', 'W']

room_id = 1
for f in floor:
    for w in wing:
        for r in range(1, 21):
            room = str(f) + str(w) + str(r)
            print("INSERT INTO Rooms ( room_id, room ) VALUES ( " + str(room_id) + ", '" + str(room) + "' );")
            room_id += 1
