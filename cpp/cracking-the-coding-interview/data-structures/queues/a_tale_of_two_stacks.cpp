#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
using namespace std;

// Implements a queue with two stacks.


/*
 * enQueue operation costly
 */

//class MyQueue {
//
//public:
//    stack<int> stack_newest_on_top, stack_oldest_on_top;
//    void push(int x) {
//      // Before taking on new element, push everything to oldest on top.
//      while (! stack_oldest_on_top.empty()) {
//        stack_newest_on_top.push(stack_oldest_on_top.top());
//        stack_oldest_on_top.pop();
//      }
//
//      // Add x to oldest on top before putting the other elements on top of it.
//      stack_oldest_on_top.push(x);
//
//      while (! stack_newest_on_top.empty()) {
//        stack_oldest_on_top.push(stack_newest_on_top.top());
//        stack_newest_on_top.pop();
//      }
//    }
//
//    void pop() {
//      if (! stack_oldest_on_top.empty()) {
//        stack_oldest_on_top.pop();
//      }
//    }
//
//    int front() {
//      return stack_oldest_on_top.top();
//    }
//};


/*
 * deQueue operation costly, also only does transfer operation when needed
 */

class MyQueue {

public:
    stack<int> stack_newest_on_top, stack_oldest_on_top;
    void push(int x) {
      stack_newest_on_top.push(x);
    }

    void pop() {
      prep_old();
      stack_oldest_on_top.pop();
    }

    int front() {
      prep_old();
      return stack_oldest_on_top.top();
    }

    void prep_old(){
      if (stack_oldest_on_top.empty()) {
        while (!stack_newest_on_top.empty()) {
          stack_oldest_on_top.push(stack_newest_on_top.top());
          stack_newest_on_top.pop();
        }
      }
    }
};

int main() {
  MyQueue q1;
  int q, type, x;
  cin >> q;

  for(int i = 0; i < q; i++) {
    cin >> type;
    if(type == 1) {
      cin >> x;
      q1.push(x);
    }
    else if(type == 2) {
      q1.pop();
    }
    else cout << q1.front() << endl;
  }
  /* Enter your code here. Read input from STDIN. Print output to STDOUT */
  return 0;
}