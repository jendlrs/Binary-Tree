#1. find_min(): finds minimum element in entire binary tree
#2. find_max(): finds maximum element in entire binary tree
#3. calculate_sum(): calcualtes sum of all elements
#4. post_order_traversal(): performs post order traversal of a binary tree
#5. pre_order_traversal(): perofrms pre order traversal of a binary tree

class BinarySearchTreeNode:
    def __init__(self,data):
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
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]

    numbers_tree = build_tree(numbers)

    print("Min:",numbers_tree.find_min())
    print("Max:",numbers_tree.find_max())