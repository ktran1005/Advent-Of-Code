package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	// oPen the file
	file, err := os.Open("./input.txt")
	if err != nil {
		fmt.Println("Error opening file: ", err)
		return
	}
	defer file.Close()

	var s []string
	points := [][]int{
		{-1, -1}, {-1, 1},
		{1, 1}, {1, -1},
	}

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		s = append(s, line)
	}

	height := len(s)
	width := len(s[0])
	answer := 0

	for row := 1; row < height-1; row++ {
		for col := 1; col < width-1; col++ {
			if string(s[row][col]) == "A" {
				tmp := ""
				for i := 0; i < len(points); i++ {
					tmp += string(s[row+points[i][0]][col+points[i][1]])
				}

				if tmp == "MMSS" || tmp == "MSSM" || tmp == "SSMM" || tmp == "SMMS" {
					answer += 1
				}
			}
		}
	}
	fmt.Println(answer)
}
