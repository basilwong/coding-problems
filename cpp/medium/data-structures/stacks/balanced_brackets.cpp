#include <iostream>
#include <bits/stdc++.h>
#include <stack>

using namespace std;
/*
Sample Input:

3
{[()]}
{[(])}
{{[[(())]]}}
 */

// Takes a string and checks if all the opening brackets have a corresponding closing bracket. Prints TRUE if the
// brackets properly line up and FALSE if not.
void check_line(string line) {
  const string f = "NO\n";
  const string t = "YES\n";
  stack< char > brackets;
  char it;
  for (int i = 0; i < line.size(); i++) {
    it = line[i];
    if ((it == '[') || (it == '(') || (it == '{')) {
      brackets.push(it);
    } else {
      if (brackets.empty()) {
        cout << f;
        return;
      }
      if ((brackets.top() == '(') && (it == ')')) {
        brackets.pop();
      } else if ((brackets.top() == '{') && (it == '}')) {
        brackets.pop();
      } else if ((brackets.top() == '[') && (it == ']')) {
        brackets.pop();
      } else {
        cout << f;
        return;
      }
    }
  }
  if (brackets.empty()) {
    cout << t;
  } else {
    cout << f;
  }

}

int main()
{
  int t;
  cin >> t;
  cin.ignore(numeric_limits<streamsize>::max(), '\n');


  for (int t_itr = 0; t_itr < t; t_itr++) {
    string expression;
    getline(cin, expression);
    check_line(expression);
  }

  return 0;
}
