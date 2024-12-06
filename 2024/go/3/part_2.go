package main

import (
	"fmt"
	"bufio"
	"os"
	"unicode"
	"strconv"
)

func main() {
	// Open the file
	file, err := os.Open("./input.txt")
	if err != nil {
		fmt.Println("Error opening file: ", err)
		return
	}
	defer file.Close()


	answer := 0
	first := ""
	second := ""
	enable := true
	// Create a new scanner for the file
	scanner := bufio.NewScanner(file)
	// Read the file line by line
	for scanner.Scan() {
		line := scanner.Text()
		for i := 0; i < len(line); i++ {
			if string(line[i]) == "d" {
				if line[i:i+4] == "do()" {
					enable = true
				}
				
				if line[i:i+7] == "don't()" {
					enable = false
				} 
			}
			if enable == true && string(line[i]) == "m" {
				if string(line[i+1]) == "u" && string(line[i+2]) == "l" && string(line[i+3]) == "(" {
					i += 4
					for {
						if !(unicode.IsDigit(rune(line[i]))) {
							break
						}
						first += string(line[i])
						i += 1
					}			
				}
				if string(line[i]) == "," {
					i += 1
					for {
						if !(unicode.IsDigit(rune(line[i]))) {
							break
						}
						second += string(line[i])
						i += 1
					}
				}
				if !(string(line[i]) == ")") {
					second = ""
				}
				if len(first) > 0 && len(second) > 0 {
					firstConv, _ := strconv.Atoi(first)
					secondConv, _ := strconv.Atoi(second)
					answer += firstConv * secondConv

				}
				first = ""
				second = ""
			} 
		}
	}
	fmt.Println(answer)
}