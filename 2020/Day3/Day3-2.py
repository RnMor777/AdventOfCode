f = open("Day3.txt", "r")
arr = f.readlines()
total = 1
length = len(arr[0])-1

for j in [1,2,3,5,7]:
    count, x = 0, 0
    k = j if j!=2 else 1
    for i in range(len(arr)):
        if (j==2 and i%2==1):
            continue
        count += 1 if arr[i][x] == "#" else 0
        x = (x+k)%length
    total*=count
print (total)
