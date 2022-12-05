def part1 (data, arrIn):
    arr = [x for x in arrIn]
    for i in data:
        x = i.strip().split(' ')
        quan, fro, to = list(map(int, [x[1], x[3], x[5]]))
        arr[to] = arr[fro][0:quan][::-1] + arr[to]
        arr[fro] = arr[fro][quan:]
    return ''.join([arr[i][0] for i in range(1, 10)])

def part2 (data, arrIn):
    arr = [x for x in arrIn]
    for i in data:
        x = i.strip().split(' ')
        quan, fro, to = list(map(int, [x[1], x[3], x[5]]))
        arr[to] = arr[fro][0:quan] + arr[to]
        arr[fro] = arr[fro][quan:]
    return ''.join([arr[i][0] for i in range(1, 10)])

if __name__ == "__main__":
    with open ("input.txt", "r") as f:
        lists = [[] for i in range(10)]
        for i in range(8):
            x = f.readline().strip()
            line = [x[i+1:i+2] for i in range(0, len(x)-2, 4)]
            for i in range(9):
                if line[i] != ' ':
                    lists[i+1].append(line[i])

        data = f.readlines()[2:]

        print("Part 1:", part1(data, lists))
        print("Part 2:", part2(data, lists))
