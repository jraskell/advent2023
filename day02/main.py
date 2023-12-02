import re

datafile = open('data.txt', 'r')
data = datafile.readlines()

results = {}

for entry in data:
    first = entry.split(":")
    index = int(first[0].strip("Game "))
    games = first[1].strip().split(";")
    
    hands = []
    for hand in games:
        pairdict = {"red": 0, "green": 0, "blue": 0}
        pairs = hand.strip().split(",")
        for pair in pairs:
            items = pair.strip().split(" ")
            pairdict[items[1]] = int(items[0])
        hands.append(pairdict)
    results[index] = hands


red = 12
green = 13
blue = 14
sum = 0
power = 0

for entry in results:
    possible = True
    maxred = 0
    maxgreen = 0
    maxblue = 0

    for dict in results[entry]:
        if possible:
            possible = dict["red"] <= red and dict["green"] <= green and dict["blue"] <= blue
        maxred = maxred if maxred > dict["red"] else dict["red"]
        maxgreen = maxgreen if maxgreen > dict["green"] else dict["green"]
        maxblue = maxblue if maxblue > dict["blue"] else dict["blue"]

    power += maxred * maxgreen * maxblue
    print(maxred, maxgreen, maxblue, maxred * maxgreen * maxblue)    
    if possible:
        print(entry)
        sum += entry

print(sum)
print(power)