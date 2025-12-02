package main

import (
	"bufio"
	"fmt"
	"os"
)

func inside(row int, col int, height int, width int) bool {
	return 0 <= row && row < height && 0 <= col && col < width
}

func main() {
	// Open the file
	file, err := os.Open("./sample.txt")
	if err != nil {
		fmt.Println("Error opening file: ", err)
		return
	}
	defer file.Close()

	var s []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		s = append(s, line)
	}

	height := len(s)
	width := len(s[0])
	string_look_for := "XMAS"
	answer := 0

	for row := 0; row < height; row++ {
		for col := 0; col < width; col++ {
			if string(s[row][col]) == "X" {
				for drow := -1; drow <= 1; drow++ {
					for dcol := -1; dcol <= 1; dcol++ {
						if drow == 0 && dcol == 0 {
							continue
						}
						all_ok := true
						for i := 0; i < 4; i++ { // row = 0, col = 4
							r2 := row + drow*i // row = 0 ; drow = -1; i = 1 => r2 = -1
							c2 := col + dcol*i // col = 4; dcol = -1; i = 1 => c2 = 3   => s[-1][3]
							if inside(r2, c2, height, width) && string(s[r2][c2]) == string(string_look_for[i]) {
							} else {
								all_ok = false
								break
							}
						}
						if all_ok {
							answer += 1
						}

					}
				}
			}
		}
	}
	fmt.Println(answer)
}
