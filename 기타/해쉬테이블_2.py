# Linear Probing 기법
import hashlib

hash_table = list([0 for _ in range(8)])

def get_key(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode()) 
    hex_dig = hash_object.hexdigest() # 16진수로 추출,
    return int(hex_dig, 16)

def hash_function(key):
    return key % 8

def save_data(data,value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            elif hash_table[index][0] == index_key:
                hash_table[index][1] = value
                return
    else:
        hash_table[hash_address] = [index_key, value]
    
def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None

save_data('DAVE', '01024670554')
save_data('JEAN', '01099176817')
save_data('DQWE', '01024343212')
save_data('VDEW', '01034325532')
save_data('VVCC', '01023583828')
save_data('DSGB', '01028277772')

print(hash_table)
print(read_data('DQWE'))