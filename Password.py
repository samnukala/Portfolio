#  File: password.py
#  Name: Samanvitha Nukala


import sys


class Link (object):
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList (object):
    
    # create a linked list
    def __init__(self):
        self.first = None

    # helper function to add an item at the end of a list
    def insert_last(self, data):
        newLink = Link(data)
        current = self.first

        if current is None:
            self.first = newLink
            return

        while current.next is not None:
            current = current.next

        current.next = newLink

    # helper function to copy the contents of the current linked list
    # returns new linked list
    def copy_list(self):
        new_list = LinkedList()
        curr = self.first
        while curr:
            new_list.insert_last(curr.data)
            curr = curr.next
        return new_list

    # helper function to count number of links
    # returns number of links
    def num_links(self):
        curr = self.first
        res = 0
        while curr:
            res += 1
            curr = curr.next
        return res

    # string representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        curr_items = []
        curr = self.first
        res = ""
        while curr:
            curr_items.append(curr.data)
            if len(curr_items) == 10:
                res += "  ".join(map(str, curr_items)) + "\n"
                curr_items = []
            curr = curr.next
        # print the remaining items
        if len(curr_items):
            res += "  ".join(map(str, curr_items))
        return res

    def delete_link(self, data):
        previous = self.first
        current = self.first

        if current is None:
            return None

        while current.data is not data:
            if current.next is None:
                return None
            else:
                previous = current
                current = current.next

        if current == self.first:
            self.first = self.first.next
        else:
            previous.next = current.next

        return current

    # return a new linked list that results from the rotation
    def rotate(self, r_step, times):

        # make sure old linked list is unchanged
        duplicate_list = self.copy_list()

        # length of initial password
        password_length = duplicate_list.num_links()

        # make sure r_step isn't greater than password length
        steps = r_step
        if steps > password_length:
            steps = steps % password_length

        # make sure password is long enough to be rotated
        if password_length <= 1:
            return duplicate_list

        for x in range(0, 2*times):
            current = duplicate_list.first
            previous = None
            for y in range(0, steps):
                duplicate_list.delete_link(current.data)
                duplicate_list.insert_last(current.data)

        return duplicate_list


def main():

    # open file
    debug = False
    if debug:
        in_data = open('password.in')
    else:
        in_data = sys.stdin

    ll = LinkedList()
    data = list(map(int, in_data.readline().split()))

    # populate linked list with data
    for d in data:
        ll.insert_last(d)

    step, count = list(map(int, in_data.readline().split()))

    rotated = ll.rotate(step, count)
    # print the original list
    print(ll)
    # print the new list that results from calling rotate()
    print(rotated)


if __name__ == "__main__":
    main()
