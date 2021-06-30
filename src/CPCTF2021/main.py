import hashlib
input = list(map(int, input().split()))
input.sort()
s = " ".join([str(i) for i in input])
print(hashlib.md5(s.encode('utf-8')).hexdigest())