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


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 18, 4]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.search(400))

    #Binary search containing string
    countries = ["India", "Pakistan", "Germany", "USA", "China", "UK", "USA"]
    country_tree = build_tree(countries)

    print ("UK is in the list?", country_tree.search("UK"))
    print ("Sweden is in the list", country_tree.search("Sweden"))

    print (country_tree.in_order_traversal())
