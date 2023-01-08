def part1 (inarr):
    # generate duplicate list for local use
    arr = list(inarr)

    #variables
    reg, step, res = 1, 1, 0

    # loop while instructions
    while len(arr) != 0:
        # if it is time to add the score
        if (step-20) % 40 == 0:
            res += step * reg

        # iterate instructions
        step += 1
        reg += arr.pop(0)

    return res

def part2 (arr):
    # variables
    reg, step = 1, 0
    picture = ""
    out = []

    # loop instructions
    while len(arr) != 0:
        # add either # or . depending on step 
        if step % 40 in range(reg-1, reg+2):
            picture += "#"
        else:
            picture += '.'

        step += 1
        reg += arr.pop(0)

        # done with a row
        if step % 40 == 0:
            out.append(picture)
            picture = ""

    return out

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        cycles = []
        while line := f.readline().strip():
            cycles.append(0)
            if line != "noop":
                cycles.append(int(line.split()[1]))

        # printing everything
        print("Part 1:", part1(cycles))
        print("Part 2:")
        print('\n'.join(part2(cycles)))
