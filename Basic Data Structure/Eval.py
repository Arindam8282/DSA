from Stack import Stack

class Eval:
    def __init__(self):
        pass

    def precedence(self,operator:str):
        if operator == '+' or operator == '-':
            return 1
        elif operator == 'X' or operator == '/' or operator == '*':
            return 2
        elif operator == '(' or operator == ')':
            return 3
        else:
            return False
    def infixToPostfixStack(self,infix:str)-> Stack:
        operatorStack = Stack()
        expressionStack = Stack()
        num = ''
        for ch in infix:
            if(self.precedence(ch)):
                if(num!=''):
                    expressionStack.push(num)
                    num = ''

                if(ch==")"):
                    while(operatorStack.top()!='('):
                        expressionStack.push(operatorStack.pop())
                    operatorStack.pop()
                else:
                    if(operatorStack.isEmpty() or (operatorStack.top()=="(" and self.precedence(ch)<self.precedence(operatorStack.top())) or self.precedence(ch)>self.precedence(operatorStack.top())):
                        operatorStack.push(ch)
                    else:
                        while self.precedence(ch)<=self.precedence(operatorStack.top()):
                            expressionStack.push(operatorStack.pop())
                        operatorStack.push(ch)
            else:
                num+=ch
        if num:
            expressionStack.push(num)

        while not operatorStack.isEmpty():
            expressionStack.push(operatorStack.pop())

        return expressionStack
    
    def infixToPrefixStack(self,infix:str)-> Stack:
        operatorStack = Stack()
        expressionStack = Stack()
        for ch in infix[::-1]:
            if(self.precedence(ch)):
                if ch=="(":
                    while operatorStack!=')':
                        expressionStack.push(operatorStack.pop())
                    operatorStack.pop()
                else:
                    if(operatorStack.isEmpty() or (operatorStack.top()==')' and self.precedence(ch)<self.precedence(operatorStack.top())) or self.precedence(ch)>=self.precedence(operatorStack.top())):
                        operatorStack.push(ch)
                    else:
                        while self.precedence(ch)>=self.precedence(operatorStack.top()):
                            expressionStack.push(operatorStack.pop())
                        operatorStack.push(ch)
            else:
                expressionStack.push(ch)
            
        while not operatorStack.isEmpty():
            expressionStack.push(operatorStack.pop())
        return expressionStack
    
    def postfixEvaluation(self,infix:str):
        expressionStack = self.infixToPostfixStack(infix)
        reverseStack = Stack()
        while not expressionStack.isEmpty():
            reverseStack.push(expressionStack.pop())
        while not reverseStack.isEmpty():
            if(not self.precedence(reverseStack.top())):
                expressionStack.push(reverseStack.pop())
            else:
                opt = reverseStack.pop()
                a = int(expressionStack.pop())
                b = int(expressionStack.pop())
                expressionStack.push(self.sum(b,a,opt))
        return expressionStack.top()
    
    def sum(self,a,b,opt):
        if opt=='+':
            return a + b
        elif opt=='-':
            return a - b
        elif opt=='*':
            return a * b
        else:
            return a / b



ev = Eval()
# ev.infixToPostfixStack("(A+B)*C/D").display()
# ev.infixToPostfixStack("A+B*C/D").display()
# ev.infixToPrefixStack("A+B*C/D").display(reverse=True)
print(ev.postfixEvaluation("12+3*(4-5)"))

