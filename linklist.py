class Node:
    def __init__(self,data):
        self.data = data #데이터 저장공간
        self.next = None #다음 노드를 가리키는 변수

class Linked_list:
    def __init__(self):
        self.head = None
        self.length = 0
    def __len__(self):
        return self.length
    def appendleft(self,data):#맨 처음에 삽입
        node = Node(data)
        if self.head is None: #만약 첫번쨰 노드면
            self.head = node #헤드에 노드의 주소를 붙임
        else:#만약 첫번째 노드가 아니라면
            node.next = self.head#새로만든 노드의 주소를 첫번째 노드에 붙이고
            self.head = node#헤드에 노드를 붙임
        self.length += 1#리스트의 길이 증가
    def append(self,data):
        node = Node(data) #새로운 노드 생성
        if self.head is None: #생성한 노드가 첫번째 노드라면
            self.head = node #헤드에 node의 주소를 붙임
        else :
            prev = self.head#처음 노드의 값
            while True:
                if prev.next is None:
                    prev.next = node
                    self.length += 1
                    break
                else:
                    prev=prev.next
                    self.length += 1
            prev.next = node
            
            node.next = None
            
    def display(self):
        if self.head is None:
            print("비어있는 리스트")
        else:
            node = self.head
            while node.next:
                print(node.data, end = "→")
                node = node.next
            print(node.data)
    def search(self,data):
        node = self.head
        while node:
            if node.data == data:
                return True
            node = node.next
            return False
        
        

mylist = Linked_list()
mylist.appendleft("A")
mylist.appendleft("B")
mylist.append("C")

mylist.display()