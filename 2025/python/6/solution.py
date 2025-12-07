def solution_part_1(input):
    with open(input, "r") as file:
        total = 0
        data = file.read().strip().splitlines()
        for i in range(len(data)):
            data[i] = (" ".join(data[i].split())).split(" ")
        
        num_rows = len(data)
        num_cols = len(data[0])

        transposed = []
        for i in range(num_cols):
            curCols = []
            for j in range(num_rows):
                curCols.append(data[j][i])
            transposed.append(curCols)

        for i in range(len(transposed)):
            cur = 0
            for j in range(len(transposed[i]) - 1):
                if transposed[i][len(transposed[i]) - 1] == "*":
                    if j == 0:
                        cur = int(transposed[i][j])
                    else:
                        cur *= int(transposed[i][j])
                else:
                    cur += int(transposed[i][j])
            
            total += cur


    print(total)

def solution_part_2(input):
    with open(input, "r") as file:
        data = file.read().split('\n')
        ops = data[-1]
        number_data = data[:-1]
        
        line_start = 0
        total = 0

        while line_start < len(ops):
            current_ops = ops[line_start]
            line_ends = line_start + 1
            while line_ends < len(ops) and ops[line_ends] == " ":
                line_ends += 1
            
            if line_ends != len(ops):
                line_ends -= 2
            else:
                line_ends -= 1
            
            val = 0 if current_ops == "+" else 1
            
            for i in range(line_start, line_ends + 1):
                current_number = 0
                for line in number_data:
                    if line[i] != " ":
                        current_number *= 10
                        current_number += int(line[i])
                
                if current_ops == "+":
                    val += current_number
                else:
                    val *= current_number

            line_start = line_ends + 2
            total += val

        print(total)

if __name__ == "__main__":
    solution_part_1("input.txt")
    solution_part_2("input.txt")