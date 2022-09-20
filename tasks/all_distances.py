"""Template for programming assignment: calculate minimum distance from given vertex to all vertices."""
from typing import Dict, List, Set


def calculate_all_distances_from_vertex(n: int, edges: Dict[int, Set], vertex: int) -> List:
    """
    Returns list with minimum distances from vertex to all vertices, including itself.
    If there is no path, please set distance to -1.
    Vertices are enumerated from 0 to N-1, there N - number of vertices.

    E.g. you have graph with 4 vertices from 0 to 3 and edges {{0,1}, {1,2}). Initial vertex is 2,
    excepted result is [2, 1, 0, -1]. 2 at the 1st position (index 0) means that 2 edges needed to get from vertex '2'
    to vertex '0': 2 -> 1 -> 0. At the 2nd position (index 1) there is 1 because vertices '1' and '2' are adjacent.
    0 is placed on the 3rd place (index 2) because it's starting point and list is finished with -1 because
    there is no path between vertices '2' and '3'.

    Parameters:
        n (int) : number of vertices in the graph, vertices are enumerated from 0 to n-1
        edges (Dict[int, Set]): adjacency dictionary which stores set of adjacent vertices for each vertex
        vertex (int): initial vertex
    Returns:
        List: distance list which reflects distance between initial vertex and all other vertices,
        number at each index I shows the distance from starting vertex to vertex I
    """
    pass
