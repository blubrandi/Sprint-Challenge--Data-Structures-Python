from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        else:
            if self.storage.length == self.capacity:
                item_to_delete = self.storage.head
                self.storage.remove_from_head()
                self.storage.add_to_tail(item)

                if item_to_delete == self.current:
                    self.current = self.storage.tail
            
            

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        current_head = self.current
        list_buffer_contents.append(current_head.value)

        if current_head.next != None:
            next_head = current_head.next
        else:
            next_head = self.storage.head
        
        while next_head != current_head:
            list_buffer_contents.append(next_head.value)

            if next_head.next != None:
                next_head = next_head.next
            else:
                next_head = self.storage.head

        return list_buffer_contents

# if the length of the list is not at capacity
# set the head of the list
# add the item to the tail of the list

# as items are added to the list, add them to the tail
# once the list is full, remove the head
# the next item in the list becomes the head

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
