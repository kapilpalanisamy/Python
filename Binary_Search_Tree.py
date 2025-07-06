import os
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Console:
    @staticmethod
    def gotoxy(row, col):
        print(f"\033[{row};{col}H", end="")

    @staticmethod
    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')

class Tree:
    def __init__(self):
        self.root=None
        self.no_of_nodes=0
        
    def add(self,num):
        nn=node(num)
        if self.root==None:
            self.root=nn
            self.no_of_nodes +=1
            return
        trav=self.root
        while True:
            if num < trav.data:
                if trav.left is None:
                    trav.left=nn
                    break
                trav=trav.left
            else:
                if trav.right is None:
                    trav.right=nn
                    break
                trav=trav.right
        self.no_of_nodes +=1
    def delete(self,del_num):
        #parent
        #Child 
        #runleft
        #prev
        child=self.root
        while child is not None and child.data!=del_num:
            parent=child
            if child.data<del_num:
                child=child.right
            else:
                child=child.left
        
        if child.left is not None and child.right is not None:
            prev=None
            runleft=child.right
            while runleft.left != None:
                prev=runleft
                runleft=runleft.left
            child.data=runleft.data
            if prev is not None:
                prev.left=runleft.right
            else:
                child.right=runleft.right
        elif self.root==child:
            if child.left is None:
                self.root=child.right
            else:
                self.root=child.left
        else:
            if parent.data<child.data:
                if child.left is None:
                    parent.right=child.right
                else:
                    parent.right=child.left
            else:
                if parent.left == child:
                    parent.left = child.left if child.left else child.right
                else:
                    parent.right = child.left if child.left else child.right
        self.no_of_nodes -=1
    def draw_tree(self, start, end, dispptr):
        if dispptr:
            col = (end - start) // 2 + start
            Console.gotoxy(self.row, col)
            print(f"{dispptr.data}", end="")
            self.row += 2
            self.draw_tree(start, (start + end) // 2, dispptr.left)
            self.draw_tree((start + end) // 2 + 1, end, dispptr.right)
            self.row -= 2

    def draw(self):
        Console.cls()
        self.row = 4
        self.draw_tree(1, 100, self.root)
        print("\n")  # Move cursor below tree
    def inorder(self):
        print()
        self.inorder_helper(self.root)
    def inorder_helper(self,proc):
        if proc==None:
            return
        self.inorder_helper(proc.left)
        print( proc.data,end=' ')
        self.inorder_helper ( proc.right )
    def preorder(self):
        print()
        self.preorder_helper(self.root)
    def preorder_helper(self,proc):
        if proc==None:
            return
        print(proc.data,end=' ')
        self.preorder_helper(proc.left)
        self.preorder_helper(proc.right)
    def postorder(self):
        print()
        self.postorder_helper(self.root)
    def postorder_helper(self,proc):
        if proc==None:
            return
        self.postorder_helper(proc.left)
        self.postorder_helper(proc.right)
        print(proc.data,end=' ')
# Tree Tester
a=Tree()
data = [40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45, 55, 65, 75]
for val in data:
    a.add(val)
print(a.no_of_nodes)
a.draw()
print("Inorder Traversal:")
a.inorder()
print("\nPreorder Traversal:")
a.preorder()
print("\nPostorder Traversal:")
a.postorder()
a.delete(20)
print("\nAfter deleting 20:")
a.draw()

        
    
    
