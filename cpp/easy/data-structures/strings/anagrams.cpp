#include <bits/stdc++.h>
#include <set>

using namespace std;

// must return an integer representing the minimum total characters that must be
// deleted to make the strings anagrams.
int makeAnagram(string a, string b) {
  // Making a vector for safe programming since we don't want to be modifying the inputs.
  multiset<char> s;
  
  for (auto& cha : a) {
    s.insert(cha);
  }
  for (auto& inte : s) {
    cout << inte;
  }
  multiset<char>::iterator temp;
  unsigned int counter = 0;
  for (auto& ch : b) {
    temp = s.find(ch);
    if (temp != s.end()) {
      counter++;
      s.erase(temp);
    }
  }
  return s.size() + (b.size() - counter);

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string a;
    getline(cin, a);

    string b;
    getline(cin, b);

    int res = makeAnagram(a, b);

    fout << res << "\n";

    fout.close();

    return 0;
}
