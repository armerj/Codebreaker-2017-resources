hex_string = ['9', 'c0', '28', 'd3', '3f', 'd7', '60', '85', '34', 'c2', '33', 'cb', '22', '8a', '6b', '8b', '6b', '97', '74', '91', '77', 'c1', '3f', '95', '3c', '9c', '68', '91', '62', 'a5']

def unscramble(toggle, c):
    if toggle:
        return chr(0xFF-0x5A^c)
    else:
        return chr(0xFF-(0xA5^c))

for x in range(0, len(hex_string)):
    print unscramble(x & 0x1, int(hex_string[x], 16)), 

