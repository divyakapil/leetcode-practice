from collections import defaultdict
from typing import List
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # build graph using adjacentcy list
        graph = defaultdict(list)
        for u, v in edges:  # since its an undirected graph, we will add both the directions u,v and v,u
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set() #to track the nodes that have been visited

        def dfs(node):
            if node == destination: #best case scenario
                return True
            visited.add(node) # update the visited 
            for neighbor in graph[node]: # check for neighbor
                if neighbor not in visited: #if neighbor is not visited set
                    if dfs(neighbor): # perform dfs recursion on that node
                        return True 
            return False # no path
        return dfs(source)
