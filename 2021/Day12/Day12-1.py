def calcPath (node, count, hops):
    if (node == "end"):
        print (hops)
        return count+1

    for i in paths[node]:
        if (i=="start"):
            continue
        if (i.islower() and i in hops.split(',')):
            continue
        count = calcPath (i, count, hops+i+",")
    return count

f = open("Day12.txt", "r")
arr = f.readlines()
paths = {}
count = 0

for i in arr:
    start, end = i.strip().split('-')
    if (start in paths):
        paths[start].append(end)
    else:
        paths[start] = [end]

    if (end in paths):
        paths[end].append(start)
    else:
        paths[end] = [start]

print(calcPath ("start", 0, ""))
