import hashlib

# SHA251
data = 'test'.encode() # Byte로 변환
hash_object = hashlib.sha1()
hash_object.update(data) 
hex_dig = hash_object.hexdigest() # 16진수로 추출,

print(hex_dig) # Data가 같을 경우는 무조건 같은 결과 값이 나온다.


# SHA256
data = 'test'.encode() # Byte로 변환
hash_object = hashlib.sha256()
hash_object.update(data) 
hex_dig = hash_object.hexdigest() # 16진수로 추출,

print(hex_dig) # Data가 같을 경우는 무조건 같은 결과 값이 나온다.