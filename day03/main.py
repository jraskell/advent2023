import re
import time
start_time = time.time()

datafile = open('data.txt', 'r')


data = []

queue = []
for entry in datafile:
    data.append([*entry.strip()])

max_x = len(data[0])
max_y = len(data)

chars = [x for x in "0123456789"]
def IsDigit(param):
    return chars.count(param) != 0
gears = {}
mask = [[' ' for i in range(max_x)] for i in range(max_y)]

y = 0
for entry in data:
    x = 0
    for value in entry:
        if not (value == '.' or value.isdigit()):
            queue.append((x,y))
            if value == '*': 
                mask[y][x] = '*'
                gears[(x,y)] = []
        x += 1
    y += 1
    
#print(chars)

abort = 0
while len(queue) > 0:
    point = queue.pop(0)
    abort += 1
    #if abort > 50: break
    #print(point)
    if IsDigit(data[point[1]][point[0]]):
        #print("digit")
        for x in [-1, 1]:
            i = point[0] + x
            j = point[1]
            
            if i >= max_x or i < 0 or j >= max_y or j < 0: continue
            if(IsDigit(data[j][i]) and not IsDigit(mask[j][i])):
                mask[j][i] = data[j][i]
                queue.append((i,j))
                #print("+", (i,j))
            #else:
                #print("-", (i,j))
    else:
        for x in range(-1,2):
            for y in range(-1,2):
                i = point[0] + x
                j = point[1] + y
                
                if i >= max_x or i < 0 or j >= max_y or j < 0: continue
                if IsDigit(data[j][i]):
                    #print("+", (i,j))
                    mask[j][i] = data[j][i]
                    queue.append((i,j))
                #else:
                    #print("-", (i,j))

sum = 0
gearsum = 0
y = 0
for entry in mask:
    #Part1 sum
    text = ''.join(entry)
    res = re.findall(r"\d+", text)
    for num in res:
        sum += int(num)
    
    #Part2 gears check
    x = 0
    adjacent = False
    num = ""
    loc = (0,0)
    for val in entry:
        if val.isdigit():
            num += val
            #is there an adjacent *?
            for a in range(-1,2):
                for b in range(-1,2):
                    i = x + a
                    j = y + b
                    if i >= max_x or i < 0 or j >= max_y or j < 0: continue
                    #print(i,j)
                    if mask[j][i] == '*':
                        adjacent = True
                        loc = (i,j)
                        #print(loc)
        elif len(num) > 0:
            if adjacent:
                gears[loc].append(int(num))
            num = ""
            adjacent = False
        x += 1
        if x >= max_x:
            #end of line.  Check for number to process
            if len(num) > 0:
                if adjacent:
                    gears[loc].append(int(num))
                num = ""
                adjacent = False
    print(text)
    y +=1

for entry in gears:
    
    if len(gears[entry]) == 2:
        print(entry, gears[entry][0] , gears[entry][1])
        gearsum += gears[entry][0] * gears[entry][1]
print(sum)
print(gearsum)
print("--- %s seconds ---" % (time.time() - start_time))