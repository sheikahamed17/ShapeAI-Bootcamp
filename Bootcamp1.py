import hashlib
strhash = input('Enter a string :')
en = strhash.encode()
result = hashlib.md5(en)
print(result.hexdigest())
