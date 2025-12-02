# the dial starts by pointing at 50
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
            
            # Apply the rotation (keep position in 0..99)
            start = (start + delta) % 100
            if start == 0:
                count += 1

            # Calculate how many times this rotation wraps past 0.
            # For N=100 positions (0..99) the number of wraps is given by
            # floor((start + delta) / 100) for positive or negative totals.
            # Using Python's floor-division (//) handles negatives correctly.
            wraps = abs((start + delta) // 100)
            if (abs((start + delta) // 100)) == 1:
                print(parts)

            # Increment count by how many times we passed position 0
            count += wraps
    
    # print(wraps)
    return count

def solution_part_2(input):
    pass

if __name__ == "__main__":
    print(solution_part_1("input.txt"))