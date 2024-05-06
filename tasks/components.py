"""Template for programming assignment: number of connected components."""
from typing import Dict, Set
from collections import deque

def find_number_of_components(n: int, edges: Dict[int, Set]) -> int:
    """
    Returns the number of connectivity components in an undirected graph.
    Vertices are enumerated from 0 to N-1, where N is the number of vertices.

    E.g. there is a graph with 6 vertices from 0 to 5 and edges {{0,1}, {1,5}, {5,0}, {3,4}},
    there are 3 connectivity components: {0, 5, 1}, {2}, {3,4}.
    Edges above will have the following 'adjacency dictionary' look: {0: {1,5}, 1: {0}, 3: {4}, 4: {3}, 5: {0}}.

    Parameters:
        n (int) : the number of vertices in the graph, vertices are enumerated from 0 to n-1
        edges (Dict[int, Set]): adjacency dictionary which stores a set of adjacent vertices for each vertex
    Returns:
        int: number of connectivity components in the given undirected graph
    """
    visited = set()
    components = 0

    for i in range(n):
        if i not in visited:
            components += 1
            queue = deque([i])
            while queue:
                vertex = queue.popleft()
                visited.add(vertex)
                for neighbor in edges.get(vertex, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
    return components
