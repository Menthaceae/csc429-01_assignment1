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

frontier = []
explored = []

def dfs(start, goal):
        frontier.append(start)
        result = dfsrecurs(goal)

        if result == 0:
                print("Path found from " + start.name + " to " + goal.name + " using DFS: ")
                for node in explored:
                        print(node.name, end=" ")
        elif result == 1:
                print("No solution found")
        else:
                print("Unkown error")            

        frontier.clear()
        explored.clear()

def dfsrecurs(goal):
        if not frontier: # No solution
                return 1
        else:
                removed = frontier.pop()
                if removed == goal: # Found solution
                        explored.append(removed)
                        return 0
                else: 
                        explored.append(removed)
                        for neighbor in removed.neighbors:
                                frontier.append(neighbor)

                        return dfsrecurs(goal)    

def bfs(start, goal):
        frontier.append(start)
        result = bfsrecurs(goal)

        if result == 0:
                print("Path found from " + start.name + " to " + goal.name + " using BFS: ")
                for node in explored:
                        print(node.name, end=" ")
        elif result == 1:
                print("No solution found")
        else:
                print("Unkown error")            

        frontier.clear()
        explored.clear()

def bfsrecurs(goal):
        if not frontier: # No solution
                return 1
        else:
                removed = frontier.pop(0)
                if removed == goal: # Found solution
                        explored.append(removed)
                        return 0
                else: 
                        explored.append(removed)
                        for neighbor in removed.neighbors:
                                frontier.append(neighbor)

                        return bfsrecurs(goal)                                      

dfs(A, E)
print("\n")
bfs(A, E)