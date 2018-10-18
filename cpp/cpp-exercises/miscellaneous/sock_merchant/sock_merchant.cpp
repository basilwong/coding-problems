#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Counts the pairs of socks in ar. 
//
// n is the number of individual socks.
// ar is a vector containing socks.
// Each integer in ar represents a sock and the value of the integer represents 
// the sock's colour.
int sockMerchant(int n, vector<int> ar) {
  
  int pairs = 0;
  std::map<int,int> sock_colour;
  std::map<int,int>::iterator it;
  
  for (int i = 0; i < n; i++) {
    it = sock_colour.find(ar[i]);
    if (it == sock_colour.end()) {
      sock_colour[ar[i]] = 1;
    } else {
      if (sock_colour[ar[i]] == 1) {
        sock_colour[ar[i]] = 0;
        pairs++;
      } else {
        sock_colour[ar[i]] = 1;
      }
    }
  }
  return pairs;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string ar_temp_temp;
    getline(cin, ar_temp_temp);

    vector<string> ar_temp = split_string(ar_temp_temp);

    vector<int> ar(n);

    for (int i = 0; i < n; i++) {
        int ar_item = stoi(ar_temp[i]);

        ar[i] = ar_item;
    }

    int result = sockMerchant(n, ar);

    fout << result << "\n";

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
