package main

import (
	"fmt"
	"bufio"
	"os"
	"regexp"
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

	pattern := `mul\(\d+,\d+\)`
	r, _ := regexp.Compile(pattern)

	answer := 0
	// Create a new scanner for the file
	scanner := bufio.NewScanner(file)
	// Read the file line by line
	for scanner.Scan() {
		line := scanner.Text()
		// fmt.Println(r.FindAllStringSubmatchIndex(line, -1))
		// fmt.Println(line[1:9], line[29:37], line[53:62], line[62:70])
		indexes := r.FindAllStringSubmatchIndex(line, -1)
		// fmt.Println(indexes)
		for idx := 0; idx < len(indexes); idx++ {
			instruction := line[indexes[idx][0]:indexes[idx][1]]
			first := ""
			second := ""
			for i := 0; i < len(instruction); i++ {
				if unicode.IsDigit(rune(instruction[i])) && string(instruction[i-1]) == "(" {
					for {
						if string(instruction[i]) == "," {
							break
						}
						first += string(instruction[i])
						i++
					}
				}

				if unicode.IsDigit(rune(instruction[i])) && string(instruction[i-1]) == "," {
					for {
						if string(instruction[i]) == ")" {
							break
						}
						second += string(instruction[i])
						i++
					}
				}
			}

			if len(first) > 0 && len(second) > 0 {
				firstConv, _ := strconv.Atoi(first)
				secondConv, _ := strconv.Atoi(second)
				answer += firstConv *  secondConv 
			}
		}
	}
	fmt.Println(answer)
}