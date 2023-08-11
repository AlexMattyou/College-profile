# A class that represents the individual node in a BST.
class Node:
    def __init__(self, key):
        self.key = key
        self.l = None
        self.r = None
        
    def BST_search(self, find_key):
        if self.key == find_key:    
            print("Node is found")
            return
        if find_key < self.key:   
            if self.l:   
                self.l.BST_search(find_key)
            else:
                print("Node not found")
        else:
            if self.r:
                self.r.BST_search(find_key) 
            else:   
                print("Node not found")  

# Function to insert a new node with the given key.
def new_node(root, new_key):
    if root is None:
        root = Node(new_key)
        return root
    if new_key < root.key:
        root.l = new_node(root.l, new_key)
    else:
        root.r = new_node(root.r, new_key)
    return root

# Function to display the output of the tree
def display(root):
    if root:
        display(root.l)
        print(root.key, end=' ')
        display(root.r)

r = Node(50)
r = new_node(r, 30)
r = new_node(r, 20)
r = new_node(r, 40)
r = new_node(r, 70)
r = new_node(r, 60)
r = new_node(r, 80)

display(r)
print()
r.BST_search(20)
r.BST_search(80)
r.BST_search(100)