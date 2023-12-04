import re

datafile = open("data.txt", 'r')
data = datafile.readlines()

cards = {}
for entry in data:
    vals = entry.split(':')
    cardnum = re.search(r"\d+", vals[0])
    cards[int(cardnum.group())] = [1, vals[1].split('|')]

sum = 0
for key in cards:
    count = cards[key][0]
    winners = cards[key][1][0].split()
    nums = cards[key][1][1].split()
    
    
    val = 0
    for winner in winners:
        if nums.count(winner) > 0: 
            val += 1
    
    for x in range(1,val+1):
        if key + x > len(cards):break
        cards[key+x][0] += count
    
    sum += count
    print(key, val, count)

print(sum)