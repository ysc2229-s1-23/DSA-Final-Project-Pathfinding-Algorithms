# DSA Final Project Report: Graph Algorithm Visualizer
Group Members: Michelle Ong, Nicole Lai

This project aims to implement and visualise several graph algorithms.
In particular, the algorithms implemented are pathfinding algorithms, i.e. given a start and end node in the graph, we want to find the shortest path from the start to the end node.
This is sometimes known as the single-pair shortest path problem.

For this project, we considered a path on the grid from the start node to the end node to be a valid shortest path if it satisfied the following:
- Each square on the path is vertically or horizontally contiguous (i.e. diagonal movements are not allowed).
- No other path between the start and end nodes is strictly longer than the path.

## How to run
Prerequisites: pygame.

To start the application, simply run `main.py`.
- You may select any of the three algorithms to visualise by clicking on the buttons.
- Left click on the grid to add the start position (orange), end position (turquoise), and barriers (black). Right click to remove any of these.
- Once you are satisfied with the setup, press `SPACE` to start the algorithm visualisation.
  - Green squares represent nodes which are to be visited 'next', in the context of the algorithm. Red squares represent nodes which have already been visited. The final path found by the algorithm is reconstructed in purple.
- To reset the path and choose a different algorithm while keeping the start, end, and barriers, press `R`.
- To clear everything on the grid and select an algorithm again, press `C`.

## Algorithms Implemented
1. **Dijkstra Algorithm**: a single-source shortest-path algorithm which, in its most general form, works on digraphs with unbounded non-negative weights.
   It is the fastest known algorithm for such arbitrary graphs, but for special cases (e.g. integer weights, undirected graphs, or additional information is available as we allow here in the form of the heuristic function), other algorithms can have better time complexity.
   It maintains a set of vertices whose shortest distance from the source is known, and iteratively selects the vertex with the smallest known distance, updating the distances of its neighbors.
   The next vertex to be visited is determined by a priority queue, which sorts the neighbors of visited vertices by their currently recorded distance.
   - Time Complexity: $O((|V| + |E|) \log(|V|))$. The $\log(|V|)$ factor comes from the use of a priority queue to efficiently select the node with the smallest distance.
   - Space Complexity: $O(|V|)$ from the priority queue in the worst case (all vertices in the queue).

2. **A\* Algorithm**: a single-pair shortest-path algorithm which builds on Dijkstra's algorithm, but also incorporates a heuristic function $h(n)$ which helps to narrow down the search space, or at least to prioritise those paths which are most likely to lead to shorter paths. 
   We chose the Manhattan distance as the heuristic function, due to our definition of a valid shortest path (diagonal movements not allowed).
   - Time Complexity: $O(|E|\log(|V|))$. Like Dijkstra's, the $\log(|V|)$ factor is due to the use of a priority queue. However, A* performs better because of its heuristic.
   - Space Complexity: also $O(|V|)$ due to the priority queue.

3. **Breadth-First Search**: BFS is a special case of Dijkstra's algorithm, in which the priority queue is replaced by a simple queue.
   This can be done because the grid can be thought of as an unweighted graph: any two paths which go through the same number of squares are considered essentially the same.
   That is, the cost for moving from one node to any of its neighbors incurs the same cost.
   - Time Complexity: $O(|V| + |E|)$. In the case of a grid where each cell has a constant number of neighbors, the time complexity simplifies to $O(|V|)$.
   - Space Complexity: also $O(|V|)$ due to the queue.

Note: all three of these algorithms are guaranteed to always find the shortest path, and all have the same space complexity. However, there are clear differences in time complexity, and this becomes apparent in the visualisations.

## Challenges
Some challenges we faced include some bugs in clearing the screen, where the purple path was still there.... 

In your README.md, include:

Descriptions of algorithms implemented.
Encountered issues or challenges.
Instructions on code execution.

[If applicable] Methodology and findings from the bonus challenge of beating Python’s built-in algorithms.

Any extra information you would like to share with me.
List the names of all group members, or your own name if you are a solo participant.