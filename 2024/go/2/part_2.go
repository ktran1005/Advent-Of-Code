package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"strconv"
	
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
	defer file.Close() // Ensure the file is closed after we are done

	// Create a new scanner for the file
	scanner := bufio.NewScanner(file)

	answer := 0
	// Read the file line by line
	for scanner.Scan() {
		line := scanner.Text() // Get the line
		nums := strings.Split(line, " ")
		for i := 0; i < len(nums); i++ {
			flag := true
			increasing := true
			decreasing := true
			newArray := append([]string{}, nums[:i]...)
        	newArray = append(newArray, nums[i+1:]...)			
			for j := 0; j < len(newArray) - 1; j++ {
				a, _ := strconv.Atoi(newArray[j + 1])
				b, _ := strconv.Atoi(newArray[j])  
				diff := a - b
				
				if diff < 0 {
					increasing  = false
				}
				
				if diff > 0 {
					decreasing = false
				}

				absDiff := AbsInt(diff)
				if !(absDiff >= 1 && absDiff <= 3) {
					flag = false
					break
				}
			}

			if flag && (increasing || decreasing) {
				answer += 1
				break
			}
		}
	}
	fmt.Printf("Answer: %v\n", answer)
}