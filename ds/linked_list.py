class Node:
    """
    Class for the Node to implement linked list
    """
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, newdata):
        self.data = newdata

    def set_next(self, newnext):
        self.next = newnext


class UnorderedList:
    """
    Unordered list
    """
    def __init__(self):
        self.head = None
        self.last_node = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        if self.head is None:
            self.head = temp
            self.last_node = temp
        else:
            temp.set_next(self.head)
            self.head = temp

    def size(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self.head

        while current is not None:
            if current.get_data() == item:
                return True
            else:
                current = current.get_next()

        return False

    def remove(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.get_data() == item:
                if previous is None:
                    self.head = current.get_next()
                    if current.get_next() is None:
                        self.last_node = self.head
                    return None
                else:
                    previous.set_next(current.get_next())
                    if current.get_next() is None:
                        self.last_node = previous
                    return None
            else:
                previous = current
                current = current.get_next()

    def append_O_n(self, item):
        newitem = Node(item)
        current = self.head

        if current is None:
            self.head = newitem
            return None

        while current is not None:
            if current.get_next() is None:
                current.set_next(newitem)
                return None
            else:
                current = current.get_next()

    def append(self, item):
        newitem = Node(item)
        self.last_node.set_next(newitem)
        self.last_node = newitem



list = UnorderedList()
list.add(1)
list.add(2)
list.add(3)
print(list.size())
print(list)
print(list.search(4))
print(list.search(2))
list.remove(2)
print(list.size())
list.append(4)
print(list.search(4))
print(list.size())
list.append(5)
list.append(6)
list.append(7)
print(list.size())

