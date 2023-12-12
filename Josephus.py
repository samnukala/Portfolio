#  File: Josephus.py
#  Name: Samanvitha Nukala

import sys

# This class represents one soldier.
class Link(object):
    
    # Constructor
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class CircularList(object):
    
    # Constructor
    def __init__(self):
        self.first = None
        self.last = None

    # Is the list empty
    def is_empty(self):
        return self.first is None

    # Append an item at the end of the list
    def insert(self, data):
        new_item = Link(data)   #create node
        if self.is_empty():
            self.first = new_item
            self.last = new_item    #set first and last to node
        else:
            current_last = self.last
            current_last.next = new_item
            self.last = new_item    #add to end, connect previous last to node

        new_item.next = self.first  #keep circular

    # Find the node with the given data (value)
    # or return None if the data is not there
    def find(self, data):
        current = self.first
        if self.first is None:  #empty list, return None
            return None
        while True:
            if current.data == data:    #found node
                return current

            current = current.next  #go to next node

            if current == self.first:   #cycled back to first, data is not in list
                return None

    # Delete a Link with a given data (value) and return the node
    # or return None if the data is not there
    def delete(self, data):
        node = self.find(data)

        if node is None:
            return None
        elif self.first == self.last:   #list with one node, set first and last to None for deletion
            self.first = None
            self.last = None
            return node

        current = self.first
        next_node = current.next

        while True:
            if next_node == node: #loop finds node before deletion node
                current.next = next_node.next   #connection skips deletion node
                if next_node == self.last:
                    self.last = current #reset self.last or self.first if necessary
                elif next_node == self.first:
                    self.first = next_node.next
                return next_node
            current = next_node
            next_node = current.next

    # Delete the nth node starting from the start node
    # Return the data of the deleted node AND return the
    # next node after the deleted node in that order
    def delete_after(self, start, step):
        current = start

        for i in range(step - 2):   #find node before deletion node
            current = current.next

        next_node = current.next    #save deletion node and call delete
        self.delete(next_node.data)

        return next_node.data, current.next

    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__(self):
        out = "["
        current = self.first
        if current is None: #empty list, just brackets
            return "[]"
        while True:
            if current == self.last:
                out += str(current.data) + "]"
                break
            else:
                out += str(current.data) + ", "
            current = current.next

        return out

# Input: Number of soldiers
# Outupt: Circular list with one link for each soldier
#         Data for first soldier is 1, etc.
def create_circular_list(num_soldiers):
    circular_list = CircularList()
    for i in range(1, num_soldiers + 1):
        circular_list.insert(i)

    return circular_list


# Input: circular list representing soldiers
#        data for the soldier to start with (1, 2...)
#        number of soldiers to count before identifying one to die
# Output: printed list of soldiers, in order they died
def process_Josephus(my_list, num_soldiers, start_data, step_count):
    node = my_list.find(start_data) #find starting node

    while True:
        if my_list.first == my_list.last:
            print(my_list.last) #print survivor
            break

        cycle = my_list.delete_after(node, step_count)
        print(cycle[0]) #print deleted node
        node = cycle[1] #set starting node to next node


def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('josephus.in')
        # in_data = open('autograde/test_cases/input_4.txt')
    else:
        in_data = sys.stdin

    # read the three numbers from the file
    line = in_data.readline().strip()
    num_soldiers = int(line)

    line = in_data.readline().strip()
    start_data = int(line)

    line = in_data.readline().strip()
    step_count = int(line)

    # Create cirular list
    my_list = create_circular_list(num_soldiers)

    # Kill off soldiers
    process_Josephus(my_list, num_soldiers, start_data, step_count)


if __name__ == "__main__":
    main()
