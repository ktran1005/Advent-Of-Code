from collections import defaultdict
def solution_part_1(input):
    with open(input, 'r') as file:
        data = file.read().strip().splitlines()
        count = 0
        current = set()
        i = 0
        for row in range(len(data)):
            for col in range(len(data[row])):
                if data[row][col] == "S":
                    current.add((row, col))
        print(current)
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
            
            current = list(set(next))
        print(count)
if __name__ == "__main__":
    solution_part_1('input.txt')