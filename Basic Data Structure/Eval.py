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
        for ch in infix:
            if(self.precedence(ch)):
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
                expressionStack.push(ch)

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


ev = Eval()
ev.infixToPostfixStack("(A+B)*C/D").display()
ev.infixToPostfixStack("A+B*C/D").display()
ev.infixToPrefixStack("A+B*C/D").display(reverse=True)

