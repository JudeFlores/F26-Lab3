# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Jude Flores
# Date: September 30th, 2026
# Purpose: Practice adding and removing elements in list.
# Usage: ./lab3d.py

# Follow the specific instructions given in the README.md file
myList = [1, 2, 3, 4, 5, 6]
myList.append(7)
myList.insert(0,0)
myList.pop(2)
print(myList)
print("The element 6 is present at the index ", myList.index(6))