#!/bin/bash

url="http://amfiindia.com/spages/NAVAll.txt"
output_file="output.csv"


curl -s "$url" -o temp.txt


awk -F, '{print $1","$6}' temp.txt > "$output_file"

rm temp.txt

echo "Extraction completed. The data is saved in $output_file."
