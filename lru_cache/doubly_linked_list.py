"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        self.length += 1
        if not self.head and not self.tail:
            #Empty list, this is new head and tail
            self.head = self.tail = ListNode(value)
        else:
            #We know list is populated
            self.head.insert_before(value)
            self.head = self.head.prev

    def remove_from_head(self):
       #current node head
       value = self.head.value
       #deletes old head value
       self.delete(self.head)
       #returns new head value
       return value

    def add_to_tail(self, value):
        self.length += 1
        if not self.head and not self.tail:
            #Empty list, this is new head and tail
            self.head = self.tail = ListNode(value)
        else:
            #We know list is populated
            self.tail.insert_after(value)
            self.tail = self.tail.next

    def remove_from_tail(self):
        #current node tail
        value = self.tail.value
        #deletes old tail value
        self.delete(self.tail)
        #returns updated tail value
        return value

    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)

    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)#pointer untouched but still there

    def delete(self, node):
        # Planning
        # If LL is empty
        if not self.head and not self.tail:
            print("ERROR:  Attempted to delete node not in list")
            return
        # If node is head 
        # If node is both
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.next
            node.delete()
        # If node is tail
        elif node == self.tail:
            self.tail = self.tail.prev
            node.delete()
        # If node is in middle
        else:
            node.delete()
        self.length -= 1

    def get_max(self):
        pass
