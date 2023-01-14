#Create a demo using the letters in your fullname as the content of the binary tree.

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child (self, data):
        #If the value already exist
        if data == self.data:
            return 

        #If data is less than the value of current node --Add to left subtree
        if data < self.data:
            if self.left:
                self.left.add_child(data) 
            else:
                self.left = BinarySearchTreeNode(data)

        #If data is greater than the value of current node --Add to right subtree
        else:
            if self.right:
                self.right.add_child(data) 
            else:
                self.right = BinarySearchTreeNode(data)

    def search (self, val):
        if self.data == val:
            return True

        if val < self.data:
            #value might be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False #It means the value does not exist in the elements

        if val > self.data:
            #value might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False #It means the value does not exist in the elements

    def in_order_traversal(self):
        elements = []

        #Visit the left tree
        if self.left:
            elements += self.left.in_order_traversal()
        
        #Visit base node
        elements.append(self.data)

        #Visit the right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def post_order_traversal(self):
        elements = []

        #Visit the left tree
        if self.left:
            elements += self.left.post_order_traversal()
        
        #Visit the right tree
        if self.right:
            elements += self.right.post_order_traversal()
        
        #Visit the base node
        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data] #For base node

        #Visit the left tree
        if self.left:
            elements += self.left.pre_order_traversal()
        
        #Visit the right tree
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
        
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    letters_name = ["M", "A", "J", "E", "N", "S", "E", "N", "N", "I","C", "O","L", "E", "C", "D", "E", "L", "A", "R", "O", "S", "A"]
    letters_name_tree = build_tree(letters_name)

    print("\nInput Letters:", letters_name)
    print("\nIn order traversal:",letters_name_tree.in_order_traversal())
    print("\nPost order traversal:",letters_name_tree.post_order_traversal())
    print("\nPre order traversal:",letters_name_tree.pre_order_traversal())
    print("\nIs there letter M?",letters_name_tree.search("M")) 
    print("\nIs there letter W?",letters_name_tree.search("W")) 