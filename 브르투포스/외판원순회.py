def turn_bit(nth):
    return bin((1 << nth) -1)

def get_nth_bit(n, nth):
    return 1 if n & (1 << nth) else 0


print(get_nth_bit(100, 3))
print(turn_bit(7))

'''
정리하면 (1 << n)은 ‘n번째 비트를 켠다’는 의미이고 (1 << n) - 1은 ‘n개의 비트를 모두 켠다’가 된다. 이에 대한 이해를 바탕으로 다음 내용을 공부하자.
'''

def count_bit(n):
    print(n//2)
    return n % 2 + count_bit(n // 2) if n >= 2 else n

print('1000은 2진수로', bin(1000), '이고, 1의 개수는', count_bit(1000), '개입니다.')

'''
1000은 2진수로 0b1111101000 이고, 1의 개수는 6 개입니다.
'''
