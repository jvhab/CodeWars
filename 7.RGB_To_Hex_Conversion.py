'''
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned.
Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.
Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
The following are examples of expected output values:
rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
'''

def rgb(r: int, g: int, b:int) -> str:
    if r > 255:
        r = 255
    elif r < 0:
        r = 0
    if g > 255:
        g = 255
    elif g < 0:
        g = 0
    if b > 255:
        b = 255
    elif b < 0:
        b = 0
    r = str(hex(r))
    g = str(hex(g))
    b = str(hex(b))
    if len(r) == 3:
        r = '0' + r[2:]
    if len(g) == 3:
        g = '0' + g[2:]
    if len(b) == 3:
        b = '0' + b[2:]
    if len(r) == 4:
        r = r[2:]
    if len(g) == 4:
        g = g[2:]
    if len(b) == 4:
        b = b[2:]
    return r.upper() + g.upper() + b.upper()
print(rgb(304, -100, 274))

'''
-----BEST PRACTICES-----
#1
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))

#2
def limit(num):
    if num < 0:
        return 0
    if num > 255:
        return 255
    return num
    
def rgb(r, g, b):
    return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))
'''