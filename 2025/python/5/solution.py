def solution_part_1(input):
    with open(input, 'r') as file:
        rangeArr = []
        count = 0
        data = file.read().strip().splitlines()
        for i in range(len(data)):
            if '-' in data[i]:
                data[i] = data[i].split('-')
                rangeArr.append(data[i])
            
            else:
                if data[i] == '':
                    continue
                
                for pair in rangeArr:
                    if int(data[i]) in range(int(pair[0]), int(pair[1]) + 1):
                        count += 1
                        break
        print(count)

def solution_part_2(input):
    # Technique: Merge Intervals
    with open(input, 'r') as file:
        interval = []
        data = file.read().strip().splitlines()
        res = []
        count = 0
        for i in range(len(data)):
            if '-' in data[i]:
                data[i] = data[i].split('-')
                interval.append([int(data[i][0]), int(data[i][1])])
            else:
                break
    
        interval.sort()

        for i in range(len(interval)):
            if not res:
                res.append(interval[i])
            else:
                if interval[i][0] <= res[-1][1]:
                    res[-1][1] = max(res[-1][1], interval[i][1])
                else:
                    res.append(interval[i])
        
        for i in range(len(res)):
            count += res[i][1] - res[i][0] + 1
        print(count)


if __name__ == "__main__":
    solution_part_1('input.txt')
    solution_part_2('input.txt')