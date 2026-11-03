class Node:
    def __init__(self):
        self.data,self.left,self.right = None,None,None
    def __init__(self,data):
        self.data = data
        self.left,self.right = None,None

class Tree:
    def __init__(self):
        self.root = None

    def constructFromInorderPostorder(self, postOrder, inOrder,root = None):
        postIndex = postOrder.index(inOrder[-1])
        for x in inOrder:
            if postIndex < postOrder.index(x):
                postIndex = postOrder.index(x)
        print(postOrder[postIndex],postOrder,inOrder)
        root = Node(postOrder[postIndex])
        inIndex = inOrder.index(postOrder[postIndex])
        if len(inOrder[:inIndex]):
            print("left -> ",postOrder,inOrder[:inIndex])
            root.left = self.constructTree(postOrder, inOrder[:inIndex])
    
        
        if len(inOrder[inIndex+1:]):
            print("right -> ",postOrder,inOrder[inIndex+1:])
            root.right = self.constructTree(postOrder, inOrder[inIndex+1:])
        
        return root
    def constructFromInorderPreorder(self, preOrder, inOrder,root = None):
        preIndex = preOrder.index(inOrder[0])
        for x in inOrder:
            if preIndex > preOrder.index(x):
                preIndex = preOrder.index(x)
        print(preOrder[preIndex],preOrder,inOrder)
        root = Node(preOrder[preIndex])
        inIndex = inOrder.index(preOrder[preIndex])
        if len(inOrder[:inIndex]):
            print("left -> ",preOrder,inOrder[:inIndex])
            root.left = self.constructTree(preOrder, inOrder[:inIndex])
    
        
        if len(inOrder[inIndex+1:]):
            print("right -> ",preOrder,inOrder[inIndex+1:])
            root.right = self.constructTree(preOrder, inOrder[inIndex+1:])
        
        return root
    
    def constructTree(self, preOrPostOrder, inOrder):
        self.root = self.constructFromInorderPostorder(preOrPostOrder,inOrder)
        return self.root
    
    def inorder(self,root = None):
        if root == None:
            self.inorder(self.root.left)
            print(self.root.data,end=',')
            self.inorder(self.root.right)

        if root!=None:
            if root.left!=None:
                self.inorder(root.left)
            print(root.data,end=',')
            if root.right != None:
                self.inorder(root.right)

    def preorder(self, root = None):
        if root == None:
            print(self.root.data,end=',')
            self.preorder(self.root.left)
            self.preorder(self.root.right)

        if root!=None:
            print(root.data,end=',')
            if root.left!=None:
                self.preorder(root.left)
            if root.right != None:
                self.preorder(root.right)
    def postorder(self, root = None):
        if root == None:
            self.postorder(self.root.left)
            self.postorder(self.root.right)
            print(self.root.data,end=',')

        if root!=None:
            if root.left!=None:
                self.postorder(root.left)
            if root.right != None:
                self.postorder(root.right)
            print(root.data,end=',')

# preOrder = [1,2,4,8,9,10,11,5,3,6,7]
# inOrder = [8,4,10,9,11,2,5,1,6,3,7]
# postOrder = [8,10,11,9,4,5,2,6,7,3,1]
# tree = Tree()
# tree.constructTree(postOrder,inOrder)
# print()
# tree.inorder()
# print()

# tree.preorder()
# print()

# tree.postorder()



