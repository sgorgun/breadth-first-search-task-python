"""Template for programming assignment: check if undirected graph has at least one cycle."""
from typing import Dict, List


def check_cycle_existence(n: int, edges: Dict[int, List]) -> bool:
    """
    Returns True if there is at least one cycle in the undirected graph.
    Vertices are enumerated from 0 to N-1, there N - number of vertices.

    E.g. there is graph with 6 vertices from 0 to 5 and edges {{0,1}, {1,5}, {5,0}, {3,4}},
    expected result is True because there is a cycle 0 - 1 - 5 - 0.

    Parameters:
        n (int) : number of vertices in the graph, vertices are enumerated from 0 to n-1
        edges (Dict[int, List]): adjacency dictionary which stores list of adjacent vertices for each vertex
    Returns:
        bool: True if there is a cycle in the undirected graph, otherwise False
    """
    pass


