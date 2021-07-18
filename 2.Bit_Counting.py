'''
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number.
You can guarantee that input is non-negative.
Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
'''

from typing import Tuple
def count_bits(n: int) -> Tuple:
    ans = []
    finish = 0
    while n != 0:
        a = n // 2
        b = n % 2
        n = a
        ans.append(b)
    ans.reverse()
    for i in range(len(ans)):
        if ans[i] == 1:
            finish += 1
    return ans, finish
ex = count_bits(1234)
print(ex)

'''
-----BEST PRACTICES-----
#1
def countBits(n):
    return bin(n).count("1")

#2
def countBits(n):
    total = 0
    while n > 0:
        total += n % 2
        n >>= 1     # Битовый сдвиг вправо на 1 (т.е. уменьшение в 2 раза, если 2 то в 4 раза, 3 в 8 раз)
    return total
'''