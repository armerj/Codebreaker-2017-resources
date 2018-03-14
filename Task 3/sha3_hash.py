import sha3
import binascii
import time

data= '8e08fe33bcb2a6417669724cf4fa1b5c6db2ccf78f1ba4ba076d5edc133b1931'
s=sha3.sha3_256(binascii.unhexlify(data)).hexdigest()
print data, s

print 'Getting collision'

for i in range(0x10000):
    col = hex(i)[2:]
    while len(col) < 4:
        col = '0' + col
    for j in range(0x10000):
        col_1 = hex(j)[2:]
        while len(col_1) < 4:
            col_1 = '0' + col_1
        col_s=sha3.sha3_256(binascii.unhexlify(col + col_1)).hexdigest()
        if s[:8] == col_s[:8]:
            print col + col_1, col_s

print time.ctime()
