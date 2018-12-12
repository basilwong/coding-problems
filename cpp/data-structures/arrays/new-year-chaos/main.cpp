#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

void minimumBribes(vector<int> q) {

  int initial_position;
  int dif;
  int swaps = 0;

  std::cout << "\n";

  // std::vector<int> tracker(q.size(), 0);

  for (int x = 0; x < q.size(); x++) {
    initial_position = x + 1;
    if (initial_position != q[x]) {
      // std::cout << initial_position << " and " << q[x] << " out of place.\n";
      dif = q[x] - initial_position;
      if (dif > 0) {
        if (dif > 2) {
          std::cout << "Too chaotic\n";
          return;
        } else {
          // std::cout << "Adding " << q[x] << " to tracker.\n";
          // tracker[q[x] - 1] = 1;
        }
      } else {
        for (int y = x; y >= 0; y--) {
          if (q[y] > q[x]) {
            swaps++;
          }
        }
        // std::cout << "swaps = " << swaps << " after " << q[x] << "\n";
      }
    }
  }
  std::cout << swaps << "\n";
}

void test_1() {
  std::cout << "Output should be Too Chaotic:\n";
  const int arr1[] = {5, 1, 2, 3, 7, 8, 6, 4};
  std::vector<int> vec1 (arr1, arr1 + sizeof(arr1) / sizeof(arr1[0]) );
  minimumBribes(vec1);

  std::cout << "\nOutput should be 7:\n";
  int arr2[] = {1, 2, 5, 3, 7, 8, 6, 4};
  std::vector<int> vec2 (arr2, arr2 + sizeof(arr2) / sizeof(arr2[0]) );
  minimumBribes(vec2);
}

int main()
{
  test_1();
    // int t;
    // cin >> t;
    // cin.ignore(numeric_limits<streamsize>::max(), '\n');
    //
    // for (int t_itr = 0; t_itr < t; t_itr++) {
    //     int n;
    //     cin >> n;
    //     cin.ignore(numeric_limits<streamsize>::max(), '\n');
    //
    //     string q_temp_temp;
    //     getline(cin, q_temp_temp);
    //
    //     vector<string> q_temp = split_string(q_temp_temp);
    //
    //     vector<int> q(n);
    //
    //     for (int i = 0; i < n; i++) {
    //         int q_item = stoi(q_temp[i]);
    //
    //         q[i] = q_item;
    //     }
    //
    //     minimumBribes(q);
    // }

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
