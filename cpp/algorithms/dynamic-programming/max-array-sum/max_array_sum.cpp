#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

int maxSubsetSum(vector<int> arr) {

  int sum = 0;
  int section_sum1 = 0;
  int section_sum2 = 0;
  // State 0: Post value zero or lower.
  // State 1: The first part of adjacent group.
  // State 2: The second part of adjacent group.
  int analysis_state; // 0, 1, 2

  if (arr[0] > 0) {
    section_sum1 += arr[0];
    analysis_state = 2;
  } else {
    analysis_state = 0;
  }

  for (int i = 0; i < arr.size(); i++) {
    if (arr[i] > 0) {
      if (analysis_state == 0) {
        section_sum1 +=  arr[i];
        analysis_state = 2;
      } else if (analysis_state == 1) {
        section_sum1 += arr[i];
        analysis_state = 2;
      } else if (analysis_state == 2) {
        section_sum2 += arr[i];
        analysis_state = 1;
      } else {
        std::cout << "\nDead code area, something went wrong.\n";
      }
    } else {
      if (section_sum1 >= section_sum2) {
        sum += section_sum1;
      } else {
        sum += section_sum2;
      }
      section_sum1 = 0;
      section_sum2 = 0;
      analysis_state = 0;
    }
  }

  if (section_sum1 >= section_sum2) {
    sum += section_sum1;
  } else {
    sum += section_sum2;
  }

  return sum;

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string arr_temp_temp;
    getline(cin, arr_temp_temp);

    vector<string> arr_temp = split_string(arr_temp_temp);

    vector<int> arr(n);

    for (int i = 0; i < n; i++) {
        int arr_item = stoi(arr_temp[i]);

        arr[i] = arr_item;
    }

    int res = maxSubsetSum(arr);

    cout << res << "\n";

    fout.close();

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
