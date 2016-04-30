#!/usr/bin/env python
import sys
"""
This program takes a bit sequence M, a smaller bit sequence N, a starting and
stopping indexes i and j, and creates a new number new_M where N is inserted
into M in M's indices of i and j.
example run:
parameters: M, N, i, j
./5.1_insertion.py 10000000000 1001101 2 8
"""
def get_bit(num, index):
    """
    Returns a number that is the single bit representation of num and index
    This will be one one and all zeroes or all zeroes
    For example: num: 1001, index: 3, result: 1
    (index is from the right, not left)
    """
    return 1 if num & (1 << index) else 0

def update_bit(num, index, value):
    """
    Sets returns an int with the value of num, but with the bit value at the
    index set to that of the value
    """
    value = get_bit(value, 0)
    mask = ~(1 << index)
    return (num & mask) | (value << index)

"""
--Start of program--
argv[1]: the bit sequence into which I will insert N
argv[2]: the bit sequence to insert into M
argv[3]: the starting index where N will be inserted into M
argv[4]: the ending index (inclusive) where N will be inserted into M
"""
M = int('0b' + sys.argv[1], 2)
N = int('0b' + sys.argv[2], 2)
i = int(sys.argv[3])
j = int(sys.argv[4])

print("num: ", bin(M))
print("shift: ", get_bit(M, 10))

new_M = M
for k in range(i, j+1):
    bit = get_bit(N, k-i)
    new_M = update_bit(new_M, k, bit)
print("orig M: " + bin(M))
print("N: " + bin(N))
print("i: ", i, "j: ", j)
print("new M: " + bin(new_M))

"""
example usage (using the command line):
./5.1_insertion.py 10000000000 1001101 2 8
num:  0b10000000000
shift:  1
k-i:  0 bit:  1
k-i:  1 bit:  0
k-i:  2 bit:  1
k-i:  3 bit:  1
k-i:  4 bit:  0
k-i:  5 bit:  0
k-i:  6 bit:  1
orig M: 0b10000000000
N: 0b1001101
i:  2 j:  8
new M: 0b10100110100
"""
