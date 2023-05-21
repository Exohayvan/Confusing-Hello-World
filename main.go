package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
)

type Decoded struct {
	Decoded string `json:"decoded"`
}

func main() {
	jsonFile, err := os.Open("decoded.json")
	if err != nil {
		fmt.Println(err)
	}
	defer jsonFile.Close()

	byteValue, _ := ioutil.ReadAll(jsonFile)

	var decoded Decoded

	json.Unmarshal(byteValue, &decoded)

	fmt.Println(decoded.Decoded)
}
