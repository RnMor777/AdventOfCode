def part1 (data):
    for i in range(len(data)-4):
        if len(list(set(data[i:i+4]))) == 4:
            return i + 4
    return -1

def part2 (data):
    for i in range(len(data)-14):
        if len(list(set(data[i:i+14]))) == 14:
            return i + 14
    return -1

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        line = f.readline().strip()

        print ("Part 1:", part1(line))
        print ("Part 2:", part2(line))
