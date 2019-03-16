// Gary is an avid hiker. He tracks his hikes meticulously, paying close
// attention to small details like topography.
// A mountain is a sequence of consecutive steps above sea level, starting with
// a step up from sea level and ending with a step down to sea level.
// A valley is a sequence of consecutive steps below sea level, starting with a
// step down from sea level and ending with a step up to sea level.

#include <bits/stdc++.h>

using namespace std;

// Given Gary's logs, finds/returns the number of valleys.
// Example input:
/*
8
UDDDUDUU
*/
int countingValleys(int n, string s) {
  int valleys = 0;
  int level = 0; // sea level
  bool below_sea_level = false;

  for (auto& ch : s) {

    // Determines level from the strings.
    if (ch == 'U') {
      level++;
    } else {
      level--;
    }

    // If comes up from below sea level count a valley.
    if (below_sea_level) {
      if (level == 0) {
        below_sea_level = false;
        valleys++;
      }
    } else {
      if (level < 0) {
        below_sea_level = true;
      }
    }
  }
  return valleys;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string s;
    getline(cin, s);

    int result = countingValleys(n, s);

    cout << result << "\n";

    return 0;
}
