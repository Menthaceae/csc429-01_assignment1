frontier = []
explored = []

def bfs(start, goal):
    frontier.append(start)
    result = bfsrecurs(goal)

    if result == 0:
        print(f"Path found from {start.name} to {goal.name} using BFS: ")
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
    
    currentNode = frontier.pop(0)
    explored.append(currentNode)
    
    if currentNode == goal: # Found solution
        return 0
    
    for neighbor in currentNode.neighbors:
        if neighbor not in explored:
            frontier.append(neighbor)

    return bfsrecurs(goal)