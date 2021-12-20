import collections

N = int(input())

que = collections.deque([])
ans = []
for i in range(N):
    arr = list(map( str, input().split()))
    ans.append(arr)

for i in range(len(ans)):
    if ans[i][0] == 'push_front':
        que.appendleft(ans[i][1])
    elif ans[i][0] == 'push_back':
        que.append(ans[i][1])
    elif ans[i][0] == 'pop_front':
        if len(que) == 0:
            print(-1)
        else:
            print(que.popleft())
    elif ans[i][0] == 'pop_back':
        if len(que) == 0:
            print(-1)
        else:
            print(que.pop())
    elif ans[i][0] == 'size':
        print(len(que))
    elif ans[i][0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif ans[i][0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    else:
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
