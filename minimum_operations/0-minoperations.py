0-minoperations.py
#!/usr/bin/env python3
"""
 write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file!
returns an integer
If n is impossible to achieve, return 0
n = 9
H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
Number of operations: 6
"""


def minOperations(n):
    if n < 2:
        return 0

    count = 0
    current_length = 1

    for i in range(2, n + 1):
        while n % i == 0:
            count += i
            n = n // i

    return count


    
    

