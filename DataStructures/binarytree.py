class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 
 
class BinaryTree:
   def __init__(self, root):
       self.root = Node(root)
 
   def print_tree(self, traversal_type):
       if traversal_type == "preorder":
           print(self.preorder_print(self.root, ""))
       elif traversal_type == "inorder":
           print(self.inorder_print(self.root, ""))
       elif traversal_type == "postorder":
           print(self.postorder_print(self.root, ""))
       else:
           print("traversal not supported")
 
   def preorder_print(self, start, traversal_str):
       # Root --> Left subtree --> Right subtree
       if start:
           traversal_str += str(start.value) + '-'
           traversal_str = self.preorder_print(start.left, traversal_str)
           traversal_str = self.preorder_print(start.right, traversal_str)
       return traversal_str
 
   def inorder_print(self, start, traversal_str):
       # Left subtree --> Root --> Right subtree
       if start:
           traversal_str = self.inorder_print(start.left, traversal_str)
           traversal_str += str(start.value) + '-'
           traversal_str = self.inorder_print(start.right, traversal_str)
       return traversal_str
 
   def postorder_print(self, start, traversal_str):
       # Left subtree --> Right subtree --> Root
       if start:
           traversal_str = self.postorder_print(start.left, traversal_str)
           traversal_str = self.postorder_print(start.right, traversal_str)
           traversal_str += str(start.value) + '-'
       return traversal_str
 
 
#           1
#          /  \
#        2      3
#       / \    /  \
#      4   5  6    7
if __name__ == '__main__':
   tree = BinaryTree(1)
   tree.root.left = Node(2)
   tree.root.right = Node(3)
   tree.root.left.left = Node(4)
   tree.root.left.right = Node(5)
   tree.root.right.left = Node(6)
   tree.root.right.right = Node(7)
 
   print('preorder traversal:')
   tree.print_tree("preorder")
   tree.print_tree("inorder")
