def solution_part_1(input):
    with open(input, "r", encoding="utf-8") as f:
        count = 0
        data = f.read().strip()
        k = 0
        for line in data.split("\n"):
            items = [item for item in line.split(",") if item]
            for item in items:
                item = item.split("-")
                for i in range(int(item[0]), int(item[1]) + 1):
                    if str(i)[0] != "0":
                        if len(str(i)) % 2 == 0 and len(str(i)) > 1:
                            if str(i)[:len(str(i)) // 2] == str(i)[len(str(i)) // 2:]:
                                count += i
                        elif len(str(i)) % 2 and len(str(i)) > 1:
                            match = True
                            for j, char in enumerate(str(i)):
                                if j == 0:
                                    continue

                                if char != str(i)[j - 1]:
                                    match = False
                                    break
                            if match:
                                count += i
        print(count)

def solution_part_2(input):
    with open(input, "r", encoding="utf-8") as f:
        count = 0
        data = f.read().strip()
        for line in data.split("\n"):
            items = [item for item in line.split(",") if item]
            for item in items:
                item = item.split("-")
                for i in range(int(item[0]), int(item[1]) + 1):
                    if str(i)[0] != "0":
                        pattern, _ = find_repeating_pattern(str(i))
                        if pattern != str(i):
                            count += i
        print(count)

def find_repeating_pattern(s):
    """Find the smallest repeating pattern in a string"""
    # s = "111", len(s) = 3
    # 3 // 2 + 1 = 2
    # first portion_size = 1 -> pattern = "1"
    # Check if "111" is made of "1" -> True
    # second portion_size = 2 -> pattern = "11"
    # Check if "111" is made of "11" -> False
    # Return "1", 1
    for portion_size in range(1, len(s) // 2 + 1):
        pattern = s[:portion_size]
        # Check if entire string is made of this pattern
        if all(s[i:i+portion_size] == pattern for i in range(0, len(s), portion_size)):
            return pattern, portion_size
    return s, len(s)  # No pattern found, return whole string

if __name__ == "__main__":
    solution_part_1("input.txt")
    solution_part_2("input.txt")