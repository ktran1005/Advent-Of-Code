package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func follow_rules(update []string, rules [][]string) (bool, int) {
	idx := make(map[string]int)
	for i := 0; i < len(update); i++ {
		idx[update[i]] = i
	}

	for i := 0; i < len(rules); i++ {
		_, ok1 := idx[string(rules[i][0])]
		_, ok2 := idx[string(rules[i][1])]
		if ok1 && ok2 && !(idx[string(rules[i][0])] < idx[string(rules[i][1])]) {
			return false, 0
		}
	}

	size := len(update)
	idex := size / 2
	val, _ := strconv.Atoi(update[idex])
	return true, val
}

func main() {
	var rules [][]string
	var updates [][]string

	// Open the file
	file, err := os.Open("./input.txt")
	if err != nil {
		fmt.Println("Error opening file: ", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if strings.Contains(line, "|") {
			split_1 := strings.Split(line, "|")
			rules = append(rules, split_1)
		}
		if strings.Contains(line, ",") {
			split_2 := strings.Split(line, ",")
			updates = append(updates, split_2)
		}
	}

	answer := 0
	for _, update := range updates {
		good, mid := follow_rules(update, rules)
		if good {
			answer += mid
		}
	}

	fmt.Println(answer)
}
