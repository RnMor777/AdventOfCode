f = open("Day2.txt", "r")
arr = f.readlines()
count = 0
for i in arr:
    bounds, char, pss = i.split(' ')
    b1, b2 = bounds.split('-')
    char = char[0]
    if (((1 if pss[int(b1)-1]==char else 0) + (1 if pss[int(b2)-1]==char else 0))%2==1):
        count += 1
print (count)
