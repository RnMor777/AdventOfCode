f = open("Day2.txt", "r")
arr = f.readlines()
count = 0
for i in arr:
    bounds, char, pss = i.split(' ')
    res = list(pss).count(char[0])
    b1, b2 = bounds.split('-')
    if (res>=int(b1) and res<=int(b2)):
        count += 1
print (count)
