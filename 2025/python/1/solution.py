def solution_part_1(input):
    start = 50
    count = 0
    with open(input, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            parts = [line[0], line[1:]]
            if parts[0] == "L":
                delta = -int(parts[1])
            elif parts[0] == "R":
                delta = int(parts[1])
            
            start = (start + delta) % 100
            if start == 0:
                count += 1
    
    return count

def solution_part_2(input):
    start = 50
    count = 0
    with open(input, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            delta = 1
            if line[0] == "L":
                delta = -1
            
            for _ in range(int(line[1:])):
                start = (start + delta) % 100
                if start == 0:
                    count += 1
    return count

if __name__ == "__main__":
    print(solution_part_2("input.txt"))