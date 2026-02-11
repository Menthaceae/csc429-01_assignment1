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
                if neighbor not in explored:
                    frontier.append(neighbor)

            return dfsrecurs(goal)    