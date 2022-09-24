
#BINARY SEARCH TREE IMPLEMENTATION

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

    #SEARCHING

    def search(self,key):
        if self.data==key:
            print(key," is Found")
            return
        elif self.data>key:
            if self.left:
                self.left.search(key)
            else:
                print(key,"is not found")
        else:
            if self.right:
                self.right.search(key)
            else:
                print(key,"is not found")



root=Node(30)
root.insert(12)
root.insert(20)
root.insert(45)
root.insert(36)
root.insert(56)
root.insert(6)
root.insert(40)
root.display()
print("/n")
key=int(input("Enter key value"))
root.search(key)
