from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n  

        for i in range(n):
            if color[i] == -1:
                queue = deque()
                queue.append(i)
                color[i] = 0  

                while queue:
                    
                    for i in range(len(queue)):
                        node = queue.popleft()

                        for neighbor in graph[node]:
                            if color[neighbor] == -1:
                                color[neighbor] = 1 - color[node]
                                queue.append(neighbor)
                            elif color[neighbor] == color[node]:
                                return False  

        return True
