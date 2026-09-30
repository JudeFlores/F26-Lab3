# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Jude Flores
# Date: September 30th, 2026
# Purpose: 
# Usage: ./lab3b.py

# Follow the specific instructions given in the README.md file
import random as r

sequence = r.sample(range(0,99), 10)
print(sequence)
sequence.reverse()
print(sequence)