# Part One

increased = 0
prev = 1000

with open("input/01.txt", "r") as file:
    for line in file:
        num = int(line)
        if num > prev:
            increased = increased + 1
        prev = num
    

print("Part One:", increased)

# Part Two

increased = 0

def sum(numbers, first, last):
    res = 0
    for i in range(first, last):
        res = res + numbers[i]
    return res

with open("input/01.txt", "r") as file:
    numbers = []
    for line in file:
        num = int(line)
        numbers.append(num)

for i in range(0, len(numbers)-3):
    first = sum(numbers, i, i+3)
    second = sum(numbers, i+1, i+4)
    if second > first:
        increased = increased + 1
print("Part Two:", increased)
