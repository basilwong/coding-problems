/*
Essentially checks if there is a common subset between two strings. 
*/
#include <bits/stdc++.h>

using namespace std;

string twoStrings(string s1, string s2) {

  std::set<char> checked;

  for (auto& ch : s1) {
    checked.insert(ch);
  }

  for (auto& ch : s2) {
    if (checked.find(ch) != checked.end()) {
      return "YES";
    }
  }

  return "NO";

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int q;
    cin >> q;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int q_itr = 0; q_itr < q; q_itr++) {
        string s1;
        getline(cin, s1);

        string s2;
        getline(cin, s2);

        string result = twoStrings(s1, s2);
        std::cout << result << "\n";
        fout << result << "\n";
    }

    fout.close();

    return 0;
}
