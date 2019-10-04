#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

int minimumBribes(vector<int> q) {

  int initial_position;
  int dif;
  int swaps = 0;
  bool in_order = true;
  // std::cout << "\n";

  // std::vector<int> tracker(q.size(), 0);

  for (int x = 0; x < q.size() - 1; x++) {
    initial_position = x + 1;

    if (initial_position != q[x]) {
      in_order = false;
      dif = q[x] - initial_position;
      // If the value is greater than initlal, possible switch.
      if (dif > 0) {
        if (dif > 2) {
          return -1;
        } else {
          if (q[x] > q[x+1]) {
            std::swap(q[x], q[x+1]);
            swaps++;
          }
        }
      } else { // Values pre algorithm swap should not be less than initial.
        return -1;
      }
    }
  }

  for (int y = q.size() - 1; y > 0; y--) {
    initial_position = y + 1;

    if (initial_position != q[y]) {
      in_order = false;
      dif = q[y] - initial_position;

      // If a value that is smaller than it should is behind a bigger value, swap.
      if (dif < 0) {
        if (q[y] < q[y-1]) {
          std::swap(q[y], q[y-1]);
          swaps++;
        }
      }
    }
  }

  if (!in_order) {
    swaps += minimumBribes(q);
    return swaps;
  } else {
    return swaps;
  }
  // std::cout << swaps << "\n";
  // return;
}

void test_1() {
  std::cout << "Output should be Too Chaotic:\n";
  const int arr1[] = {5, 1, 2, 3, 7, 8, 6, 4};
  std::vector<int> vec1 (arr1, arr1 + sizeof(arr1) / sizeof(arr1[0]) );
  std::cout << minimumBribes(vec1) << "\n";

  std::cout << "\nOutput should be 7:\n";
  int arr2[] = {1, 2, 5, 3, 7, 8, 6, 4};
  std::vector<int> vec2 (arr2, arr2 + sizeof(arr2) / sizeof(arr2[0]) );
  std::cout << minimumBribes(vec2) << "\n";
}

int main()
{
  // test_1();
    int swaps;
    int t;
    cin >> t;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int t_itr = 0; t_itr < t; t_itr++) {
        int n;
        cin >> n;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        string q_temp_temp;
        getline(cin, q_temp_temp);

        vector<string> q_temp = split_string(q_temp_temp);

        vector<int> q(n);

        for (int i = 0; i < n; i++) {
            int q_item = stoi(q_temp[i]);

            q[i] = q_item;
        }

        swaps = minimumBribes(q);
        if (swaps == -1) {
          std::cout << "Too chaotic\n";
        } else {
          std::cout << swaps << "\n";
        }
    }

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}
