#include <cmath>
#include <cstdio>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>
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

  Graph(int n) {
    this->size = n;
    for (int i = 0; i < n; i++) {
      Node *new_node = new Node(i);
      node_lookup.insert(std::make_pair( i, new_node ));
    }
  }

  void add_edge(int u, int v) {
    Node* first = node_lookup[u];
    Node* second = node_lookup[v];

    first->adjacent.push_back(second);
  }

  vector<int> shortest_reach(int start) {

    for (int i = 0; i < start; i++) {

    }

    for (int j = start + 1; j < size; j++) {
      
    }
  }


};

/*
2
4 2
1 2
1 3
1
3 1
2 3
2
*/

// int main() {
//     int queries;
//     cin >> queries;
//
//     for (int t = 0; t < queries; t++) {
//
// 		int n, m;
//         cin >> n;
//         // Create a graph of size n where each edge weight is 6:
//         Graph graph(n);
//         cin >> m;
//         // read and set edges
//         for (int i = 0; i < m; i++) {
//             int u, v;
//             cin >> u >> v;
//             u--, v--;
//             // add each edge to the graph
//             graph.add_edge(u, v);
//         }
// 		int startId;
//         cin >> startId;
//         startId--;
//         // Find shortest reach from node s
//         vector<int> distances = graph.shortest_reach(startId);
//
//         for (int i = 0; i < distances.size(); i++) {
//             if (i != startId) {
//                 cout << distances[i] << " ";
//             }
//         }
//         cout << endl;
//     }
//
//     return 0;
// }

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


}
