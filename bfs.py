class Node:
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors

F = Node("F", [])
E = Node("E", [])
D = Node("D", [F])
C = Node("C", [E])
B = Node("B", [C, D])
A = Node("A", [B])   

def goDownTheTree(node):
        print(node.name)
        print(node.neighbors)

        if node.neighbors:
                goDownTheTree(node.neighbors.pop())

goDownTheTree(A)
