#include "sets.h"

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>

/*
  1 Add an element  to the set.
  2 Delete an element  from the set. (If the number  is not present in the set, then do nothing).
  3 If the number  is present in the set, then print "Yes"(without quotes) else print "No"(without quotes).

Input Format:

The first line of the input contains  where  is the number of queries. The next  lines contain  query each. Each query
consists of two integers  and  where  is the type of the query and  is an integer.
 */

void sets(){
  // Getting Q.
  int Q;
  std::cin >> Q;

  // Responding the the queries.
  int x, y;
  std::set< int > s;
  std::set<int>::iterator itr;
  for (int i = 0; i < Q; i++) {
    std::cin >> y >> x;
    if (y == 1) {
      s.insert(x);
    } else if (y == 2) {
      s.erase(x);
    } else {
      itr = s.find(x);
      if (itr == s.end()) {
        std::cout << "No" << std::endl;
      } else {
        std::cout << "Yes" << std::endl;
      }
    }
  }
}