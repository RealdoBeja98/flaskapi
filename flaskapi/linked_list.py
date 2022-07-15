class Node:
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
        
    def to_list(self):
        list = []
        if self.head is None:
            return list

        node = self.head
        while node:
            list.append(node.data)
            node = node.next_node
        return list

    def print_linked_list(self):
        linked_list = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            linked_list += f" {str(node.data)} ->"
            node = node.next_node
        
        linked_list += " None"
        print(linked_list)
    
    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head

        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_beginning(data)
            return
             
        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node
