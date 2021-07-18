'''
Your task is to construct a building which will be a pile of n cubes.
The cube at the bottom will have a volume of n^3, the cube above will have volume of (n-1)^3 and so on until the top which will have a volume of 1^3.
You are given the total volume m of the building. Being given m can you find the number n of cubes you will have to build?
The parameter of the function findNb (find_nb, find-nb, findNb, ...)
will be an integer m and you have to return the integer n such as n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists or -1 if there is no such n.
Examples:
findNb(1071225) --> 45
findNb(91716553919377) --> -1
'''

def find_nb(m: int) -> int:
    ans = 0
    i = 0
    while ans != m:
        ans += i ** 3
        i += 1
        if ans > m:
            return -1
        elif ans == m:
            return i - 1
print(find_nb(1071225))

'''
-----BEST PRACTICES-----
#1
def find_nb(m):
    n = 1
    volume = 0
    while volume < m:
        volume += n**3
        if volume == m:
            return n
        n += 1
    return -1
'''