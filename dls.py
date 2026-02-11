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
        print("No solution found. Printing path taken:")
        for node in explored:
            print(node.name, end=" ")           

    frontier.clear()
    explored.clear()

def dlsrecurs(goal, limit, currentDepth):    
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
                if neighbor not in explored:
                    frontier.append(neighbor)

            return dlsrecurs(goal, limit, currentDepth + 1)  