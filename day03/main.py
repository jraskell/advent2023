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

mask = [[' ' for i in range(max_x)] for i in range(max_y)]
x = 0
y = 0
for entry in data:
    x = 0
    for value in entry:
        if not (value == '.' or value.isdigit()):
            queue.append((x,y))
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
for entry in mask:
    text = ''.join(entry)
    res = re.findall(r"\d+", text)
    for num in res:
        sum += int(num)
    #print(text)

print(sum)
print("--- %s seconds ---" % (time.time() - start_time))