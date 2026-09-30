# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Jude Flores
# Date: September 30th, 2026
# Purpose: 
# Usage: ./lab3a.py
import random

randomValues = []
for i in range(20):
    randomValues.append(random.randint(0, 99))
    print(randomValues[i])

print("Sorted List: ")
randomValues.sort()
for i in range(20):
    print(randomValues[i])