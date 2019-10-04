#include <bits/stdc++.h>

using namespace std;

std::map< int, int > track;



// Complete the stepPerms function below.
int stepPerms(int n) {
  
  if (track.find(n) != track.end()) {
    return track[n];
  }

  int x = (stepPerms(n - 1) % 10000000007) + (stepPerms(n - 2) % 10000000007) + (stepPerms(n - 3) % 10000000007);

  track.insert(std::make_pair(n, x));
  return x;

}

int main()
{
    track.insert(std::make_pair(0, 0));
    track.insert(std::make_pair(1, 1));
    track.insert(std::make_pair(2, 2));
    track.insert(std::make_pair(3, 4));
    ofstream fout(getenv("OUTPUT_PATH"));

    int s;
    cin >> s;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int s_itr = 0; s_itr < s; s_itr++) {
        int n;
        cin >> n;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        int res = stepPerms(n);

        fout << res << "\n";
    }

    fout.close();

    return 0;
}
