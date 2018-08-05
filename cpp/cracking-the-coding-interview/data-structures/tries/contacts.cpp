#include <bits/stdc++.h>

using namespace std;

struct Node {
  struct Node *children[26]; // 26 letters in alphabet
  bool end_of_word;
};

vector<string> split_string(string);
void parse_operation(Node *root, string op_in, string contact_in);
Node* new_node();


int main()
{
  int n;
  cin >> n;
  cin.ignore(numeric_limits<streamsize>::max(), '\n');

  Node *root = new_node();

  for (int n_itr = 0; n_itr < n; n_itr++) {
    string opContact_temp;
    getline(cin, opContact_temp);

    vector<string> opContact = split_string(opContact_temp);

    string op = opContact[0];

    string contact = opContact[1];

    parse_operation(root, op, contact);

  }

  return 0;
}

vector<string> split_string(string input_string) {
  string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
      return x == y and x == ' ';
  });

  input_string.erase(new_end, input_string.end());

  while (input_string[input_string.length() - 1] == ' ') {
    input_string.pop_back();
  }

  vector<string> splits;
  char delimiter = ' ';

  size_t i = 0;
  size_t pos = input_string.find(delimiter);

  while (pos != string::npos) {
    splits.push_back(input_string.substr(i, pos - i));

    i = pos + 1;
    pos = input_string.find(delimiter, i);
  }

  splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

  return splits;
}

// Parses the inputted operations and executes the queries.
void parse_operation(Node *root, string op_in, string contact_in) {

  if (op_in == "add") {

  } else if (op_in == "find") {

  }
}

void add_contact(Node *root, string contact) {

}

// Creates a new Node struct pointer and instantiates all the alphabet pointers
// in the struct to NULL.
Node* new_node() {
  Node *new_trie_node;

  new_trie_node = new Node;

  new_trie_node->end_of_word = false;

  for (int i = 0; i < 26; i++) {
    new_trie_node->children[i] = NULL;
  }

  return new_trie_node;
}