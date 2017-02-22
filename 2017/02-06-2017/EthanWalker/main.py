#!/usr/bin/env python3

from reverse_str import reverse_line
import sys

#open file and get lines
with open(sys.argv[1], 'r') as in_file:
    file = in_file.readlines()

# print reversed lines
for line in file:
    print(reverse_line(line))