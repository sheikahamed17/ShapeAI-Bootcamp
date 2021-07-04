import hashlib
strhash = "sdsheikahamed"
en = strhash.encode()
result = hashlib.md5(en)
print(result.hexdigest())