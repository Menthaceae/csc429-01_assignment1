frontier = []
explored = []

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
                            if neighbor not in explored:
                                frontier.append(neighbor)

                        return bfsrecurs(goal)