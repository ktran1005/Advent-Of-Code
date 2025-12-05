def solution_part_1(input):
    with open(input, 'r') as file:
        rangeArr = []
        count = 0
        data = file.read().strip().splitlines()
        # print(data)
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



if __name__ == "__main__":
    solution_part_1('input.txt')