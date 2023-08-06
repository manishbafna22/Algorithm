**Breadth First Search**


**Introduction**
BFS is a graph traversal algorithm used to explore all vertices in a graph or search for a specific node in the graph.
The algorithm explores all nodes at the current level before moving to nodes at the next level. This means it explores nodes layer by layer.
BFS is often used to find the shortest path between two nodes in an unweighted graph, among other applications. 
Additionally, it provides a good way to explore all nodes in a graph and can be useful for other graph-related problems like connected components, finding cycles, and more.

**Steps involved**
Choose a starting node (often referred to as the "source" node) from which the traversal begins.
BFS uses a queue to keep track of the nodes that need to be visited. Nodes are enqueued and dequeued in a first-in-first-out (FIFO) manner.
Enqueue the starting node into the queue and mark it as visited to keep track of visited nodes.
Dequeue a node from the front of the queue. Explore all its unvisited neighbors (adjacent vertices) and enqueue them into the queue.
Mark the visited neighbors as visited to avoid revisiting them later.
Repeat the process of dequeuing nodes from the queue, visiting their unvisited neighbors, and marking them visited until the queue becomes empty.
The BFS algorithm terminates when all nodes in the graph have been visited, or when a specific condition (e.g., finding a target node) is met.
BFS guarantees that the first path it finds from the source node to any other reachable node is the shortest path. In an unweighted graph, this is the shortest number of edges between nodes.
BFS is particularly useful when you need to find the shortest path, find the minimum steps to reach a destination, or explore the graph in a layered manner.
The time complexity of BFS is O(V + E), where V is the number of vertices (nodes) and E is the number of edges in the graph.
The space complexity of BFS is O(V) because it needs to maintain a queue to store the nodes to be visited.
BFS is widely used in various applications, such as network routing, maze-solving, and finding connected components in a graph. Its simplicity and efficiency make it a popular choice for graph traversal tasks.

**Overview:**
The problem statement is to determine if a ball can reach the destination in a maze. The maze is represented as a 2D matrix of size MxN, where each cell is either a 0 (empty space) or a 1 (wall). The ball can move up, down, left, or right, but it can't go through walls. The ball starts at a given starting position, and the destination is another cell in the matrix. We need to find if the ball can reach the destination by navigating through the maze.

**Presentation Link:**
[Leet Code 490: The MAZE using Breadth First Search](https://docs.google.com/presentation/d/1eXXO3uMvlgs7S3fHf_E7orDWWi3e-laPGmtKvDMY0TM/edit?usp=sharing "Leet Code 490: The MAZE using Breadth First Search")
  
