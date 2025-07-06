class stack_node():
    def __init__(self,ch):
        self.ch=ch
        self.next=None

class stack():
    def __init__(self):
        self.top=None
        
    def push(self,keep):
        nn=stack_node(keep)
        if self.top is None:
            self.top=nn
        else:
            nn.next=self.top
            self.top=nn
    def peek(self):
        return self.top.ch
    def pop(self):
        a=self.top.ch
        self.top=self.top.next
        return a
    def isEmpty(self):
        return self.top == None
    
def prec(ch):
    if ch in "+-":
        return 10
    elif ch in "*%/":
        return 20
    elif ch in "^":
        return 30
    else:
        return 0
def precedence(ch1,ch2):
    return prec(ch1)-prec(ch2)
def isOperator(ch):
    return ch in "+-*/%^"
def isScope(ch):
    return ch in "()"
def converter(infix):
    my_stack = stack()
    out_str = ""
    #"abxh(dkvjdhfuiv)dics"
    for inFix_ind in range(0,len(infix)):
        ch=infix[inFix_ind]
        if isOperator(ch) == False and isScope(ch)==False:
            out_str=out_str+ch
        else:
            if my_stack.isEmpty()==True or ch=="(":
                my_stack.push(ch)
            else:
                if ch==")":
                    while my_stack.peek() != "(":
                        out_str =out_str+my_stack.pop()
                    my_stack.pop()
                    
                else:
                    if my_stack.isEmpty()==False and precedence(ch,my_stack.peek())<=0:
                        out_str =out_str+my_stack.pop()
                    my_stack.push(ch)
    while my_stack.isEmpty==False:
        out_str=out_str+my_stack.pop()
    return out_str


if __name__=="__main__":
    in_str = "a+b*(c^d-e)^(f+g*h)-i"
    a=converter(in_str)
    print(in_str)
    print(a)
    
                        
                
