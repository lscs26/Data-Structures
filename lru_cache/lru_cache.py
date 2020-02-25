import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import (DoublyLinkedList, ListNode)

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        # amount of nodes it can hold
        self.limit = limit
        # current number of nodes it's holding
        self.size = 0
        # setting DoublyLinkedList as the value for self.LinkedList
        self.LinkedList = DoublyLinkedList()
        self.hashT = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # if there's no key to retrieve, return None
        if not self.hashT.get(key):
            return None
        else:
            # node is being created for the key
            node = self.hashT.get(key)
            # move the node to the beginning
            self.LinkedList.move_to_front(node)
            # get the value and return it
            return node.value

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # check if item already exists
        node = self.hashT.get(key)
        # check if node is none then put action
        if node is not None:
            node.value = value
            self.LinkedList.move_to_front(node)
        else: # if the node doesn't exist yet
            # if at capacity
            if self.size == self.limit:
                # remove from tail
                self.LinkedList.remove_from_tail()
                # decrement LRU cache size
                self.size -= 1
            
            # add to the hash table
            new_node = ListNode(value)
            self.hashT[key] = new_node

            # add to the beginning of the linked list
            self.LinkedList.add_to_head(new_node)

            # increment size of list
            self.size += 1