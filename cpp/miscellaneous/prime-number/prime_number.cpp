#include <bits/stdc++.h>

using namespace std;

/*
Prints whether the input was a prime number or not.

- if number is 0 or 1: not prime
- if the number has a factor of 2: not prime
- check all the odd numbers starting from 3 and below sqrt(n) to see if they
are factors of n: if so not prime
- if the number is 2: prime

*/
string primality(int n) {
  bool prime = false;
  if (n > 1) {
    prime = true;
    if (n % 2 == 0) {
      prime = false;
    }
    for (int x = 3; x <= std::sqrt(n); x += 2) {
      if (n % x == 0) {
        prime = false;
      }
    }
  }
  if (n == 2) {
    prime = true;
  }
  if (prime) {
    return "Prime";
  } else {
    return "Not prime";
  }
}

// Main function for testing primality function.
int main()
{
  int count = 0;
  for (int i = 1; i < 100; i++) {
    if (primality(i) == "Prime") {
      count++;
      std::cout << i << "\n";
    }
  }
  std::cout << "\n\n";
  std::cout << count << "\n";

  // ofstream fout(getenv("OUTPUT_PATH"));
  //
  // int p;
  // cin >> p;
  // cin.ignore(numeric_limits<streamsize>::max(), '\n');
  // 
  // for (int p_itr = 0; p_itr < p; p_itr++) {
  //     int n;
  //     cin >> n;
  //     cin.ignore(numeric_limits<streamsize>::max(), '\n');
  //
  //     string result = primality(n);
  //
  //     fout << result << "\n";
  // }
  //
  // fout.close();
}
