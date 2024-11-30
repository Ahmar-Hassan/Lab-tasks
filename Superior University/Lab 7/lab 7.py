class Node:
    def __init__(self, value, x, y):
        self.value = value     
        self.x = x             
        self.y = y             
        self.g = float('inf')   
        self.h = 0              
        self.f = float('inf')   
        self.parent = None     
def heuristic(node, goal):
    
    return abs(node.x - goal.x) + abs(node.y - goal.y)

def a_star_algorithm(start, goal, graph):
    open_set = [start]  
    closed_set = set() 

    start.g = 0
    start.h = heuristic(start, goal)
    start.f = start.g + start.h

    while open_set:
        
        current = min(open_set, key=lambda node: node.f)

        if current == goal:
          
            path = []
            while current:
                path.append(current.value)
                current = current.parent
            return path[::-1] 

        open_set.remove(current)
        closed_set.add(current)

       
        for neighbor, cost in graph[current.value]:
            if neighbor in closed_set:
                continue

            tentative_g = current.g + cost
            if neighbor not in open_set:
                open_set.append(neighbor)
            elif tentative_g >= neighbor.g:
                continue

           
            neighbor.parent = current
            neighbor.g = tentative_g
            neighbor.h = heuristic(neighbor, goal)
            neighbor.f = neighbor.g + neighbor.h

    return None 


n1, n2, n3, n4, n5 = Node(1, 0, 0), Node(2, 1, 0), Node(3, 2, 0), Node(4, 1, 1), Node(5, 2, 1)
graph = {
    1: [(n2, 1), (n4, 1)],
    2: [(n3, 1), (n4, 1)],
    3: [(n5, 1)],
    4: [(n5, 1)],
    5: []
}


start, goal = n1, n5
path = a_star_algorithm(start, goal, graph)
print("Shortest Path:", path) 
