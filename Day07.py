movements = []

with open("input/07.txt") as file:
    for line in file:
        curr = [int(i) for i in line.split(",")]
        for i in curr:
            movements.append(i)

def cost_for_mov(target):
    sum = 0
    for mov in movements:
        sum += abs(mov-target)
    return sum


cache = {}

def get_mov_cost(fromPos, toPos):
    global cache
    dist = abs(fromPos-toPos)
    if not dist in cache:
        cache[dist] = sum([i for i in range(dist+1)])
    return cache[dist]

def cost_for_mov_two(target, maxAllowed):
    sum = 0
    for mov in movements:
        if sum > maxAllowed:
            return sum
        sum += get_mov_cost(mov, target)
    return sum

def get_min_cost():
    min_target = -1
    min_cost = 9999999999
    for possibility in range(min(movements), max(movements)+1):
        cost = cost_for_mov(possibility)
        if cost < min_cost:
            print("New min {} for target {}".format(cost, possibility))
            min_target = possibility
            min_cost = cost
    return [min_target, min_cost]

def get_min_cost_two():
    min_target = -1
    min_cost = 9999999999

    min_val = min(movements)
    max_val = max(movements)
    for possibility in range(min_val, max_val+1):
        cost = cost_for_mov_two(possibility, min_cost)
        if cost < min_cost:
            print("New min {} for target {}".format(cost, possibility))
            min_target = possibility
            min_cost = cost
    return [min_target, min_cost]

if __name__ == "__main__":
    print("Part One:", get_min_cost())
    print("Part Two:", get_min_cost_two())