class Node:
    # initialize the node
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.dirs = []
        self.files = {}
        self.size = 0

    # add a sub directory to the current directory
    def add_dir (self, name):
        self.dirs.append(Node(name, self))

    # add the file size to current directory and update all parents
    def add_file (self, name, size):
        self.files[name] = size
        self.size += size

        tmp = self.parent
        while (tmp is not None):
            tmp.size += size
            tmp = tmp.parent

    # change the directory to a sub directory
    def change_dir (self, name):
        for node in self.dirs:
            if node.name == name:
                return node

        self.add_dir(name)
        return self.dirs[-1]

def calcSize (arr, node):
    # loop through all folders and return their sizes
    for i in node.dirs:
        arr.append((i.name, i.size))
        calcSize (arr, i)

def generateNodes (data):
    # create an intial root node
    i = 0
    rootNode = Node('/', None)
    currNode = rootNode

    # for each line in the data file
    for i in data:
        line = i.strip().split()

        # if the entry was a command
        if line[0] == "$":
            # if you are supposed to change directory
            if line[1] == "cd":
                # if the directory is going up or down
                if line[2] == "..":
                    currNode = currNode.parent
                else:
                    currNode = currNode.change_dir (line[2])

        # found a file or directory to add to folder structure
        else:
            if line[0] == "dir":
                currNode.add_dir(line[1])
            else:
                currNode.add_file(line[1], int(line[0]))

    # return the root directory
    return rootNode

def part1 (rootNode):
    # calculate all sizes of folders
    arr = []
    calcSize (arr, rootNode)

    # find all that are less than 100,000
    totSize = 0
    for (_, j) in arr:
        if j <= 100000:
            totSize += j

    return totSize

def part2 (rootNode):
    # calculate all sizes of folders
    arr = []
    calcSize (arr, rootNode)

    # find the first node that is just greater than our goal
    goal = 30000000 - (70000000 - rootNode.size)
    arr = [j for (i, j) in arr if j >= goal]
    arr.sort()

    return arr[0]

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.readlines()
        rootNode = generateNodes(data)

        print ("Part 1:", part1(rootNode))
        print ("Part 2:", part2(rootNode))
