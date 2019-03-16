#include "maps.h"

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

//You are appointed as the assistant to a teacher in a school and she is correcting the answer sheets of the students.
// //Each student can have multiple answer sheets.So the teacher has  queries:
//
//1 Add the marks  to the student whose name is .
//
//2 Erase the marks of the students whose name is .
//
//3 Print the marks of the students whose name is . (If  didn't get any marks print .)
void maps() {

  // Retrieve Q.
  int Q;
  cin >> Q;

  int inpt;
  string name;
  int marks;
  map < string, int > m;
  // Responding to queries.
  for (int i = 0; i < Q; i++) {

    // Get the first part of the query.
    cin >> inpt;

    // Conditional branch for different queries.
    if (inpt == 1) {

      // Get name and makes for query type 1.
      cin >> name;
      cin >> marks;

      // Adds the marks if the name already exists, otherwise it inserts the values.
      if (m.find(name) == m.end()) {
        m.insert(make_pair(name, marks));
      } else {
        m[name] += marks;
      }
    } else if (inpt == 2) {
      cin >> name;
      m[name] = 0;
    } else {
      cin >> name;
      cout << m[name] << endl;
    }

  }
}

/*
7
1 Jesse 20
1 Jess 12
1 Jess 18
3 Jess
3 Jesse
2 Jess
3 Jess
*/