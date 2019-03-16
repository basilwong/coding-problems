#include <bits/stdc++.h>

using namespace std;

// Given the coordinates of the top right index of the hourglass, returns the
// sum of the values of the hourglass.
//
// Hourglass values must exist. So the starting index correlated with values
// which are within the range.
int get_hour_glass(vector<vector<int>> arr, int x, int y) {
  return arr[y][x] + arr[y][x+1] + arr[y][x+2] + arr[y+1][x+1] + arr[y+2][x] + arr[y+2][x+1] + arr[y+2][x+2];
}

// Returns the largest sum of values of an hourglass. Array must be a rectangle.
int hourglassSum(vector<vector<int>> arr) {
  int max = -100000;
  int sum;
  for (int x = 0; x < 5; x++) {
    for (int y = 0; y < 5; y++) {
      sum = get_hour_glass(arr, y, x);
      if (sum > max) {
        max = sum;
      }
    }
  }

  return max;

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    vector<vector<int>> arr(6);
    for (int i = 0; i < 6; i++) {
        arr[i].resize(6);

        for (int j = 0; j < 6; j++) {
            cin >> arr[i][j];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    int result = hourglassSum(arr);

    fout << result << "\n";

    fout.close();

    return 0;
}
