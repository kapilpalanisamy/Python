class PostToInfix:
    def __init__(self, postfix_expr):
        self.inFixStr = postfix_expr
        self.post_fix_str = ""
        self.convert()

    def is_operator(self, ch):
        return ch in "+-*/%^"

    def convert(self):
        s = self.Stack()
        for ch in self.inFixStr:
            if self.is_operator(ch):
                op2 = s.pop()
                op1 = s.pop()
                make_str = '(' + op1 + ch + op2 + ')'
                s.push(make_str)
            else:
                s.push(ch)
        self.post_fix_str = s.pop()

    def get(self):
        return self.post_fix_str

    class StackNode:
        def __init__(self, keep):
            self.keep = keep
            self.s_next = None

    class Stack:
        def __init__(self):
            self.top = None

        def push(self, to_stack):
            nn = PostToInfix.StackNode(to_stack)
            nn.s_next = self.top
            self.top = nn

        def pop(self):
            if self.top is None:
                return ""
            give_back = self.top.keep
            self.top = self.top.s_next
            return give_back


#=== Tester Class ===
class PostToInfixTester:
    @staticmethod
    def main():
        inFix1 = "abcd^e-fgh*+^*+i-"
        test1 = PostToInfix(inFix1)
        postFix1 = test1.get()
        print("Postfix:", inFix1)
        print("Infix:  ", postFix1)
        print()

        inFix2 = "36+28+*82/35^**"
        test2 = PostToInfix(inFix2)
        postFix2 = test2.get()
        print("Postfix:", inFix2)
        print("Infix:  ", postFix2)

#=== Run main ===
if __name__ == "__main__":
    PostToInfixTester.main()
