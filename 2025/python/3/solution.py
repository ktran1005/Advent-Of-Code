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

def solution_part_2(input):
    # Method: Stack
    with open(input, "r", encoding="utf-8") as f:
        count = 0
        data = f.read().strip().splitlines()
        for line in data:
            size = len(line)
            stack = []
            for i in range(size):
                # Ensure that we can still form a 12-digit number
                # by checking if the remaining digits plus the current stack size
                # is greater than 12
                # Pop smaller digits to maintain the largest possible number
                # and keep the stack size within 12
                # Push the current digit onto the stack
                # Finally, if the stack exceeds 12 digits, pop the smallest digits
                # to maintain the size
                while stack and stack[-1] < line[i] and len(stack) + (size - i) > 12:
                    stack.pop()
                stack.append(line[i])

                while len(stack) > 12:
                    stack.pop()

            count += int("".join(stack[:12]))

    print(count)  

if __name__ == "__main__":
    solution_part_1("input.txt")
    solution_part_2("input.txt")