# implementing deque in python
# A data structure from where items could be removed from either side


class Deque:
    """
    Deque class. Here front is the last element of the list and rear is the first element of the list
    """
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addRear(self, item):
        self.items.insert(0, item)

    def addFront(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


def palchecker(aString):
    deque = Deque()
    for i in aString:
        deque.addRear(i)

    while deque.size() > 1:
        f = deque.removeFront()
        r = deque.removeRear()
        if f != r:
            return False

    return True


print(palchecker("lsdkjfskf"))
print(palchecker("radar"))

# Another naive way to implement palindrome is to put all characters in a list,
# pop characters from the list and append to a new one and then compare if the two lists have the same characters