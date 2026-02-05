class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add(self, nodes):
        for neighbor in nodes:
            self.neighbors.append(neighbor)