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
        if root.data == data:
            return root
        else:
            rootLeft = self.__findRootByData(root.left, data)
            if rootLeft == None and root.right != None:
                root = self.__findRootByData(root.right, data)
        return root
        
    def insert(self, data):
        self.root = self.__insertNode(data,self.root)
        
    def delete(self,data):
        root = self.__findRootByData(self.root,data)
        if root == None:
            print(data, 'doesnt exist')
            return None
        if root.left == None and root.right == None:
            del root
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
tree.delete(60)
tree.preorder()

