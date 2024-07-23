# Creating a stack
def stack():
    stack=[]
    return stack

#create an empty stack
def empty(stack):
    return len(stack)==0
# for add element in stack
def push(stack,item):
    stack.append(item)
    print("pushed item :",item)

#remove element from stack
def pop(stack):
    if(empty(stack)):
        return "stack is empty"
    return stack.pop()

stac=stack()
push(stac,1)
push(stac,2)
push(stac,5)
pop(stac)
print("poped items: ",pop(stack()))
print("stack after poping element",str(stack))