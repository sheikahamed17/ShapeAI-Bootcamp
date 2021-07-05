import hashlib, binascii

hash = hashlib.pbkdf2_hmac('md5',b'sdsheikahamed',b'z1y2x3w4v5u6t7s8',272)
binascii.hexlify(hash)
print(hash)
