#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the roadsAndLibraries function below.
long roadsAndLibraries(int n, int c_lib, int c_road, vector<vector<int>> cities) {

  if (c_lib <= c_road) {
    return c_lib * n;
  }

  long cost = 0;
  map<int, vector<int>> c;
  vector<bool> v(n + 1); // cities to visit

  // Add roads to map
  for (auto r : cities) {
      c[r[0]].push_back(r[1]);
      c[r[1]].push_back(r[0]);
    }

  for (int i = 1; i <= n; i++) {
    stack<int> s;
    int nodes = 0;

    if (!v[city]) {
      s.push(city);
      v[city] = true;

      while (!s.empty()) {
        int visit = s.top();
        s.pop();

        for (auto connected : c[visit]) {
          if (!v[connected]) {
            v[connected] = true;
            s.push(connected);
            nodes++;
          }
        }
      }
      result += (nodes) ? long(nodes) * c_road + c_lib : c_lib;
    }
  }
}
  }


  }

  if (!visited.empty()) {
    cost += (visited.size() - 1) * c_road;
    cost += c_lib;
    logged.insert(visited.begin(), visited.end());
  }

  cost += (n - logged.size()) * c_lib;

  return cost;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int q;
    cin >> q;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int q_itr = 0; q_itr < q; q_itr++) {
        string nmC_libC_road_temp;
        getline(cin, nmC_libC_road_temp);

        vector<string> nmC_libC_road = split_string(nmC_libC_road_temp);

        int n = stoi(nmC_libC_road[0]);

        int m = stoi(nmC_libC_road[1]);

        int c_lib = stoi(nmC_libC_road[2]);

        int c_road = stoi(nmC_libC_road[3]);

        vector<vector<int>> cities(m);
        for (int i = 0; i < m; i++) {
            cities[i].resize(2);

            for (int j = 0; j < 2; j++) {
                cin >> cities[i][j];
            }

            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }

        long result = roadsAndLibraries(n, c_lib, c_road, cities);

        fout << result << "\n";
    }

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
