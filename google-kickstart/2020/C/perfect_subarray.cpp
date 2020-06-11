#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int N;
int arr[100000];
int prefix_sum[100000];

bool isPerfectSquare(int x)
{
  // Find floating point value of
  // square root of x.
  long double sr = sqrt(x);

  // If square root is an integer
  return ((sr - floor(sr)) == 0);
}

void gogo()
{
    int count = 0;
    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> arr[i];

    prefix_sum[0] = arr[0];
    count += isPerfectSquare(arr[0]) ? 1 : 0;

    for (int i = 1; i < N; i++) {
      prefix_sum[i] = prefix_sum[i - 1] + arr[i];
      if (isPerfectSquare(prefix_sum[i])) {
        count += 1;
        // cout << "P-square " <<  prefix_sum[i] << " " << i << "\n";
      }
    }

    for (int i = 0; i <= N; i++) {
      for (int j = i+1; j <= N; j++) {
        if (isPerfectSquare(prefix_sum[j]-prefix_sum[i])){
            // cout << "P-square " <<  prefix_sum[j]-prefix_sum[i] << " " << i << " " << j << "\n";
            count += 1;
        }
      }
    }

    cout << count << "\n";
}


int main()
{
    ios_base::sync_with_stdio(0);

    int T; cin >> T;
    for (int i = 0; i < T; i++)
    {
        cout << "Case #" << i + 1 << ": ";
        gogo();
    }
}
