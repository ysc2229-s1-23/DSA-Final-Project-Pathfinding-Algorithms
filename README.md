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

4. **Fringe Search**: an algorithm which aims to strike a balance between the space/time trade-off of A\* and Iterative Deepening A\* (IDA\*) for pathfinding on grid-based maps. The key motivation is to eliminate problems with repeated states/cycles and reduce the overhead of iterative deepening in IDA\*.
   The algorithm maintains two lists, "now" and "later," representing the current iteration and the next iteration respectively; this is implemented as a single concatenated list in our code, following the pseudocode provided by the authors of the [paper](https://web.archive.org/web/20090219220415/http://www.cs.ualberta.ca/~games/pathfind/publications/cig2005.pdf) introducing the algorithm.
   It iterates over the fringe (frontier) of the search tree, expanding nodes based on their costs.

   Compared to A\*, Fringe Search does not require the now list to be kept in sorted order, which may reduce time cost.
   However, Fringe Search may visit nodes that are irrelevant for the current iteration and A\*’s ordering means that it is more likely to find a goal state sooner than the Fringe Search.
   The relative costs of these differences determines which of A\* and Fringe Search performs better in specific problems.

Note: the first three of these algorithms are guaranteed to always find the shortest path, and all have the same space complexity. However, there are clear differences in time complexity, and this becomes apparent in the visualisations.

We faced some challenges implementing Fringe Search (and attempting to implement IDA\*), which we will address in the next section.

## Challenges

### Visualisation
Some challenges we faced include some bugs in clearing the screen, where the purple path was still there.... 
We also had an issue with a flickering screen when trying to present the pathfinding statistics, which we realized was due to repeatedly updating the grid in the for loops. We solved this issue via ..

### Implementing algorithms
While our implementation of Dijkstra's, A\* and BFS passed all our tests and managed to find the shortest path every time, we faced challenges implementing both IDA\* and Fringe Search.
We ended up discarding IDA\* as we did not have time to fix the implementation.

Although the Fringe Search algorithm was generally faster than Dijkstra's or BFS, it often did not find the shortest path (off by 1-10 nodes), and was about as fast as A\* in many cases.

It is very possible that we misunderstood something in the pseudocode and/or the paper while implementing the algorithm. While Fringe Search is still included in the visualizer, finding the shortest path with it is not guaranteed in all cases. 

### Others
When experimenting with different features and trying to generate functions, we faced an issue of computer crashing, presumably because of computational overload and some personal computer issue. This greatly slowed down our progress in experimenting with code. 

We spent a lot of time debugging code, especially when trying to do the UI and testing, because we had to think about how to separate the pygame elements from the actual algorithm. Definitely a challenging but worthwhile experience!


In your README.md, include:

Descriptions of algorithms implemented.
Encountered issues or challenges.
Instructions on code execution.

[If applicable] Methodology and findings from the bonus challenge of beating Python’s built-in algorithms.

Any extra information you would like to share with me.