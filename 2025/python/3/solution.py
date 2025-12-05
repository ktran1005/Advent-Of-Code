def solution_part_1(input):
    with open(input, "r", encoding="utf-8") as f:
        count = 0
        data = f.read().strip().splitlines()
        for line in data:
            curMax = 0
            for i in range(len(line)):
                if i == len(line) - 1:
                    break
                j = i + 1
                while j < len(line):
                    num = int(line[i] + line[j])
                    curMax = max(curMax, num)
                    j += 1
            count += curMax
        print(count)
if __name__ == "__main__":
    solution_part_1("input.txt")