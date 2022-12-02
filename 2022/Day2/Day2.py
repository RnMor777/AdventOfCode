# A - Rock
# B - Paper
# C - Scissors

def procScore (opp, you):
    tot = ord(you) - ord('A') + 1

    if opp == you:
        tot += 3
    elif opp == 'A' and you == 'B':
        tot += 6
    elif opp == 'A' and you == 'C':
        tot += 0
    elif opp == 'B' and you == 'A':
        tot += 0
    elif opp == 'B' and you == 'C':
        tot += 6
    elif opp == 'C' and you == 'A':
        tot += 6
    elif opp == 'C' and you == 'B':
        tot += 0

    return tot

def day1 (data):
    mapping = ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
    sums = [0 for i in range(6)]

    # loop through all data and permutations
    for i in data:
        x = i.strip()
        opp, you = x.split(' ')
        for j in range(6):
            mapped = mapping[j][ord(you) - ord('X')]
            sums[j] += procScore(opp, mapped)

    return max(sums)

def day2 (data):
    tot = 0

    for i in data:
        x = i.strip()
        opp, you = x.split(' ')

        # You need to lose
        if you == "X":
            if opp == "A":
                tot += procScore(opp, "C")
            elif opp == "B":
                tot += procScore(opp, "A")
            else:
                tot += procScore(opp, "B")

        # You need to tie
        elif you == "Y":
            tot += procScore(opp, opp)

        # You need to win
        elif you == "Z":
            if opp == "A":
                tot += procScore(opp, "B")
            elif opp == "B":
                tot += procScore(opp, "C")
            else:
                tot += procScore(opp, "A")

    return tot


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.readlines()

        print("Day 1:", day1(data))
        print("Day 2:", day2(data))
