# DSA Final Project Report: Graph Algorithm Visualizer
Group Members: Michelle Ong, Nicole Lai

This project aims to implement and visualise several graph algorithms.
In particular, the algorithms implemented are pathfinding algorithms, i.e. given a start and end node in the graph, we want to find the shortest path from the start to the end node.
This is sometimes known as the single-pair shortest path problem.

## How to run
Prerequisites: pygame.

To start the application, simply run `main.py`.
- You may select any of the three algorithms by clicking on the buttons.
- Left click on the grid to add the start position (orange), end position (turquoise), and barriers (black). Right click to remove individual squares.
- Once you are satisfied with the setup, press `SPACE` to start the algorithm visualisation.
  - Green squares represent nodes which are to be visited 'next', in the context of the algorithm. Red squares represent nodes which have already been visited. The final path found by the algorithm is reconstructed in purple.
- To clear everything on the grid and select an algorithm again, press `c`.
- To reset the path and choose a different algorithm while keeping the start, end, and barriers, press `r`.

## Algorithms Implemented
1. **Dijkstra Algorithm**: a single-source shortest-path algorithm which, in its most general form, works on digraphs with unbounded non-negative weights.
   It is the fastest known algorithm for such arbitrary graphs, but for special cases (e.g. integer weights, undirected graphs, or additional information is available as we allow here in the form of the heuristic function), other algorithms can have better time complexity.

2. **A* Algorithm**: a single-pair shortest-path algorithm which builds on Dijkstra's algorithm, but also incorporates a heuristic function $h(n)$ which helps to narrow down the search space, or at least to prioritise those paths which are most likely to lead to shorter paths. 
   We chose the Manhattan distance as the heuristic function

3. **Fringe Search**: 





In your README.md, include:

Descriptions of algorithms implemented.
Encountered issues or challenges.
Instructions on code execution.

[If applicable] Methodology and findings from the bonus challenge of beating Python’s built-in algorithms.

Any extra information you would like to share with me.
List the names of all group members, or your own name if you are a solo participant.