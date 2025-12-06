def solution_part_1(input):
    with open(input, "r") as file:
        data = file.read().strip().splitlines()
        for i in range(len(data)):
            data[i] = (" ".join(data[i].split())).split(" ")
        
        print(data)

if __name__ == "__main__":
    solution_part_1("input.txt")