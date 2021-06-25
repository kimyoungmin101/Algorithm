def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

Num_list = list(range(2,246912))
Sort_list = []
for i in Num_list:
    if(isPrime(i)):
         Sort_list.append(i)

while(True):
    N = int(input())
    
    if(N == 0):
        break
    if(N == 1):
        print(1)
        continue
    arr = []
    for i in Sort_list:
        if N < i < N*2:
            arr.append(i)
    print(len(arr))
            
