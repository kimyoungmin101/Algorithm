
# heap 클래스 구현 

from operator import le
from turtle import left


class heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
            return False
        
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        
        self.heap_array.append(data)
        
        inserted_idx = len(self.heap_array) - 1

        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
            inserted_idx = parent_idx
    
    def move_down(self, poped_idx):
        left_child = poped_idx * 2
        right_child = poped_idx * 2 + 1 
        # 1) 자식이 없을때 왼쪽 자식이 없는 경우, heap이니깐
        
        if left_child >= len(self.heap_array):
            return False # 바꾸지 않는다
        
        # 2) 자식이 한개인 경우 오른쪽 자식만 없을때
        elif right_child >= len(self.heap_array):
            if self.heap_array[left_child] > self.heap_array[poped_idx]:
                return True
            else:
                return False
        
        # 3) 자식이 두개인 경우
        else:
            if self.heap_array[left_child] > self.heap_array[right_child]:
                if self.heap_array[poped_idx] < self.heap_array[left_child]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[poped_idx] < self.heap_array[right_child]:
                    return True
                else:
                    return False

    def pop(self):
        if len(self.heap_array) <= 1:
            return None
        
        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1] # 마지막 데이터를 [1]에 넣어준다.
        del self.heap_array[-1]
        poped_idx = 1
        
        while self.move_down(poped_idx):
            left_child = poped_idx * 2
            right_child = poped_idx * 2 + 1 
            
            # Case2)
            if right_child >= len(self.heap_array):
                if self.heap_array[left_child] > self.heap_array[poped_idx]:
                    self.heap_array[left_child], self.heap_array[poped_idx] = self.heap_array[poped_idx], self.heap_array[left_child]
                    poped_idx = left_child
            # Case3) 자식이 두개인 경우
            else:
                if self.heap_array[left_child] > self.heap_array[right_child]:
                    if self.heap_array[poped_idx] < self.heap_array[left_child]:
                        self.heap_array[left_child], self.heap_array[poped_idx] = self.heap_array[poped_idx], self.heap_array[left_child]
                        poped_idx = left_child
                else:
                    if self.heap_array[poped_idx] < self.heap_array[right_child]:
                        self.heap_array[poped_idx], self.heap_array[right_child] = self.heap_array[right_child], self.heap_array[poped_idx]
                        poped_idx = right_child
        
        return returned_data


heap = heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)

print(heap.heap_array)
print(heap.pop())
print(heap.heap_array)
print(heap.pop())
print(heap.heap_array)
print(heap.pop())
print(heap.heap_array)