import sys

# a queue class, tested and working
class Queue(object):
    
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)

    # checks the item at the top of the Queue
    def peek(self):
        return self.queue[0]

    # check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # return the size of the queue
    def size(self):
        return len(self.queue)


# Node class that defines items in the Tree
class Node(object):
    
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# The Binary Search Tree class
class BST(object):
    
    def __init__(self, int_list=None):
        self.root = None
        if int_list is not None:
            for num in int_list:
                self.insert(num)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_helper(self.root, data)

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
        print(self.getSpaces(level), node.data, "-----")
        if node.left:
            self.printTreeHelper(node.left, level+1)

    # Returns True if two BSTs are similar
    def is_similar(self, compTree):
        return self.similar_helper(self.root, compTree.root)

    def similar_helper(self, node_a, node_b):

        while node_a is not None and node_b is not None:
            # need to break out of the loop with a base case
            if node_a.data != node_b.data:
                return False
            elif node_a.data == node_b.data:
                # if first nodes are equal check the right and left children
                if self.similar_helper(node_a.left, node_b.left) is True:
                    if self.similar_helper(node_a.right, node_b.right) is True:
                        return True
                    else:
                        return False
                else:
                    return False

        # account for both trees being null
        if node_a is None and node_b is None:
            return True

    # Returns True if a BST is a complete tree
    def is_complete(self):

        complete_queue = Queue()
        complete_queue.enqueue(self.root)

        count = 0

        while complete_queue.is_empty() is False:
            check_node = complete_queue.dequeue()
            if check_node is not None:
                complete_queue.enqueue(check_node.left)
                complete_queue.enqueue(check_node.right)
            if check_node is None:
                # count will increase once the first null node is reached
                count += 1
            if count > 0 and check_node is not None:
                # after the first null node is reached they should all be null after that
                return False
        return True
    

# Debug flag - set to False before submitting
debug = False
if debug:
    in_data = open('bst_util.in')
else:
    in_data = sys.stdin

# read number of trees
numTrees = int(in_data.readline())
trees = []

# build list of trees
for i in range(numTrees):
    line = in_data.readline()
    line = line.strip()
    line = line.split()
    tree_input = list(map(int, line)) 	# converts elements into ints
    trees.append(BST(tree_input))
    if debug:
        trees[i].printTree()

# run utility methods
num_similar = 0
num_complete = 0
for i in range(numTrees):
    for j in range(i + 1, numTrees):
        if (i != j and trees[i].is_similar(trees[j])):
            num_similar += 1
    if (trees[i].is_complete()):
        num_complete += 1

print(num_similar)
print(num_complete)
