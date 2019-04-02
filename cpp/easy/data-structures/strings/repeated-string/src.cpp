#include <bits/stdc++.h>

using namespace std;

// Complete the repeatedString function below.
long repeatedString(string s, long n) {
  int count = 0;
  for (auto i : s) {
    if (i == 'a') {
      count++;
    }
  }

  long full_repeats = n / s.length();
  long extra = n - (s.length() * full_repeats);
  long added = 0;
  for (int j = 0; j < extra; j++) {
    if (s[j] == 'a') {
      added++;
    }
  }

  return count*full_repeats + added;

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    long n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    long result = repeatedString(s, n);

    fout << result << "\n";

    fout.close();

    return 0;
}
