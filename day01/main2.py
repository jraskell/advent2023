#from data import data
import os
#data = ["1abc2",
#"pqr3stu8vwx",
#"a1b2c3d4e5f",
#"treb7uchet"]
"""
data = ["two1nine",
"eightwothree",
"abcone2threexyz",
"xtwone3four",
"4nineeightseven2",
"zoneight234",
"7pqrstsixteen"
]
"""
print(os.getcwd())
datafile = open('day01/data.txt', 'r')
data = datafile.readlines()

sum = 0

words = {
    "one":'1',
    "two":'2',
    "three":'3',
    "four":'4',
    "five":'5',
    "six":'6',
    "seven":'7',
    "eight":'8',
    "nine":'9',
}

for entry in data:
    print(entry)
    i = 0
    while i < len(entry):
        for key in words:
            if entry.startswith(key, i):
                entry = entry[:i] + words[key] + entry[i+1:]
        i += 1
    print(entry)
    tmp = "".join(c for c in entry if c.isnumeric())
    tmp = tmp[0] + tmp[-1]
    print(tmp)
    sum += int(tmp)    

print("sum: " + str(sum))