frontier = []
explored = []

def dfs(start, goal):
    frontier.append(start)
    result = dfsrecurs(goal)

    if result == 0:
        print(f"Path found from {start.name} to {goal.name} using DFS: ")
        for node in explored:
            print(node.name, end=" ")
    elif result == 1:
        print("No solution found.")
    else:
        print("Unkown error")            

    frontier.clear()
    explored.clear()

def dfsrecurs(goal):
    if not frontier: # No solution
        return 1
    
    currentNode = frontier.pop()
    explored.append(currentNode)
    
    if currentNode == goal: # Found solution
        return 0
    
    for neighbor in currentNode.neighbors:
        if neighbor not in explored:
            frontier.append(neighbor)

    return dfsrecurs(goal)    