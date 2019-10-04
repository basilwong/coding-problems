#include <bits/stdc++.h>

using namespace std;

class Node {
    public:
        int data;
        Node *left;
        Node *right;
        Node(int d) {
            data = d;
            left = NULL;
            right = NULL;
        }
};

class Solution {
    public:
  		Node* insert(Node* root, int data) {
            if(root == NULL) {
                return new Node(data);
            } else {
                Node* cur;
                if(data <= root->data) {
                    cur = insert(root->left, data);
                    root->left = cur;
                } else {
                    cur = insert(root->right, data);
                    root->right = cur;
               }

               return root;
           }
        }

// -----------------------------------------------------------------------------

/*The tree node has data, left child and right child
class Node {
    int data;
    Node* left;
    Node* right;
};

*/
    int height(Node* root) {
      int ret = 0;
      int right = 0;
      int left = 0;
      if (root->left != NULL) {
        ret++;
      } else if (root->right != NULL) {
        ret++;
      }

      if (root->left != NULL) {
        left = height(root->left);
      }
      if (root->right != NULL) {
        right = height(root->right);
      }

      if (right >= left) {
        ret += right;
      } else {
        ret += left;
      }

      return ret;
     }

// -----------------------------------------------------------------------------

}; //End of Solution

int main() {

    Solution myTree;
    Node* root = NULL;

    int t;
    int data;

    std::cin >> t;

    while(t-- > 0) {
        std::cin >> data;
        root = myTree.insert(root, data);
    }

    int height = myTree.height(root);

  	std::cout << height;

    return 0;
}
