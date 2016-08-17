#!/bin/bash

# replace beginning (^) and end ($) of each line with ", 
# then replace the end ($) with ,
sed -e 's/^\|$/"/g' -e 's/$/,/g' words.txt > strings.txt
