def count_zeros(lines, index):
    zeroes = 0
    for line in lines:
        if int(line[index]) == 0:
            zeroes += 1
    return zeroes

def construct_gamma(count):
    out = ""
    for index in count:
        if index[0] > index[1]:
            out += "0"
        else:
            out += "1"
    print(out)
    return int(out, 2)


def construct_epsilon(count):
    out = ""
    for index in count:
        if index[0] > index[1]:
            out += "1"
        else:
            out += "0"
    print(out)
    return int(out, 2)

lines = []

with open("input/03.txt", "r") as file:
    for line in file:
        lines.append(line.replace("\n", ""))

length = len(lines[0])
print(length)

count = []

for i in range(length):
    zeroes = count_zeros(lines, i)
    count.append([zeroes, len(lines)-zeroes])

gamma = construct_gamma(count)
epsilon = construct_epsilon(count)
print("Gamma:", gamma, "Epsilon:", epsilon)
print("Part One:", gamma*epsilon)


# Find Oxygen

left = list(lines)
index = 0

while len(left) > 1 and index < length:   
    zeroes = count_zeros(left, index)
    ones = len(left)-zeroes
    if zeroes > ones:
        for line in list(left):
            if line[index] != "0":
                left.remove(line)
    else:
        for line in list(left):
            if line[index] != "1":
                left.remove(line)
    
    index += 1


oxygen = left[0]
print("Oxygen:", oxygen, "left", len(left))

left = list(lines)
index = 0

while len(left) > 1 and index < length:
    zeroes = count_zeros(left, index)
    ones = len(left)-zeroes
    if zeroes <= ones:
        for line in list(left):
            if line[index] != "0":
                left.remove(line)
    else:
        for line in list(left):
            if line[index] != "1":
                left.remove(line)

    index += 1

co2 = left[0]
print("C02:", co2, "left", len(left))

oxynum = int(oxygen, 2)
co2num = int(co2, 2)

print("Oxy", oxynum, ", Co2", co2num)
print("Part Two:", oxynum*co2num)
