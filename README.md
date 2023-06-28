# Theorie des Graph - Graph Visualization and Shortest Path Calculation


This project is a Python-based implementation of graph visualization and shortest path calculation, inspired by the concepts of graph theory. The application allows users to create their own directed and undirected graphs, add nodes and edges, and drag and drop them anywhere on the canvas. The edges can have positive or negative weights.

The main features of this project include:

- Graph Creation: Users can create their own graphs by adding nodes and connecting them with edges. The graphs can be oriented or non-oriented, depending on user preference.
- Drag and Drop: Nodes and edges can be easily dragged and dropped to different positions on the canvas, allowing for flexible graph layout arrangements.
- Weighted Edges: The edges can have positive or negative weights, representing the relationship between connected nodes.
- Shortest Path Calculation: The application calculates the shortest path from a given node to all other nodes in the graph or to a specific node, depending on user input.
- Path Highlighting: The shortest path is visually highlighted with a different color, making it easy for users to identify the path.
- Algorithms Used: Dijkstra's algorithm is used for graphs that contain only positive-weighted edges, while the Bellman-Ford algorithm is used for graphs that contain both positive and negative-weighted edges.
- Absorbent Circuit Detection: In case of an absorbent circuit (a cycle with a negative total weight), it is identified and highlighted with a different color.

## Motivation

This project was developed from scratch with the goal of learning and understanding graph theory concepts, as well as improving programming skills in Python. It encompasses various aspects, including graphics, such as buttons, nodes, and edges, and the implementation of graph algorithms.

## Fun Fact

During the development of this project, a fun fact emerged: It provided an opportunity to finally apply trigonometric functions such as cosine (cos), tangent (tan), and sine (sin) by attempting to update the arrow positions relevant to both the node position and the edge position. This practical usage of trigonometry added an interesting dimension to the project and showcased the diverse applications of mathematical concepts in real-world scenarios.

##Screenshots

**We notice that in this algorithm the number of nodes doesn't matter, it calculates the shortes path by edge weight**

![thg1](https://github.com/nouha-belka/THG-project/assets/84313345/f7128795-8410-404b-80ff-8ebdfa38a060)

![thg](https://github.com/nouha-belka/THG-project/assets/84313345/148fc012-9e8d-4702-a818-8f67287f08e8)

**An example of directed edge**

![thg2](https://github.com/nouha-belka/THG-project/assets/84313345/f54ec32a-8401-4861-9231-4d0f15fbaab0)

**The project refuses to calculate with Dijkstra since there are some negative edges, it uses bellman instead**
![thg4](https://github.com/nouha-belka/THG-project/assets/84313345/ffe22535-71f7-4737-a6db-801ff74ae4fe)

**Absorbent Circuit Detection**
![Screenshot (559)](https://github.com/nouha-belka/THG-project/assets/84313345/d909b210-c90d-4236-8e99-fe44cf2e7cfc)

---

Thank you for exploring this project! If you have any questions or feedback, please feel free to reach out. Enjoy working with graphs and discovering the fascinating world of graph theory!
