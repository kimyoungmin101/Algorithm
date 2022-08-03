from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1
    
    L = len(weak)
    
    for i in range(L):
        weak.append(weak[i] + n)

    
    for start in range(L):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count - 1]
        
            for idx in range(start, start + L):
                if weak[idx] > position:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[idx] + friends[count - 1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer
