#include <iostream>
#include <vector>
#include <algorithm>

/*
Detects a cycle in a linked list. 
Note that the head pointer is 'NULL' if the list is empty.

A Node is defined as: 
    struct Node {
        int data;
        struct Node* next;
    }
*/

bool has_cycle(Node* head) {
  // Initializes the head node.
  Node* current_node = head;
  if (current_node == NULL) {
    return false;
  }
  // List of past data. 
  std::vector< Node* > data_list;
  
  while(true) {
  
    std::vector< Node* >::iterator it = find (data_list.begin(), data_list.end(), current_node);
    if (it != data_list.end()) {
      // Data is in the vector, thus linked list has cycle.
      return true;
    } else {
      // Data is not in the vector, add data to vector and go to the next node.
      data_list.push_back(current_node);
      current_node = current_node->next;
      if (current_node == NULL) {
        // At the end of the linked list.
        return false;
      }
    }
  }
}