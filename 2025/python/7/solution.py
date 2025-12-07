from collections import defaultdict
def solution_part_1(input):
    with open(input, 'r') as file:
        count = 0
        start = None
        first_stop = True
        data = file.read().strip().splitlines()
        track = []
        for row in range(len(data)):
            hashMap = defaultdict(list)
            for col in range(len(data[0])):
                if data[row][col] == "S":
                    start = (row, col)
                    continue
                if data[row][col] == "^" and first_stop: 
                    first_stop = False
                    track.append(col)
                    continue
                
                if track:
                    if data[row][col] == "^":
                        if col not in track:
                            # print("row {} col {} plus 1".format(row, col))
                            count += 1
                            hashMap[row].append(col)
            
            if len(hashMap[row]):
                while track:
                    track.pop()
                for c in hashMap[row]:
                    track.append(c)
                print("track: {} after adding new element at row {}; count {}".format(track, row, count))

        print(count)
if __name__ == "__main__":
    solution_part_1('input.txt')