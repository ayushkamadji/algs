from typing import List, TypeVar
from edge import Edge

T = TypeVar("T")

class Graph:
    def __init__(self, V: int) -> None:
        self.V = V  
        self.adj = [[] for i in range(V)]
        self.edges = []

    def add_edge(self, e: Edge) -> None:
        v = e.either()
        w = e.other(v)
        self.adj[v].append(e)
        self.adj[w].append(e)
        self.edges.append(e)
    
    def adjacent_of(self, v: int) -> List[Edge]:
        return self.adj[v]

    def E(self) -> int:
        return len(self.edges)