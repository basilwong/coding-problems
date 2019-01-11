#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Finds the max subset of a vector. No adjacent values.
int maxSubsetSum(vector<int> arr) {
  if (arr.size() == 0) {
    return 0;
  }
  arr[0] = std::max(0, arr[0]);
  if (arr.size() == 1) {
    return arr[0];
  }
  arr[1] = max(arr[0], arr[1]);
  for (int i = 2; i < arr.size(); i++) {
    arr[i] = max(arr[i-1], arr[i] + arr[i-2]);
  }
  return arr[arr.size() - 1];
}

// Tests the
void test2() {
  static const int arr_test1[] = {0, 7, -4, 1, 5};
  std::vector<int> vec_test1 (arr_test1, arr_test1 + sizeof(arr_test1) / sizeof(arr_test1[0]) );
  std::cout << "Test 1: 0 7 4 -1 5\n";
  int result1 = maxSubsetSum(vec_test1);
  std::cout << "Expected Result: 12\n";
  std::cout << "Actual Result: " << result1;

  std::cout << "\n\n";

  static const int arr_test2[] = {2, 1, 5, 8, 4};
  std::vector<int> vec_test2 (arr_test2, arr_test2 + sizeof(arr_test2) / sizeof(arr_test2[0]) );
  std::cout << "Test 1: 2 1 5 8 4\n";
  int result2 = maxSubsetSum(vec_test2);
  std::cout << "Expected Result: 11\n";
  std::cout << "Actual Result: " << result2;

  std::cout << "\n\n";

  static const int arr_test3[] = {3, 5, -7, 8, 10};
  std::vector<int> vec_test3 (arr_test3, arr_test3 + sizeof(arr_test3) / sizeof(arr_test3[0]) );
  std::cout << "Test 1: 3 5 -7 8 10\n";
  int result3 = maxSubsetSum(vec_test3);
  std::cout << "Expected Result: 15\n";
  std::cout << "Actual Result: " << result3;
}

int main()
{
  test2();
    // ofstream fout(getenv("OUTPUT_PATH"));
    //
    // int n;
    // cin >> n;
    // cin.ignore(numeric_limits<streamsize>::max(), '\n');
    //
    // string arr_temp_temp;
    // getline(cin, arr_temp_temp);
    //
    // vector<string> arr_temp = split_string(arr_temp_temp);
    //
    // vector<int> arr(n);
    //
    // for (int i = 0; i < n; i++) {
    //     int arr_item = stoi(arr_temp[i]);
    //
    //     arr[i] = arr_item;
    // }
    //
    // int res = maxSubsetSum(arr);
    //
    // cout << res << "\n";
    //
    // fout.close();
    //
    // return 0;
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
