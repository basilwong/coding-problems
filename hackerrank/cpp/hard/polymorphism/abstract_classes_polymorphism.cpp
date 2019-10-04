/*
A cache is a component that stores data so future requests for that data can be
served faster. The data stored in a cache might be the results of an earlier
computation, or the duplicates of data stored elsewhere. A cache hit occurs when
the requested data can be found in a cache, while a cache miss occurs when it
cannot. Cache hits are served by reading data from the cache which is faster
than recomputing a result or reading from a slower data store. Thus, the more
requests that can be served from the cache, the faster the system performs.

One of the popular cache replacement policies is: "least recently used" (LRU).
It discards the least recently used items first.

Given an abstract base class Cache with member variables and functions:

mp - Map the key to the node in the linked list
cp - Capacity
tail - Double linked list tail pointer
head - Double linked list head pointer
set() - Set/insert the value of the key, if present, otherwise add the key as
  the most recently used key. If the cache has reached its capacity, it should
  replace the least recently used key with a new key.
get() - Get the value (will always be positive) of the key if the key exists in
  the cache, otherwise return -1.
*/

#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <set>
#include <cassert>
using namespace std;

struct Node{
  Node* next;
  Node* prev;
  int value;
  int key;
  Node(Node* p, Node* n, int k, int val):prev(p),next(n),key(k),value(val){};
  Node(int k, int val):prev(NULL),next(NULL),key(k),value(val){};
};

class Cache{
  protected:
  map<int,Node*> mp; //map the key to the node in the linked list
  int cp;  //capacity
  Node* tail; // double linked list tail pointer
  Node* head; // double linked list head pointer
  virtual void set(int, int) = 0; //set function
  virtual int get(int) = 0; //get function
};

// Extends the class Cache and uses the member functions and variables to
// implement an LRU cache.
class LRUCache: public Cache {

public:

    LRUCache(int capacity) {
      cp = capacity;
    }

    void set(int key, int value) {

      Node *N;

      // Check length of the linked list.
      if (mp.empty()) {
        N = new Node(key, value);
        head = N;
        tail = N;
        mp.insert(std::pair< int, Node* >(key, N));
        return;
      }


      auto it = mp.find(key);

      if (it == mp.end()) {
        N = new Node(NULL, head, key, value);
        head->prev = N;
        head = N;
        mp.insert(std::pair< int, Node* >(key, N));

        if (mp.size() > cp) {
          tail = tail->prev;
          mp.erase(tail->next->key);
          delete tail->next;
          tail->next = NULL;
        }
      } else {
        it->second->value = value;

        if (head == it->second) {
          return;
        }

        it->second->prev->next = it->second->next;

        if(tail == it->second) {
          tail = tail->prev;
        } else {
          it->second->next->prev = it->second->prev;
        }
        it->second->next = head;
        it->second->prev = NULL;
        head->prev = it->second;
        head = it->second;
      }

    }

    int get(int key) {
      auto it = mp.find(key);
      if(it != mp.end())
        return it->second->value;

      return -1;
    }
};

int main() {
  int n, capacity,i;
  cin >> n >> capacity;
  LRUCache l(capacity);
  for (i=0;i<n;i++) {
    string command;
    cin >> command;
    if (command == "get") {
      int key;
      cin >> key;
      cout << l.get(key) << endl;
    } else if (command == "set") {
      int key, value;
      cin >> key >> value;
      l.set(key,value);
    }
  }
  return 0;
}
