# binary tree

class Treenode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
root = Treenode('1')
nodeA = Treenode('2')
nodeB = Treenode('3')
nodeC = Treenode('4')
nodeD = Treenode('5')
nodeE = Treenode('6')
nodeF = Treenode('7')

root.left = nodeA
root.right=nodeB
nodeA.left = nodeC
nodeA.right = nodeD
nodeB.right = nodeE
nodeB.right = nodeF



## preorder treversal

def preorder(node):
    if node is None:
        return
    print(node.data,end='-->')
    preorder(node.left)
    preorder(node.right)
print("preorder traversal of binary tree: ")
preorder(root)

# postorder traversal

def postorder(node):
   if node == None:
     return
   print(node.data, end="-->")
   postorder(node.right)
   postorder(node.left)
print(" \n")
print("postorder traversal in binary tree:")
postorder(root)

# inorder traversal

def inorder(node):
  if node is None:
    return
  inorder(node.left)
  print(node.data, end='-->')
  inorder(node.right)
print("\n")
print('inorder traversal in binary tree: ')
inorder(root)
