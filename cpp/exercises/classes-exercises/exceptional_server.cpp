/*
The compute function of the Server class can output certain exceptions when the
output is not standard. These exceptions are handled in the main function.
*/

#include <iostream>
#include <exception>
#include <string>
#include <stdexcept>
#include <vector>
#include <cmath>
using namespace std;

/*
Sample Input:

2
-8 5
1435434255433 5
*/

class Server {
private:
	static int load;
public:
	static int compute(long long A, long long B) {
		load += 1;
		if(A < 0) {
			throw std::invalid_argument("A is negative");
		}
		vector<int> v(A, 0);
		int real = -1, cmplx = sqrt(-1);
		if(B == 0) throw 0;
		real = (A/B)*real;
		int ans = v.at(B);
		return real + A - B*ans;
	}
	static int getLoad() {
		return load;
	}
};
int Server::load = 0;

int main() {
	int T; cin >> T;
	while(T--) {
		long long A, B;
		cin >> A >> B;
    // Handling of the 'compute' exceptions.
    // -------------------------------------------------------------------------
    Server server;
    int x;
    try {
    x = server.compute(A, B);
  } catch (std::bad_alloc e) {
    std::cout << "Not enough memory\n";
    continue;
  } catch (std::exception& e) {
    std::cout << "Exception: " << e.what() << "\n";
    continue;
  } catch(...) {
    std::cout << "Other Exception\n";
    continue;
  }
    std::cout << x << "\n";

    // -------------------------------------------------------------------------
  }
  cout << Server::getLoad() << endl;
  return 0;
}
