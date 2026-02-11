frontier = []
explored = []
limit = 0

def dls(start, goal, limit):
    frontier.append(start)
    result = dlsrecurs(goal, limit, 0)

    if result == 0:
        print(f"Path found from {start.name} to {goal.name} using DLS with a limit of {limit}: ")
        for node in explored:
            print(node.name, end=" ")
    elif result == 1:
        print(f"No solution found with limit of {limit}. Printing path taken:")
        for node in explored:
            print(node.name, end=" ") 
    else:
        print("Unknown error")                 

    frontier.clear()
    explored.clear()

def dlsrecurs(goal, limit, currentDepth):    
    if not frontier: # No solution
        return 1
    
    currentNode = frontier.pop()
    explored.append(currentNode)
    
    if currentNode == goal: # Found solution
        return 0
    
    for neighbor in currentNode.neighbors:
        if neighbor not in explored and currentDepth < limit:
            frontier.append(neighbor)

    return dlsrecurs(goal, limit, currentDepth + 1)  