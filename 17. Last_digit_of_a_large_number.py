'''
Define a function that takes in two non-negative integers aaa and bbb and returns the last decimal digit of aba^ba
b. Note that aaa and bbb may be very large!
You may assume that the input will always be valid.
Examples
last_digit(4, 1)                # returns 4
last_digit(4, 2)                # returns 6
last_digit(9, 7)                # returns 9
last_digit(10, 10 ** 10)        # returns 0
last_digit(2 ** 200, 2 ** 300)  # returns 6
'''

def last_digit(n1: int, n2: int) -> int:
    numbers = []
    if n2 == 0:
        return 1
    step = 1
    while True:
        number = pow(n1, step)
        step += 1
        last = int(str(number)[-1])
        if last in numbers:
            break
        numbers.append(last)
    return numbers[n2 % len(numbers) - 1]

print(last_digit(9, 7))

'''
-----BEST PRACTICES-----
#1
def last_digit(n1, n2):
    return pow( n1, n2, 10 )
#2
rules = {
    0: [0,0,0,0],   
    1: [1,1,1,1],
    2: [2,4,8,6],
    3: [3,9,7,1],
    4: [4,6,4,6], 
    5: [5,5,5,5], 
    6: [6,6,6,6], 
    7: [7,9,3,1], 
    8: [8,4,2,6], 
    9: [9,1,9,1],
}
def last_digit(n1, n2):
    ruler = rules[int(str(n1)[-1])]
    return 1 if n2 == 0 else ruler[(n2 % 4) - 1]
'''
