class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
    
    def add(self, data):
        node = self.head

        while node.next:
            node = node.next

        node.next = Node(data)
    
    def desc(self): # 노드를 출력 하는 함수
        node = self.head

        while node:
            print(node.data)
            node = node.next

    def insert_data(self, data):
        node = self.head

        while node.next:
            if (node.data < data and node.next.data > data):
                cnt_node = Node(data)
                cnt_node.next = node.next
                node.next = cnt_node
                break
            
            node = node.next
            if node.next == None:
                node.next = Node(data)
                break

linkedList = NodeMgmt(0)


for data in range(1, 10):
    linkedList.add(data)

linkedList.insert_data(102)

linkedList.desc()
