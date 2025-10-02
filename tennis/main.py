import csv
import os
import numpy as np

directory = os.path.dirname(os.path.abspath(__file__))
players = np.array([['Player', 'Wins', 'Matches']])
count = 1
with open(directory + '/data/atp_no_spaces.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=",")
    next(data)
    for row in data:
        if row[7] in players[:]:
            index = np.where(players == row[7])[0]
            thing = players[index]
            value = int(thing[0, 2])
            thing[0, 2] = value+1
            players[index] = thing
            if row[7] == row[9] in players[:]:
                index = np.where(players == row[7])[0]
                thing = players[index]
                value = int(thing[0, 1])
                thing[0, 1] = value+1
                players[index] = thing
        else:
            if row[7] == row[9] in players[:]:
                players = np.vstack([players, [row[7], 1, 1]])
            else:
                players = np.vstack([players, [row[7], 0, 1]])
        if row[8] in players[:]:
            index = np.where(players == row[8])[0]
            thing = players[index]
            value = int(thing[0, 2])
            thing[0, 2] = value+1
            players[index] = thing
            if row[8] == row[9] in players[:]:
                index = np.where(players == row[8])[0]
                thing = players[index]
                value = int(thing[0, 1])
                thing[0, 1] = value+1
                players[index] = thing
        else:
            if row[8] == row[9] in players[:]:
                players = np.vstack([players, [row[8], 1, 1]])
            else:
                players = np.vstack([players, [row[8], 0, 1]])
with open(directory + "/data/matchWL.csv", 'w', newline='') as csvfile:
    newcsv = csv.writer(csvfile, delimiter=',')
    for row in players:
        newcsv.writerow(row)