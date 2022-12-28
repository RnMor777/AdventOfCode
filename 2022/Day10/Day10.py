def part1 (arr):
    reg, step, res = 1, 1, 0
    while len(arr) != 0:
        if (step-20) % 40 == 0:
            res += step * reg

        step += 1
        reg += arr.pop(0)

    return res

def part2 (arr):
    reg, step, res = 1, 1, 0
    picture = [["." for i in range(40)] for j in range(6)]
    while len(arr) != 0:
        math.floor(step/40)
        if (step-20) % 40 == 0:
            res += step * reg

        step += 1
        reg += arr.pop(0)

    return res


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        cycles = []
        while line := f.readline().strip():
            cycles.append(0)
            if line != "noop":
                cycles.append(int(line.split()[1]))

        print("Part 1:", part1(cycles))
