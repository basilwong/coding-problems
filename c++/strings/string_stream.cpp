#include <sstream>
#include <vector>
#include <iostream>
using namespace std;


//23,4,56
// Takes a string such as the one above and parses it into a vector of int
// values.
vector<int> parseInts(string str) {

	vector<int> v;

	stringstream ss(str);

	int integer_t;
	char ch;

  while(ss >> integer_t) {
    v.push_back(integer_t);
    ss >> ch;
  }

  return v;
}



void string_stream() {

    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }

}
