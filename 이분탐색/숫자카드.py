from sys import stdin, stdout


def LowerBound(left, right, target):
    while left < right: # left가 right보다 작을 때 까지 while문 실행
        mid = int((left + right)/2)
        # print ("{0} {1} {2} {3}".format(left, mid, right, target))
        if cards[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right


def UpperBound(left, right, target):
    while left < right:
        mid = int((left + right)/2)
        # print ("{0} {1} {2} {3}".format(left, mid, right, target))
        if cards[mid] <= target:
            left = mid + 1
        else:
            right = mid
        
    return right
 


N = int(input())
strCards = input()

cards = [int(i) for i in strCards.split(' ')]
cards.sort()

M = int(input())
strGuesses = input()



guesses = [int(i) for i in strGuesses.split(' ')]


for i in guesses:
    print ((UpperBound(0, N, int(i))) - LowerBound(0, N, int(i)), end = " ")
