import numpy as np

def part1 (data):
    # iterate over all the rows and columns
    arr1, arr2, arr3, arr4 = [], [], [], []
    for i, row in enumerate(data):
        row = list(map(int, row.strip()))
        col = [int(data[j][i]) for j in range(len(data))]

        # stores 1s and 0s in arrays if the trees are visible or not
        arr1.append([1 if max(row[0:j],default=-1)<row[j] else 0 for j in range(len(row))])
        arr2.append([1 if max(row[j+1:],default=-1)<row[j] else 0 for j in range(len(row))])
        arr3.append([1 if max(col[0:j],default=-1)<col[j] else 0 for j in range(len(col))])
        arr4.append([1 if max(col[j+1:],default=-1)<col[j] else 0 for j in range(len(col))])

    # converts to np arrays
    a = np.array(arr1)
    b = np.array(arr2)
    c = np.array(arr3)
    d = np.array(arr4)

    # ors the np arrays together to get final visibility bool value
    outarr = (a + b + c.T + d.T).astype(bool)

    # returns all true values
    return np.count_nonzero(outarr)

def calcVis (data, i, j, xupdate, yupdate):
    # set variables
    currMax = 0
    tree = int(data[i][j])
    x = i + xupdate
    y = j + yupdate

    # go until out or range of hit a taller tree
    while (len(data) > x >= 0 and len(data) > y >= 0):
        currMax += 1
        if tree <= int(data[x][y]):
            break

        x += xupdate
        y += yupdate

    # return visibility score
    return currMax

def part2 (data):
    # loop through all trees and find visibility rating for each
    visMax = 0
    for i, row in enumerate(data):
        for j in range(len(row.strip())):
            currMax = 1
            currMax *= calcVis (data, i, j, -1, 0)
            currMax *= calcVis (data, i, j, 1, 0)
            currMax *= calcVis (data, i, j, 0, -1)
            currMax *= calcVis (data, i, j, 0, 1)

            visMax = max(currMax, visMax)

    # return highest score
    return visMax

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.readlines()

        print ("Part 1:", part1(data))
        print ("Part 2:", part2(data))
