class Graph:
    def __init__(self, G : dict = {}, terminals : set = set()) -> None:
        self.map = G
        self.N = len(self.map)
        self.unvisited = set(i for i in range(self.N))
        self.visited = set()
        self.terminals = terminals

    def cost(self) -> int:
        return len(self.map)

    def is_connected(self) -> bool:
        if not self.map:
            return False

        start = next(iter(self.map))

        visited = {start}
        queue = [i for i in self.map[start]]

        while queue:
            v = queue.pop()
            visited.add(v)
            queue.extend(i for i in self.map[v] if i not in visited)

        return len(visited) == len(self.map)
    
    def is_cycle(self):
        visited = set()
        
        def dfs(v, parent):
            visited.add(v)
            for neighbor in self.map[v]:
                if neighbor not in visited:
                    if dfs(neighbor, v):
                        return True
                elif neighbor != parent:
                    return True
            return False
        
        for v in self.map.keys():
            if v not in visited:
                if dfs(v, None):
                    return True
        
        return False

    def containsAllTerminals(self):
        for terminal in self.terminals:
            if terminal not in self.map:
                return False
        
        return True

    def is_valid_output(self):
        if not self.is_connected():
            return False
        
        if self.is_cycle():
            return False
        
        if not self.containsAllTerminals():
            return False
        
        return True
            
    def removeV(self, v):
        neigbors = self.map.pop(v)
        for n in neigbors:
            self.map[n].remove(v)
        self.N -= 1

    def numUnknown(self):
        return len(self.unvisited)

    def getNextUnknown(self):
        v = self.unvisited.pop()
        self.visited.add(v)

        return v
    
    def preProcess(self):
        # Remove terminals from removal candidates
        self.unvisited -= self.terminals

        # Remove vertices that are the only neighbor of a 
        # terminal from set of canditates
        to_remove = []
        for v in self.map:
            neighbors = self.map[v]
            if v in self.terminals:
                if len(neighbors) == 1:
                    self.unvisited.remove(next(iter(neighbors)))
            elif len(neighbors) == 1:
                to_remove.append(next(iter(neighbors)))

        for v in to_remove:
            if v in self.map:
                self.removeV(v)
            if v in self.unvisited:
                self.unvisited.remove(v)