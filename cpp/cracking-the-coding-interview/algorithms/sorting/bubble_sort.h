#include <bits/stdc++.h>
#include <algorithm>
#include <vector>

using namespace std;

vector<string> split_string(string);

// Complete the countSwaps function below.
void countSwaps(vector<int> a) {
    int unsorted_length = a.size() - 1;
    int num_swaps = 0;
    bool is_unsorted = false;
    
    while (! is_unsorted) {
        is_unsorted = true;
        
        for (int i = 0; i < unsorted_length; i++) {
            if (a[i] > a[i + 1]) {
                std::swap(a[i], a[i + 1]);
                is_unsorted = false;
                num_swaps++;
            }
        }
        
        unsorted_length--;
    }
    
    std::cout << "Array is sorted in " << num_swaps << " swaps.\n";
    std::cout << "First Element: " << a[0] << "\n";
    std::cout << "Last Element: " << a[a.size() - 1] << "\n";

}

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string a_temp_temp;
    getline(cin, a_temp_temp);

    vector<string> a_temp = split_string(a_temp_temp);

    vector<int> a(n);

    for (int i = 0; i < n; i++) {
        int a_item = stoi(a_temp[i]);

        a[i] = a_item;
    }

    countSwaps(a);

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
