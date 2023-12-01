from data import data

#data = ["1abc2",
#"pqr3stu8vwx",
#"a1b2c3d4e5f",
#"treb7uchet"]


sum = 0

nums = {d:d for d in '0123456789'}

for entry in data:
    tmp = "".join(c for c in entry if c.isnumeric())
    tmp = tmp[0] + tmp[-1]
    print(tmp)
    sum += int(tmp)

print(sum)