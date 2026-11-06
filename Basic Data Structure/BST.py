from BinaryTree import Node, Tree

class BSTree(Tree):
    def __init__(self):
        self.root = None

    def __insertNode(self, data, root = None) -> Node:
        if root == None:
            root = Node(data)
        else:
            if data>root.data:
                root.right = self.__insertNode(data, root.right)
            else:
                root.left = self.__insertNode(data, root.left)
        return root
    def __findRootByData(self, root, data):
        if root == None:
            return None
        if root.left!=None and root.left.data == data:
            return root
        elif root.right!=None and root.right.data == data:
            return root
        else:
            rootLeft, rootRight = None, None
            if root.left != None:
                rootLeft = self.__findRootByData(root.left, data)
            if root.right != None:
                rootRight = self.__findRootByData(root.right, data)
            return rootLeft if rootLeft != None else rootRight
                  
    def __findMax(self, root):
        if root != None and root.left == None and root.right == None:
            return root
        rootLeft, rootRight = None, None
        if root.left != None:
            rootLeft =  self.__findMax(root.left) 
        if root.right!= None:
            rootRight = self.__findMax(root.right)
        if rootLeft == None:
            return rootRight
        if rootRight == None: 
            return rootLeft
        if rootLeft.data > rootRight.data:
            return rootLeft
        else:
            return rootRight
    
    def __findMin(self, root):
        if root != None and root.left == None and root.right == None:
            return root
        rootLeft, rootRight = None, None
        if root.left != None:
            rootLeft =  self.__findMin(root.left) 
        if root.right!= None:
            rootRight = self.__findMin(root.right)
        if rootLeft == None:
            return rootRight
        if rootRight == None: 
            return rootLeft
        if rootLeft.data < rootRight.data:
            return rootLeft
        else:
            return rootRight
    def insert(self, data):
        self.root = self.__insertNode(data,self.root)
        
    def delete(self,data):
        root = self.__findRootByData(self.root,data)
        maxNode, minNode = None, None
        if root.left!=None and root.left.data == data:
            rootLeft = root.left
            if rootLeft.left != None:
                maxNode = self.__findMax(root.left)
            elif rootLeft.right!= None:
                minNode = self.__findMin(root.right)
            else:
                root.left = None
                return
            node = maxNode
            if maxNode == None:
                node = minNode
            root.left = node
            root.left.left = rootLeft.left
            root.left.right = rootLeft.right

        else:
            rootRight = root.right
            if rootRight.left != None:
                maxNode = self.__findMax(root.left)
            elif rootRight.right!= None:
                minNode = self.__findMin(root.right)
            else:
                root.right = None
                return
            node = maxNode
            if maxNode == None:
                node = minNode
            root.left = node
            root.left.left = rootLeft.left
            root.left.right = rootLeft.right
        # if root == None:
        #     print(data, 'doesnt exist')
        #     return None
        # if root.Right == None and root.right == None:
        #     del root
        return root

    
list1 = [11,6,8,19,4,10,5,17,43,49,31]
tree = BSTree()
for x in list1:
    tree.insert(x)
tree.inorder()
print()
tree.preorder()
print()
tree.postorder()
print()

tree.preorder(tree.delete(4))
print()
tree.preorder()


