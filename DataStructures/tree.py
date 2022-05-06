class TreeNode:
    def __init__(self, data):
       self.data = data
       self.children = []
       self.parent = None
 
    def add_child(self, child):
       # child is an instance of TreeNode class, and its parent is the current TreeNode
       child.parent = self
       self.children.append(child)
 
    def get_level(self):
       level = 0
       p = self.parent
       while p:
           level += 1
           p = p.parent
       return level
 
    # tree is recursive data structure; call print_tree recursively on child node
    def print_tree(self):
       spaces = ' ' * self.get_level() * 3
       # pretty-print with spacing if not root (if self.parent exists)
       prefix = spaces + "|--" if self.parent else ""
       print(prefix + self.data)
       if self.children:
           for child in self.children:
               child.print_tree()
 
 
def build_product_tree():
   # store "Electronics" in self.data
   root = TreeNode("Electronics")
 
   laptop = TreeNode("Laptop")
   laptop.add_child(TreeNode("Mac"))
   laptop.add_child(TreeNode("Thinkpad"))
   laptop.add_child(TreeNode("Dell"))
 
   cellphone = TreeNode("Cell Phone")
   cellphone.add_child(TreeNode("iPhone"))
   cellphone.add_child(TreeNode("Google Pixel"))
   cellphone.add_child(TreeNode("Nokia"))
 
   tv = TreeNode("TV")
   tv.add_child(TreeNode("Samsung"))
   tv.add_child(TreeNode("LG"))
 
   root.add_child(laptop)
   root.add_child(cellphone)
   root.add_child(tv)
 
   return root
 
 
if __name__ == '__main__':
   root = build_product_tree()
   root.print_tree()
 
