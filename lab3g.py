# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Jude Flores
# Date: September 30th, 2026
# Purpose: 
# Usage: ./lab3g.py

# Follow the specific instructions given in the README.md file
list = []
x = 0
while len(list)<7:
   list.append(int(input("Enter a number: ")))
   list[x] = list[x]*10
   x = x + 1
list.reverse()
print(list)