#include <iostream>

// Checks if the left child is lower than the parent. Additionally, it calls
// check_right and itself recursively to check the child's children.
bool check_left(Node *root) {
  bool left;
  bool right;
  Node* left_child;
  
  std::cout << "\n\nNode: " << root->data << " check left.";

  // If the node has no left child, return true. This part of the binary tree is
  // within bst parameters.
  if (root->left == NULL) {
    std::cout << "\nReturn true: Null.";
    return true;
  }

  // Instantiate node of the left child.
  left_child = root->left;
  
  std::cout << "\nComparing: Parent: " << root->data << " Left Child: " << left_child->data;

  
  // Compare the date of the left child with the data of the parent.
  if (root->data < left_child->data) {
    // std::cout << "Incorrect: Parent: " << root->data << " Left Child: " << left_child->data;
    return false;
  }
  if (! check_left(left_child)) {
    return false;
  }
  if (! check_right(left_child)) {
    return false;
  }
  // std::cout << "root: " << root->data << " larger than " << "left: " << left_child->data << "return false\n\n";
  return true;
}

// Checks if the right child is lower than the parent. Additionally, it calls
// check_left and itself recursively to check the child's children.
bool check_right(Node *root) {
  bool left;
  bool right;
  Node* right_child;

  std::cout << "\nNode: " << root->data << " check right.";
  
  // If the node has no right child, return true. This part of the binary tree
  // is within bst parameters.
  if (root->left == NULL) {
    std::cout << "\nReturn true: Null.";
    return true;
  }

  // Instantiate node of the left child.
  right_child = root->right;

  std::cout << "\nComparing: Parent: " << root->data << " Right Child: " << right_child->data;

  
  // Compare the date of the left child with the data of the parent.
  if (root->data > right_child->data) {
    // std::cout << "Incorrect: Parent: " << root->data << " Right Child: " << right_child->data;
    return false;
  }

  if (! check_left(right_child)) {
    return false;
  }
  if (! check_right(right_child)) {
    return false;
  }

  // std::cout << "root: " << root->data << " less than " << "right: " << right_child->data << "return false\n\n";
  return true;
}

bool checkBST(Node *root) {
  // std::cout << "\n\n";
  if (! check_left(root)) {
    return false;
  }
  if (! check_right(root)) {
    return false;
  }
  return true;
}




//
//int main() {
//  std::cout << "Hello, World!" << std::endl;
//  return 0;
