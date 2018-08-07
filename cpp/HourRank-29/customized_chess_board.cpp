#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

// Complete the solve function below.
string solve(vector<vector<int>> board) {
    int N = board.size();
    
    if (N == 0) {
        return "Yes";
    }
    
    // Check the 0th cell.
    int root = board[0][0];
    
    // Check diagonal.
    for (int i = 1; i < N; i++) {
        if (board[i][i] != root) {
            return "No";
        }
    }
    
    //Check top half.
    int row;
    int sum;
    int check;
    for (int a = 1; a < N; a++) {
        row = 0;
        sum = 0;
        check = (a + root) % 2;
        std::cout << check << "\n"; // checking if the above thing is a thing
        for (int b = a; b < N; b++) {
            if (board[row][b] != check) {
                return "No";
            }
            row++;
        }
    }
    
    //Check bottom half.
    int column;
    for (int a = 1; a < N; a++) {
        column = 0;
        sum = 0;
        check = (a + root) % 2;
        std::cout << check << "\n"; // checking if the above thing is a thing
        for (int b = a; b < N; b++) {
            if (board[b][column] != check) {
                return "No";
            }
            column++;
        }
    }
    
    return "Yes";
    
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string t_temp;
    getline(cin, t_temp);

    int t = stoi(ltrim(rtrim(t_temp)));

    for (int t_itr = 0; t_itr < t; t_itr++) {
        string n_temp;
        getline(cin, n_temp);

        int n = stoi(ltrim(rtrim(n_temp)));

        vector<vector<int>> board(n);

        for (int i = 0; i < n; i++) {
            board[i].resize(n);

            string board_row_temp_temp;
            getline(cin, board_row_temp_temp);

            vector<string> board_row_temp = split(rtrim(board_row_temp_temp));

            for (int j = 0; j < n; j++) {
                int board_row_item = stoi(board_row_temp[j]);

                board[i][j] = board_row_item;
            }
        }

        string result = solve(board);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
