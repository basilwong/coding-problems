#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Prints what numbers in the cost vector add up to exactly the money input.
void whatFlavors(vector<int> cost, int money) {

  bool found = false;
  int id1, id2, left, right, mid, val, price1, price2;
  std::map<int, std::vector<int> > table;
  // Adding values to a table to save the IDs of their order.
  for (int i = 0; i < cost.size(); i++) {
    std::vector<int> a = {};
    table.insert(std::pair<int,std::vector<int> >(cost[i], a));
  }
  for (int x = 0; x < cost.size(); x++) {
    table[cost[x]].push_back(x);
  }
  // Now that the IDs are saved we sort the valeus in the cost vector.
  std::sort (cost.begin(), cost.end());

  for (int j = 0; j < cost.size(); j ++) {
    if (found) {
      break;
    }
    left = j + 1;
    right = cost.size() - 1;
    mid = (left + right) / 2;
    val = money - cost[j];

    while (left <= right) {
      mid = (left + right) / 2;
      if (cost[mid] == val) {
        price1 = cost[j];
        price2 = cost[mid];
        found = true;
        break;
      } else if (cost[mid] > val) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    }
  }

  id1 = table[price1][0];
  id2 = table[price2][0];
  if (id1 == id2) {
    id2 = table[price2][1];
  }
  if (id2 < id1) {
    std::swap(id1, id2);
  }

  std::cout << (id1 + 1) << " " << (id2 + 1) << "\n";
}

int main()
{
    int t;
    cin >> t;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int t_itr = 0; t_itr < t; t_itr++) {
        int money;
        cin >> money;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        int n;
        cin >> n;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        string cost_temp_temp;
        getline(cin, cost_temp_temp);

        vector<string> cost_temp = split_string(cost_temp_temp);

        vector<int> cost(n);

        for (int i = 0; i < n; i++) {
            int cost_item = stoi(cost_temp[i]);

            cost[i] = cost_item;
        }

        whatFlavors(cost, money);
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
