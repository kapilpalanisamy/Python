import os

class Console:
    @staticmethod
    def gotoxy(row, col):
        # ANSI escape code to move cursor
        print(f"\033[{row};{col}H", end='')

    @staticmethod
    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[H\033[2J", end='')  # Move cursor to top-left and clear
        
class ExprTree:
    class TreeNode:
        def __init__(self, ch):
            self.opera_tor_rand = ch
            self.left = None
            self.right = None
    
    class Listnode:
        def __init__(self,keep):
            self.safe=keep
            self.next=None
    class stack:
        def __init__(self):
            self.top=None
        def push(self,keepit):
            nn=ExprTree.Listnode(keepit)
            if self.top is None:
                self.top=nn
            else:
                nn.next=self.top
                self.top=nn
        def pop(self):
            giveback=self.top.safe
            self.top=self.top.next
            return giveback
        
    def isOperator(self,ch):
        return ch in "+-*/%^"
    
    def draw_tree(self, start, end, dispptr):
        if dispptr is not None:
            col = (end - start) // 2 + start
            Console.gotoxy(self.row, col)
            print(dispptr.opera_tor_rand, end='')
            self.row += 2
            self.draw_tree(start, (end + start) // 2, dispptr.left)
            self.draw_tree((end + start) // 2 + 1, end, dispptr.right)
            self.row -= 2
            
    def draw(self):
        Console.cls()
        self.row = 4
        self.draw_tree(1, 100, self.root)
    
    def __init__(self,postfix):
        self.root=None
        self.s=ExprTree.stack()
        
        #36+28+*82/35^**"
        for postFix_ind in range(len(postfix)):
            ch=postfix[postFix_ind]

            if self.isOperator(ch):
                nn=ExprTree.TreeNode(ch)
                nn.right=self.s.pop()
                nn.left=self.s.pop()
                self.s.push(nn)
            
            else:
                nn=ExprTree.TreeNode(ch)
                self.s.push(nn)
        self.root=self.s.pop()
    
    def solve(self):
        return self.solve_helper(self.root)
    
    def solve_helper(self,proc):
        
        if not self.isOperator(proc.opera_tor_rand):
            return int(proc.opera_tor_rand)
        
        leftval=self.solve_helper(proc.left)
        rightval=self.solve_helper(proc.right)

        if proc.opera_tor_rand == "+":
            return leftval+rightval
        elif proc.opera_tor_rand == "-":
            return leftval-rightval
        elif proc.opera_tor_rand == "*":
            return leftval*rightval
        elif proc.opera_tor_rand == "/":
            return leftval//rightval
        elif proc.opera_tor_rand == "%":
            return leftval%rightval
        elif proc.opera_tor_rand == "^":
            return leftval**rightval
        else:
            return 0

class treetester:
    @staticmethod
    def main():
        postFix = "36+28+*82/35^**"
        ourtree=ExprTree(postFix)
        ourtree.draw()
        res = ourtree.solve()
        print(f"\nres = {res}")
        
if __name__=="__main__":
    treetester.main()
        
