"""
Stack() creates a new stack that is empty. It needs no parameters and returns an empty stack.
push(item) adds a new item to the top of the stack. It needs the item and returns nothing.
pop() removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
peek() returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.
isEmpty() tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
size() returns the number of items on the stack. It needs no parameters and returns an integer.
"""

class Stack():

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def isEmpty(self):
        return (self.items == [])

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

def testParantheses(chaine):
    pile = Stack()
    for p in chaine:
        if p == "(":
            pile.push(1)
        else:
            if pile.isEmpty():
                return False
            pile.pop()
    if pile.isEmpty():
        return True
    return False

print(testParantheses("()()("))

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval('7 8 + 3 2 + /'))

"""
Queue() creates a new queue that is empty. It needs no parameters and returns an empty queue.
enqueue(item) adds a new item to the rear of the queue. It needs the item and returns nothing.
dequeue() removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.
isEmpty() tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
size() returns the number of items in the queue. It needs no parameters and returns an integer.
"""

class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
