/*
 * The below code checks whether the input tree is a binary search tree.
 */

struct Node {
    int data;
    Node* left;
    Node* right;
}

// Checks if the left child is lower than the parent. Additionally, it calls
// check_right and itself recursively to check the child's children.
bool check_left(Node *root) {
  bool compare;
  bool left;
  bool right;
  Node* left_child;
  Node* child_of_child;

  // If the node has no left child, return true. This part of the binary tree is
  // within bst parameters.
  if (root->left == NULL) {
    return true;
  }

  // Instantiate node of the left child.
  left_child = root->left;

  // Compare the date of the left child with the data of the parent.
  if (root->data > left_child->data) {

  }

}

// Checks if the right child is lower than the parent. Additionally, it calls
// check_left and itself recursively to check the child's children.
bool check_right(Node *root) {

}

bool checkBST(Node *root) {
  if ((check_left(root)) && (check_right(root))) {
    return true;
  } else {
    return false;
  }
}




//
//int main() {
//  std::cout << "Hello, World!" << std::endl;
//  return 0;
//}