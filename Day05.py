import numpy

only_part_one=True
lines = []

with open("input/05.txt") as file:
    for line in file:
        start, _, end = line.split(" ")

        start = [int(coord) for coord in start.split(",")]
        end = [int(coord) for coord in end.split(",")]
        lines.append([start, end])

# Filter horizontal/vertical

lines = [line for line in lines 
if line[0][0] == line[1][0] 
or line[0][1] == line[1][1] 
or abs(line[0][0]-line[1][0]) == abs(line[0][1] - line[1][1])]


max_x = 0
max_y = 0
for li in lines:
    max_x = max(max_x, li[0][0], li[1][0])
    max_y = max(max_y, li[0][1], li[1][1])


map = numpy.zeros((max_x+1, max_y+1))

def make_name(x,y):
    return "{},{}".format(x, y)

def add_point(x, y):
    map[x][y] += 1

def make_vertical(x, y1, y2):
    #print("Creating ({},{}) -> ({},{})".format(x,y1,x,y2))
    for y in range(y1, y2+1):
        #print("Adding ({},{})".format(x, y))
        add_point(x,y)

def make_horizontal(y, x1, x2):
    #print("Creating ({},{}) -> ({},{})".format(x1, y, x2, y))
    for x in range(x1, x2+1):
        add_point(x, y)

def make_diagonal(x1, y1, x2, y2):
    if only_part_one:
        return
    #print("({},{}) -> ({},{})".format(x1,y1,x2,y2))
    xDir = 1 if x1 < x2 else -1
    yDir = 1 if y1 < y2 else -1
    while x1 != x2 and y1 != y2:
        add_point(x1, y1)
        x1+=xDir
        y1+=yDir
    add_point(x2, y2)

for line in lines:
    x1,y1 = line[0]
    x2,y2 = line[1]
    if x1 == x2:
        make_vertical(x1, min(y1, y2), max(y1, y2))
    elif y1 == y2:
        make_horizontal(y1, min(x1, x2), max(x1, x2))
    else:
        make_diagonal(x1,y1,x2,y2)

def count_intersections():
    res = 0
    for x in range(0, max_x+1):
        for y in range(0, max_y+1):
            if map[x][y] > 1:
                res += 1
    return res

if __name__ == "__main__":
    print("Max X:", max_x, "Max Y:", max_y)
    print("Part One:", count_intersections())
