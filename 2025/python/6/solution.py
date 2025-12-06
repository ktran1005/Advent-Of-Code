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
        total = 0
        data = file.read().strip().splitlines()
        for i in range(len(data)):
            data[i] = (" ".join(data[i].split())).split(" ")
        
        num_rows = len(data)
        num_cols = len(data[0])

        transposed = []
        hashMap = {}
        for i in range(num_cols):
            curCols = []
            maxLen = 0
            for j in range(num_rows):
                curCols.append(data[j][i])
                maxLen = max(maxLen, len(data[j][i]))
            transposed.append(curCols)
            hashMap[i] = maxLen
        
        print(hashMap)
        print(transposed)
        for i in range(len(transposed) - 1, -1, -1):
            temp = ""
            k = 0
            while k < hashMap[i]:
                for j in range(len(transposed[i]) - 1):
                    if len(transposed[i][j]) < hashMap[i] and k < hashMap[i] - len(transposed[i][j]):
                        continue
                # while k < hashMap[i]:
                #     if len(transposed[i][j]) < hashMap[i] and k < hashMap[i] - len(transposed[i][j]):
                #         continue
                #     temp += transposed[i][j][k]
                #     k += 1
                

if __name__ == "__main__":
    # solution_part_1("input.txt")
    solution_part_2("input.txt")