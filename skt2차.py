import heapq

def solution(arr, processes):
    answer = []
    # 읽기 -> 읽기 가능(쓰기 대기가 없을 경우), 쓰기 대기
    # 쓰기 -> 읽기 대기, 쓰기 대기

    # 대기에 쓰기가 읽기보다 먼저 실행해야함
    
    # 읽기 작업에서 읽은 내용과 전체 프로세스가 배열을 사용한 시간은 얼마나 되는지 알아보려 합니다.
    
    heap_doing = []

    for i in range(len(processes)):
        A = list(processes[i].split())
        processes[i] = A
    
    while processes:
        if processes[0][0] == 'write':  
            heap_doing.append([1, processes.pop(0)])  
        else:
            heap_doing.append([2, processes.pop(0)])  

    heap_doing = sorted(heap_doing, key = lambda X : (X[0], X[1][1], X[1][2]))

    heap_waiting = []

    times = [[] for _ in range(100000)]
        
    for a in range(len(times)):
        i = 0
        while heap_doing:
            if int(heap_doing[i][1][1]) <= a:
                # 배열에 읽기 작업을 수행 중인 경우, 새로운 읽기 요청 프로세스는 즉시 작업을 수행할 수 있습니다.
                if heap_doing[i][0] == 2: # read 일경우
                    is_bool = True
                    for tk in heap_waiting:
                        if tk[0] == 1:
                            is_bool = False
                    if is_bool == False:
                        break
                    
                    is_writed_in = False # Write 작업이 실행하고 있는지?
                    for k in times[a]:
                        if k[0] == 'write':
                            is_writed_in = True
                    # wirte 작업 중이라면 대기로
                    if is_writed_in:
                        break
                    else: # write작업이 없다면 바로 실행해주기
                        A = heap_doing.pop(i)
                        A = A[1]
                        
                        dense = ''
                        for z in range(int(A[3]), int(A[4]) + 1):
                            dense += arr[z]
                        answer.append(dense)
                        
                        for q in range(a, int(A[2]) + a):
                            times[q].append(A)
                        i -= 1

                else: # Write일 경우
                    if len(times[a]) != 0: # 작업이 있을경우
                        if heap_doing[i] not in heap_waiting:
                            heap_waiting.append(heap_doing[i])
                            i += 1
                        continue
                    else: # 실행시켜주기
                        if heap_doing[i] in heap_waiting:
                            heap_waiting.remove(heap_doing[i])
                        A = heap_doing.pop(i)
                        A = A[1]
                        
                        for q in range(a, int(A[2]) + a):
                            times[q].append(A)
                        
                        for z in range(int(A[3]), int(A[4])+1):
                            arr[z] = A[5]
                        break
            i += 1
            
            if len(heap_doing) <= i:
                break
        
            
    idx = 0    

    for i in range(len(times)):
        if times[i] != []:
            idx += 1
    
    answer.append(str(idx))
    idx = 0
        
    return answer

# ["24", "3415", "4922", "12492215", "13"]
print(solution(["1", "2", "4", "3", "3", "4", "1", "5"], ["read 1 3 1 2", "read 2 6 4 7", "write 4 3 3 5 2", "read 5 2 2 5", "write 6 1 3 3 9", "read 9 1 0 7"]))