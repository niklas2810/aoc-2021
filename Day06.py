fishes = []

def fetch_data():
  global fishes
  fishes = [0 for i in range(9)]
  with open("input/06.txt") as file:
    for line in file:
      current = [int(i) for i in line.split(",")]
      for i in current:
        fishes[i] += 1


def simulate_iterations(duration):
  for day in range(1,duration+1):
    add_today = fishes[0]
    for i in range(1,len(fishes)):
      fishes[i-1] = fishes[i]
    fishes[6] += add_today
    fishes[len(fishes)-1] = add_today

def count_fishes():
  sum = 0
  for i in fishes:
    sum += i
  return sum

if __name__ == "__main__":
  fetch_data()
  simulate_iterations(80)
  print("Part One: {}".format(count_fishes()))

  fetch_data()
  simulate_iterations(256)
  print("Part Two: {}".format(count_fishes()))