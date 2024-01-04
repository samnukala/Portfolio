#  File: BalanceFactor.py
#  Name: Samanvitha Nukala

import sys


# Node class that defines items in the Tree
class Node(object):
    
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BST(object):
    
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data.lower())
        else:
            self.insert_helper(self.root, data.lower())

    def insert_helper(self, node, data):
        # Compare the new value with the parent node
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert_helper(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert_helper(node.right, data)

    def getSpaces(self, num):
        spaces = ""
        for i in range(num):
            spaces += "    "
        return spaces

    # Print the tree
    def printTree(self):
        if (self.root is None):
            return
        else:
            self.printTreeHelper(self.root)

    def printTreeHelper(self, node, level=0):
        if node.right:
            self.printTreeHelper(node.right, level+1)
        print(self.getSpaces(level), node.data)
        if node.left:
            self.printTreeHelper(node.left, level+1)

    # Find the height of the given node.
    def getHeight(self, node):

        # If there is no node, the default height is -1
        if node is None:
            return -1
        else:
            # The height of the node is taken recursively to take into account child nodes
            left_height = self.getHeight(node.left)
            right_height = self.getHeight(node.right)
            # The greater height from either the left or right subtree is used for the height
            return 1 + max(left_height, right_height)

    # Return the integer balance factor of a tree with the given root node.
    def balance_factor(self, node):

        # if there are no child nodes the default balance factor is -1
        left_height = -1
        if node.left is not None:
            left_height = self.getHeight(node.left)
        # if there are no child nodes the default balance factor is -1
        right_height = -1
        if node.right is not None:
            right_height = self.getHeight(node.right)
        # Balance factor is found by subtracting left subtree height from right subtree height
        return right_height - left_height

def main():
    
    # data_in = ''.join(sys.stdin.readlines())
    # node = pickle.loads(str.encode(data_in))

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('bfactor.in')
    else:
        in_data = sys.stdin

    list = in_data.readline().split(" ")

    myTree = BST()

    for item in list:
        myTree.insert(item)

    #print("Tree: (tree is sideways with root on the left)")
    #myTree.printTree()

    print(myTree.balance_factor(myTree.root))


if __name__ == "__main__":
    main()
