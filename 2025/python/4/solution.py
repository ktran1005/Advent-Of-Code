def solution_part_1(input):
    with open(input, 'r') as file:
        count = 0
        data = file.read().strip().splitlines()
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == "@":
                    adjacent_count = check_8_adjacent_position(data, i, j)
                    if adjacent_count < 4:
                        count += 1
        print(count)

def solution_part_2(input):
    with open(input, 'r') as file:
        data = file.read().strip().splitlines()
        total = 0
        count = 0
        more = True
        iteration = 0
        track = []
        while more:
            count = 0
            for i in range(len(data)):
                for j in range(len(data[i])):
                    if data[i][j] == "@":
                        adjacent_count = check_8_adjacent_position(data, i, j)
                        if adjacent_count < 4:
                            track.append([i, j])
                            count += 1
            iteration += 1
            total += count
            if count == 0:
                more = False
            else:
                for i, j in track:
                    temp = list(data[i])
                    temp[j] = "."
                    data[i] = "".join(temp)

        print(total)

def check_8_adjacent_position(grid, row, col):
    count = 0
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        # Check if the new position is within the grid boundaries
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            if grid[r][c] == "@":
                count += 1
    return count


if __name__ == "__main__":
    solution_part_1('input.txt')
    solution_part_2('input.txt')