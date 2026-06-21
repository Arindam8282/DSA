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
                if(operatorStack.isEmpty() or self.precedence(ch)>self.precedence(operatorStack.top())):
                    operatorStack.push(ch)
                else:
                    while self.precedence(ch)<=self.precedence(operatorStack.top()):
                        expressionStack.push(operatorStack.pop())
            else:
                expressionStack.push(ch)

        while not operatorStack.isEmpty():
            expressionStack.push(operatorStack.pop())

        return expressionStack


ev = Eval()
ev.infixToPostfixStack("A+B*C/D").display()