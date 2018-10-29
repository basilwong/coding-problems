#include <cmath>
#include <cstdio>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>
#include <set>
#include <queue>
using namespace std;

class Graph {

private:
  int size;

public:
  // Defining the nodes which make up the graph.
  struct Node {
  public:
    int id;
    std::vector< Node* > adjacent;

    Node(int id) {
      this->id = id;
    }
  };

  // Defining a map for access to nodes with just their id.
  std::map< int, Node* > node_lookup;

  // initializer for the Graph class. Makes a graph containing n number of nodes
  // with id's numbered from 0 to n.
  Graph(int n) {
    this->size = n;
    for (int i = 0; i < n; i++) {
      Node *new_node = new Node(i);
      node_lookup.insert(std::make_pair( i, new_node ));
    }
  }

  // Adds a edge from Node(id = u) to Node(id = v). It is up to the
  // user to make sure the nodes exists.
  void add_edge(int u, int v) {
    Node *first = node_lookup[u];
    Node *second = node_lookup[v];

    first->adjacent.push_back(second);
    second->adjacent.push_back(first);
  }

  // Returns the shortest path to every other node in the graph, given the id of
  // the start node. The lenght of an edge is 6 and if no path exists the path
  // length to that node is -1.
  std::vector< int > shortest_reach(int start) {

    std::vector< int > sr;

    for (int i = 0; i < start; i++) {
      sr.push_back(bfs_get_length(start, i));
    }
    sr.push_back(-1);
    for (int j = start + 1; j < size; j++) {
      sr.push_back(bfs_get_length(start, j));
    }

    return sr;
  }

  // Gets the length of the shortest path from the start node to the destination node.
  // This function uses breadth first search algorithm to get shortest path.
  // If no path exists this function returns -1.
  int bfs_get_length(int start, int destination) {

    int check_node;
    int path_length = 0;
    std::queue< int > to_visit;
    std::set< int > visited;
    std::set< int > next_to_visit;

    to_visit.push(start);

    while(!to_visit.empty()) {

      // Get the next node to check from the to_visit vector of Node pointers.
      check_node = to_visit.front();
      to_visit.pop();

      // std::cout << "\n\nChecking: " << check_node;
      // std::cout << "\nVisited: ";
      // for (auto& nodee : visited) {
      //   std::cout << nodee << " ";
      // }

      // Return the current path length if we get the required end.
      if (check_node == destination) {
        // std::cout << "\nFound path at " << check_node << " of length " << path_length << "\n\n";
        return path_length;
      }

      // Skips nodes that have already been visited.
      if (visited.find(check_node) != visited.end()){
        // std::cout << "\nAlready visited.";
        continue;
      }

      visited.insert(check_node);

      // If the node that is checked is not the end, we add all adjacent nodes
      // to the next round of nodes.
      for (auto& adj_node : node_lookup[check_node]->adjacent) {
          // std::cout << "\nAdding to next to visit:" << adj_node->id;
          next_to_visit.insert(adj_node->id);

      }

      // If all the current adjacted nodes are not the end, we add the next
      // level of nodes to the to_visit vector (from the next_to_visit vector).
      if (to_visit.empty()) {
        for (auto& next_node : next_to_visit) {
          to_visit.push(next_node);
        }
        next_to_visit.clear();
        // std::cout << "\nNext round, ading 6 to path.";
        path_length += 6; // Going to next level so add 6 to path length.
      }
    }

    // std::cout << "\nCould not find path.\n\n";
    return -1; // If no path found.

  }


};

int main() {
    int queries;
    cin >> queries;

    for (int t = 0; t < queries; t++) {

		int n, m;
        cin >> n;
        // Create a graph of size n where each edge weight is 6:
        Graph graph(n);
        cin >> m;
        // read and set edges
        for (int i = 0; i < m; i++) {
            int u, v;
            cin >> u >> v;
            u--, v--;
            // add each edge to the graph
            graph.add_edge(u, v);
        }
		int startId;
        cin >> startId;
        startId--;
        // Find shortest reach from node s
        vector<int> distances = graph.shortest_reach(startId);

        for (int i = 0; i < distances.size(); i++) {
            if (i != startId) {
                cout << distances[i] << " ";
            }
        }
        cout << endl;
    }

    return 0;
}

// This main was used for white box testing each of the components of the
// graph class.
int main() {
 Graph new_graph = Graph(5);

  std::cout << "\n\nTesting the proper creation of a graph upon construction.:\n\n";
  // Testing the proper creation of a graph upon construction.
  for(auto it = new_graph.node_lookup.cbegin(); it != new_graph.node_lookup.cend(); ++it) {
      std::cout << it->first << " " << it->second->id << "\n";
  }

  std::cout << "\n\nTesting add_edge:\n\n";

  // Testing the add edge method.
  new_graph.add_edge(0, 2); // In the actual main code, the id values of the edges are decreased by one to make them start at 0.

  std::cout << new_graph.node_lookup[0]->adjacent[0]->id << "\n"; // Tests whether an edge was added properly between node 0 and 2.

  // Testing the breadth first search function.
  std::cout << "\n\nTesting bfs algorithm:\n\n";
  std::cout << "\nFound path length from 0 to 2 is: " << new_graph.bfs_get_length(0, 2) << " should be 6.\n";
  std::cout << "\nFound path length from 0 to 1 is: " << new_graph.bfs_get_length(0, 1) << " should be -1.\n";

  // Testing shortest reach function.
  std::cout << "\n\nTesting shortest_reach algorithm:\n\n";
  std::vector< int > shortest = new_graph.shortest_reach(0);
  for (auto& length : shortest) {
    std::cout << "\nLength: " << length;
  }

  // Testing fo correct results: straight graph.
  Graph straight_graph = Graph(5);
  straight_graph.add_edge(0, 1);
  straight_graph.add_edge(1, 2);
  straight_graph.add_edge(2, 3);
  straight_graph.add_edge(3, 4);

  std::vector< int > shortest_straight = straight_graph.shortest_reach(0);
  std::cout << "\n\nResults from straight graph, start at 0.";
  for (auto& length_s : shortest_straight) {
    std::cout << "\nLength: " << length_s;
  }
  std::cout << "\nExpected Result: 6, 12, 18, 24";

  std::vector< int > straight_middle = straight_graph.shortest_reach(2);
  std::cout << "\n\nResults from straight graph, start at 3.";
  for (auto& length_m : straight_middle) {
    std::cout << "\nLength: " << length_m;
  }
  std::cout << "\nExpected Result: 12, 6, 6, 12";

  // Testing circle graph.
  Graph circle_graph = Graph(5);
  circle_graph.add_edge(0, 1);
  circle_graph.add_edge(1, 2);
  circle_graph.add_edge(2, 3);
  circle_graph.add_edge(3, 4);
  circle_graph.add_edge(4, 0);


  std::vector< int > shortest_circle = circle_graph.shortest_reach(0);
  std::cout << "\n\nResults from circle graph, start at 0.";
  for (auto& length_s : shortest_circle) {
    std::cout << "\nLength: " << length_s;
  }
  std::cout << "\nExpected Result: 6, 12, 12, 6";

  std::vector< int > circle_middle = circle_graph.shortest_reach(2);
  std::cout << "\n\nResults from circle graph, start at 3.";
  for (auto& length_m : circle_middle) {
    std::cout << "\nLength: " << length_m;
  }
  std::cout << "\nExpected Result: 12, 6, 6, 12";
}
