instructions = []

with open("input/02.txt", "r") as file:
    for line in file:
        instructions.append(line.split(" "))

print("Fetched", len(instructions), "instructions")

horizontal = 0
depth = 0

for instr in instructions:
    num = int(instr[1])
    if instr[0] == "forward":
        horizontal = horizontal + num
    elif instr[0] == "down":
        depth = depth + num
    elif instr[0] == "up":
        depth = depth - num

print("Part One:", depth*horizontal)

# Part Two

horizontal = 0
depth = 0
aim = 0

for instr in instructions:
    num = int(instr[1])
    if instr[0] == "forward":
        horizontal = horizontal + num
        depth += aim*num
    elif instr[0] == "down":
        aim = aim + num
    elif instr[0] == "up":
        aim = aim - num

print("Part Two:", depth*horizontal)
