class Node:
    def __init__(self, data):
        self.data = data      
        self.left = None      
        self.right = None    


class BinaryTree:
    def __init__(self, root_data):
        self.root = Node(root_data)  


tree = BinaryTree(10)          
tree.root.left = Node(5)       
tree.root.right = Node(20)     
tree.root.left.left = Node(3)  
tree.root.left.right = Node(7) 
print(tree.root.data)             
print(tree.root.left.data)         
print(tree.root.right.data)        
print(tree.root.left.left.data)    
print(tree.root.left.right.data)