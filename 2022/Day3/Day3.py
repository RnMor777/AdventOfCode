def priority (res):
    if res.isupper():
        return ord(res) - ord('A') + 27
    else:
        return ord(res) - ord('a') + 1

def part1 (data):
    tot = 0

    for x in data:
        x = x.strip()
        length = len(x) // 2
        bin1, bin2 = x[:length], x[length:]

        res =  list(set(bin1).intersection(set(bin2)))[0]
        tot += priority(res)

    return tot

def part2 (data):
    tot = 0
    for i in range(0, len(data), 3):
        bag1, bag2, bag3 = data[i].strip(), data[i+1].strip(), data[i+2].strip()
        s1, s2, s3 = set(bag1), set(bag2), set(bag3)

        res = list(s1.intersection(s2).intersection(s3))[0]
        tot += priority(res)

    return tot


if __name__ == "__main__":
    with open ("input.txt", "r") as f:
        data = f.readlines()

        print("Part 1:", part1(data))
        print("Part 2:", part2(data))
