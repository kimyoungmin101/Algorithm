A = input()

try:
    print(ord(A))
except:
    A = int(A)
    print(chr(A))
