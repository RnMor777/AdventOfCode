f = open("Day3.txt", "r")
arr = f.readlines()
x = 0
count = 0
length = len(arr[0])-1

for i in range(len(arr)):
    count += 1 if arr[i][x] == "#" else 0
    x = (x+3)%length
print (count)
