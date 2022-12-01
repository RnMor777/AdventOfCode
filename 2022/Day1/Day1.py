def part1 (arr):
    # print the max element
    return max(arr)


def part2 (arr):
    # sort array and print first 3
    arr.sort(reverse=True)
    return sum(arr[0:3])


if __name__ == "__main__":
    # Open the input file
    with open("input.txt", "r") as f:
        arr = []
        cur = 0

        # Read every line
        while x := f.readline():
            # if there was a space, then the elf is done
            if x != "\n":
                cur += int(x)
            else:
                arr.append(cur)
                cur = 0

        # print out both parts
        print("Part 1:", part1(arr))
        print("Part 2:", part2(arr))
