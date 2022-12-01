f = open("Day1.txt", "r")
arr = list(map(int, f.readlines()))
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if (arr[i]+arr[j]==2020):
            print (arr[i]*arr[j])
            break
