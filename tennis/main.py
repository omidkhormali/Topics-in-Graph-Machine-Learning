import csv
import os
import numpy as np

directory = os.path.dirname(os.path.abspath(__file__))
players = np.array([['Player', 'Wins', 'Matches']])
with open(directory + '/data/atp_fixed.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=",")
    next(data)
    for row in data:
        if row[9] in players[:]:
            index = np.where(players == row[9])[0]
            thing = players[index]
            value = int(thing[0, 2])
            thing[0, 2] = value+1
            players[index] = thing
            if row[9] == row[11] in players[:]:
                value = int(thing[0, 1])
                thing[0, 1] = value+1
                players[index] = thing
        else:
            if row[9] == row[11]:
                players = np.vstack([players, [row[9], 1, 1]])
            else:
                players = np.vstack([players, [row[9], 0, 1]])
        if row[10] in players[:]:
            index = np.where(players == row[10])[0]
            thing = players[index]
            value = int(thing[0, 2])
            thing[0, 2] = value+1
            players[index] = thing
            if row[10] == row[11]:
                value = int(thing[0, 1])
                thing[0, 1] = value+1
                players[index] = thing
        else:
            if row[10] == row[11]:
                players = np.vstack([players, [row[10], 1, 1]])
            else:
                players = np.vstack([players, [row[10], 0, 1]])

print("Writing to the CSV...")
with open(directory + "/data/matchWL.csv", 'w', newline='') as csvfile:
    newcsv = csv.writer(csvfile, delimiter=',')
    for row in players:
        if row[0] == "Player":
            ratio = "W/L Ratio"
        else:
            ratio = float(row[1])/float(row[2])
        row = np.append(row, ratio)
        newcsv.writerow(row)
print("Part 1 done!\n")

# FOR EACH YEAR

finalYr = np.empty((0, 4))
playersYr = np.array([['Year', 'Player', 'Wins', 'Matches']])
year = 1999
with open(directory + '/data/atp_fixed.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=",")
    next(data)
    for row in data:
        if str(row[1]) != str(year):
            if int(row[1]) > year:
                year = year + 1
            else:
                year = year - 1
            finalYr = np.vstack([finalYr, playersYr])
            playersYr = np.empty((0, 4))
        if row[9] in playersYr[:]:
            index = np.where(playersYr == row[9])[0]
            thing = playersYr[index]
            value = int(thing[0, 3])
            thing[0, 3] = value+1
            playersYr[index] = thing
            if row[9] == row[11]:
                value = int(thing[0, 2])
                thing[0, 2] = value+1
                playersYr[index] = thing
        else:
            if row[9] == row[11]:
                playersYr = np.vstack([playersYr, [year, row[9], 1, 1]])
            else:
                playersYr = np.vstack([playersYr, [year, row[9], 0, 1]])
        if row[10] in playersYr[:]:
            index = np.where(playersYr == row[10])[0]
            thing = playersYr[index]
            value = int(thing[0, 3])
            thing[0, 3] = value+1
            playersYr[index] = thing
            if row[10] == row[11]:
                value = int(thing[0, 2])
                thing[0, 2] = value+1
                playersYr[index] = thing
        else:
            if row[10] == row[11]:
                playersYr = np.vstack([playersYr, [year, row[10], 1, 1]])
            else:
                playersYr = np.vstack([playersYr, [year, row[10], 0, 1]])
    finalYr = np.vstack([finalYr, playersYr])
print("Writing to CSV...")
with open(directory + "/data/matchWLYear.csv", 'w', newline='') as csvfile:
    newcsv = csv.writer(csvfile, delimiter=',')
    for row in finalYr:
        newcsv.writerow(row)
print("Part 2 done!\n")

data = np.empty((0, 6))
for row in finalYr:
    index = np.where(players == row[1])[0]
    thing = players[index]
    if str(thing[0, 1]) == "Wins":    
        value1 = "T Wins"
        value2 = "T Sets"
    else:
        value1 = int(thing[0, 1])
        value2 = int(thing[0, 2])
    data = np.vstack([data, [row[0], row[1], row[2], row[3], value1, value2]])
dataGet = np.empty((0, 9))
with open(directory + "/data/tvalue.csv", 'w', newline='') as csvfile:
    newcsv = csv.writer(csvfile, delimiter=',')
    for row in data:
        if row[0] == "Year":
            rate = "Wins Rate"
            matches = "Matches Rate"
            t = "t Value"
        else:
            if int(row[4]) == 0:
                rate = 0
            else:
                rate = float(row[2])/float(row[4])
            matches = float(row[3])/float(row[5])
            t = rate * matches
        dataSet = np.array([row[0], row[1], row[2], row[3], row[4], row[5], rate, matches, t])
        dataGet = np.vstack([dataGet, dataSet])
        newcsv.writerow(dataSet)
print("Part 3 done!\n")

data = np.empty((0, 6))
for row in dataGet:
    if row[0] == "Year":
        data = np.vstack([data, [row[1], row[0], row[8], "Win Rate", "Weight", "g(v)"]])
    else:
        if row[1] in data[:]: 
            index = np.where(data == row[1])[0]
            thing = data[index]
            value = float(thing[0, 2])
            if(value < float(row[8])):
                weight = (float(1)/(1+np.exp(0.5*(19-(int(row[0])-2000)))))/(float(1)/(1+np.exp(0.5*(19-25))))
                g = rate*weight
                data[index] = [row[1], row[0], row[8], rate, weight, g]
        else:
            rate = float(row[4])/float(row[5])
            weight = (float(1)/(1+np.exp(0.5*(2019-int(row[0])))))/(float(1)/(1+np.exp(0.5*(-6))))
            g = rate*weight
            data = np.vstack([data, [row[1], row[0], row[8], rate, weight, g]])
with open(directory + "/data/g-function.csv", 'w', newline='') as csvfile:
    newcsv = csv.writer(csvfile, delimiter=',')
    for row in data:
        newcsv.writerow(row)
print("Part 4 done!\n")