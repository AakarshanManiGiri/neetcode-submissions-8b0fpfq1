class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        intstack = []
        for e in tokens:
            if e == '+':
                intstack.append(intstack.pop()+intstack.pop())
            elif e == '-':
                a,b = intstack.pop(),intstack.pop()
                intstack.append(b -a )
            elif e == '*':
                intstack.append(intstack.pop()*intstack.pop())
            elif e == '/':
                a,b = intstack.pop(),intstack.pop()
                intstack.append(int(float(b)/a))
            else:
                intstack.append(int(e))
        return intstack[0]