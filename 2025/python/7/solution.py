from collections import Counter
def solution_part_1(input):
    with open(input, 'r') as file:
        data = file.read().strip().splitlines()
        count = 0
        current = set()
        for row in range(len(data)):
            for col in range(len(data[row])):
                if data[row][col] == "S":
                    current.add((row, col))

        while len(current) > 0:
            next = set()
            for x, y in current:
                if x + 1 >= len(data):
                    continue
                if data[x][y] == "^":
                    next.add((x + 1, y - 1))
                    next.add((x + 1, y + 1))
                    count += 1
                else:
                    next.add((x + 1, y))
            
            current = next
        print(count)

def solution_part_2(input):
    with open(input, 'r') as file:
        data = file.read().strip().splitlines()
        count = 0
        current = []
        for row in range(len(data)):
            for col in range(len(data[row])):
                if data[row][col] == "S":
                    current.append((row, col, 1))

        while len(current) > 0:
            next = []
            for x, y, c in current:
                if x + 1 >= len(data):
                    count += c
                    continue
                if data[x][y] == "^":
                    next.append((x + 1, y - 1, c))
                    next.append((x + 1, y + 1, c))
                else:
                    next.append((x + 1, y, c))
            
            p = Counter()
            for (x, y, c) in next:
                p[(x, y)] += c 


            for x, y in p.keys():
                current.append((x, y, p[(x, y)]))
        print(count)



if __name__ == "__main__":
    # solution_part_1('input.txt')
    solution_part_2("input.txt")