class Node:
    def __init__(self, ID, p = None, n = None):
        self.ID = ID
        self.p = p
        self.n = n


class Queue:
    def __init__(self):
        self.first_node = Node(0)
        self.last_node = Node(float("inf"))
        self.size = 0
        self.first_node.n = self.last_node
        self.last_node.p = self.first_node

    def push(self, n):
        curr_node = Node(n, self.last_node.p, self.last_node)
        self.last_node.p.n = curr_node
        self.last_node.p = curr_node
        if self.size == 0:
            self.first_node.n = curr_node
        self.size += 1
    
    def pop(self):
        if self.size == 0:
            print("You can't pop.")
            return
        popped = self.first_node.n.ID
        self.first_node.n = self.first_node.n.n
        self.size -= 1
        return popped

    def __len__(self):
        return self.size


q = Queue()
