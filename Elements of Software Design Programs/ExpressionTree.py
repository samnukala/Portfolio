#  File: ExpressionTree.py 
#  Name: Samanvitha Nukala

import sys

# list of valid operators
operators = ['+', '-', '*', '/', '//', '%', '**']


# Input: Elements of a simple expression
# Output: result of evaluation of the expression

def operation(operator, n, m):
    expression = str(n) + operator + str(m)
    return eval(expression)

# Stack Class
# Purpose: Traditional Stack implementation containing list of data items
# Used to keep track of items in nested expressions.

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if (not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0


# Node Class
# Purpose: Used by the Tree Class to represent one operand or operators
# in a binary expression. It includes data (a character) and
# two pointers, to the left and right child nodes.

class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild


# Tree Class
# Purpose: To represent the string representation of operators and operands
# of a binary expression, so it can be evaluated.

class Tree (object):
    def __init__(self):
        self.root = Node(None)

    # Input: a string expression
    # Output: an expression tree

    def create_tree(self, expr):
        current_node = self.root
        stack = Stack()
        token_strings = expr.split()

        for token in token_strings:
            if token == '(':
                current_node.lChild = Node(None)
                stack.push(current_node)
                current_node = current_node.lChild

            elif token in operators:
                current_node.data = token
                stack.push(current_node)
                current_node.rChild = Node(None)
                current_node = current_node.rChild

            elif token == ')':
                if stack.is_empty():
                    break
                else:
                    current_node = stack.pop()
            else:
                current_node.data = token
                current_node = stack.pop()

    # Input: A node in an expression tree
    # Output: The result of evaluating the expression with this node as the root

    def evaluate(self, current):
        if current is None:
            return None
        if current.data in operators:
            n = self.evaluate(current.lChild)
            m = self.evaluate(current.rChild)
            return operation(current.data, n, m)
        return float(current.data)

    # Starter Method for pre_order
    # Input: a node in an expression tree
    # Output: (string) the preorder notation of the expression
    # with this node at the root

    def pre_order(self, current):
        result = " "
        if current.data not in operators:
            return str(current.data)
        if current is not None:
            result = current.data
            result += ' '
            result += self.pre_order(current.lChild)
            result += ' '
            result += self.pre_order(current.rChild)
        return result

    # Starter Method for post_order
    # Input: a node in an expression tree
    # Output: (string) the post order notation of the expression
    # with this node at the root

    def post_order(self, current):
        result = " "
        if current.data not in operators:
            return str(current.data)
        if current is not None:
            result = ''
            result += self.post_order(current.lChild)
            result += ' '
            result += self.post_order(current.rChild)
            result += ' '
            result += current.data
        return result



def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('expression.in')
    else:
        in_data = sys.stdin

    # read infix expression
    line = in_data.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())


if __name__ == "__main__":
    main()
