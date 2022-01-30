class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class NodeMgmt:
    def __init__(self, head):
        self.head = head
    
    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def serach(self, value):
        self.current_node = self.head

        while True:
            if self.current_node.value == value:
                return True
            elif self.current_node.value > value:
                if self.current_node.left == None:
                    break
                self.current_node = self.current_node.left
            else:
                if self.current_node.right == None:
                    break
                    
                self.current_node = self.current_node.right
        return False

    def delete(self, value):
        searched = False
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            if self.current_node == None:
                break
            if self.current_node.value == value:
                searched = True
                break
            else:
                if self.current_node.value > value:
                    self.parent = self.current_node
                    self.current_node = self.current_node.left
                else:
                    self.current_node = self.current_node.right
        
        if searched == False:
            return False
        
        ### 이후 부터 CASE 총 3개의 경우를 구현해야한다.

        # self.current.node가 삭제할 Node, self.parent는 삭제할 Node의 Parent Node인 상태

        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.current_node
            
        # 삭제할 노드가 자식을 한개 가지고 있을 때 ! 왼쪽 자식이냐 오른쪽 자식이냐 갈릴 수 있음
        if self.current_node.left != None and self.current_node.right == None: # 왼쪽 자식만 있을 경우
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left
        elif self.current_node.left == None and self.current_node.right != None: # 오른쪽 자식만 있을 경우
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

        # 삭제할 노드의 자식이 두개일 때,
        # CASE 1) 오른쪽 자식 중 가장 작은 값을 위로 올리는 경우 3-1
        if self.current_node.left != None and self.current_node.right != None:
            if value < self.parent.value:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node.parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.left = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right

        # CASE 2) 오른쪽 자식 중 가장 작은 값을 위로 올리는 경우 3-2
        else:
            self.change_node = self.current_node.right
            self.change_node_parent = self.current_node.right

            while self.change_node.left == None:
                self.change_node_parent = self.change_node
                self.change_node = self.change_node.left
            if self.change_node.right != None:
                self.change_node_parent.left = self.change_node.right
            else:
                self.change_node_parent.left = None
            self.parent.right = self.change_node
            self.change_node.left = self.current_node.left
            self.current_node.right = self.current_node.right
        del self.current_node

head = Node(1)

BST = NodeMgmt(head)
BST.insert(2)
BST.insert(3)
BST.insert(4)

print(BST.serach(4))
