package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"strconv"
	"sort"
)

// Absolute value function for integers
func AbsInt(n int) int {
	if n < 0 {
		return -n
	}
	return n
}

func main() {
	// Open the file
	file, err := os.Open("./input.txt")
	if err != nil {
		fmt.Println("Error opening file: ", err)
		return
	}
	defer file.Close() // Ensure the file is closed when we're done

	// Create a new scanner for the file
	scanner := bufio.NewScanner(file)

	// temp array
	var x []int
	var y []int

	// Read the file line by line
	for scanner.Scan() {
		line := scanner.Text() // Get the line text
		parts := strings.Fields(line)
		for i := 0; i < len(parts); i++ {
			
			if i == 0 {
				num, _ := strconv.Atoi(parts[i])
				x = append(x, num)
			} else {
				num, _ := strconv.Atoi(parts[i])
				y = append(y, num)
			}
		}
	}
	sort.Ints(x)
	sort.Ints(y)

	var sum int
	for i := 0; i < len(x); i++ {
		sum += AbsInt(x[i] - y[i])
	}

	fmt.Println("Sum: ", sum)
}