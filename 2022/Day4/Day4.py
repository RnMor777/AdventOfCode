def part1 (data):
    tot = 0
    for i in data:
        r1, r2, r3, r4 = list(map(int, i.strip().replace(',','-').split('-')))
        set1 = set(range(r1, r2+1))
        set2 = set(range(r3, r4+1))

        tot += 1 if set1.issubset(set2) or set2.issubset(set1) else 0

    return tot

def part2 (data):
    tot = 0
    for i in data:
        r1, r2, r3, r4 = list(map(int, i.strip().replace(',','-').split('-')))
        set1 = set(range(r1, r2+1))
        set2 = set(range(r3, r4+1))

        tot += 1 if len(set1.intersection(set2)) > 0 else 0

    return tot

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.readlines()

        print("Part 1:", part1(data))
        print("Part 2:", part2(data))
