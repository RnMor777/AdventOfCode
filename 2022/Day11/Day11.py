class monkey:
    def __init__(self, start, operation, cond, t, f, monkeys):
        self.items = start
        self.operation = operation
        self.condition = cond
        self.t = t
        self.f = f
        self.mlist = monkeys

    def procTurn (self):
        while len(self.items) > 0:
            self.items.pop(0)
            tmp = self.operation.replace('old', '5')
            exec (f"x = {tmp}")
            print (locals()['x'])


def generateMonkeys (lines):
    monkeys = []
    for i in range(0, len(lines), 7):
        start = lines[i+1].replace(',', '')
        start = list(map(int, start.split()[2:]))
        operation = lines[i+2][18:].strip()
        cond = int(lines[i+3].split()[-1])
        t = int(lines[i+4].split()[-1])
        f = int(lines[i+5].split()[-1])
        monkeys.append(monkey(start, operation, cond, t, f, monkeys))

    return monkeys

def part1 (lines):
    return

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()
        monkeys = generateMonkeys(lines)
        monkeys[0].procTurn()

        # printing everything
        # print("Part 1:", part1(cycles))
