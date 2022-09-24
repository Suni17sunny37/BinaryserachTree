class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

    #INSERTION

    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
    
    #DISPLAY

    def display(self):
        if self.left:
            self.left.display()
        print(self.data,end=" ")
        if self.right:
            self.right.display()

root=Node(30)
root.insert(12)
root.insert(20)
root.insert(45)
root.insert(36)
root.insert(56)
root.insert(6)
root.insert(40)
root.display()