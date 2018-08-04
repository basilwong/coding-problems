#include <bits/stdc++.h>
#include <iostream>
#include <iomanip>
#include <functional>
#include <queue>
#include <vector>
#include <cstdlib> 

using namespace std;

// Finds the running medium of the inputted set of numbers. 
class MedianFinder {
    
private:
    std::priority_queue< int > lowers;
    std::priority_queue< int, std::vector< int >, std::greater< int > > highers;
    std::vector< double > medians;
    
    // Add the number to the two heaps (in this case priority queues) so that the number doesn't
    // change the min and max.
    void add_num(int i) {
        if ((lowers.empty()) || (i < lowers.top())) {
            // std::cout << "Adding " << i << " to lowers.\n";
            lowers.push(i);
        } else {
            // std::cout << "Adding " << i << " to highers.\n";
            highers.push(i);
        }
    }

    // Make sure the sizes of the heaps are within 1 in size.
    void rebalance() {
        int high_size = highers.size();
        int low_size = lowers.size();
        if (low_size - high_size > 1) {
            highers.push(lowers.top());
            lowers.pop();
        } else if (low_size - high_size < -1) {
            lowers.push(highers.top());
            highers.pop();
        }
    }
    
    // Find the current median using the two heaps. Assumes both heaps are not empty and have 
    // sizes within 1 of each other. 
    double current_median() {
        if (lowers.size() - highers.size() == 0) {
            if (! lowers.empty()) {
                return (double) (lowers.top() + highers.top()) / 2;
            } else {
                std::cout << "\n\nHeaps are empty.\n\n";
                return 0;
            }
        } else if (lowers.size() - highers.size() == 1) {
            return (double) lowers.top();
        } else if (lowers.size() - highers.size() == -1) {
            return (double) highers.top();
        } else {
            std::cout << "\n\nIssue with heap sizes.\n\n";
            return 0;
        }
        
    }
    
    // Print all the medians found in the input of get_medians.
   void print_medians() {
        cout << std::setprecision(1) << std::fixed;
        for (auto& x : medians) {
            std::cout << x << std::endl;
        }
    }
        
public:
    // Takes a vector of ints and prints the running median as the function iterates through 
    // each value of the input from the 0th element to the nth element. 
    void get_medians(std::vector< int > input) {
        // Clear the class memebers.
        lowers = priority_queue < int >(); 
        highers = std::priority_queue< int, std::vector< int >, std::greater< int > >();
        medians.clear();
        
        // Adds the values to the class members and calculates the running median each loop.
        for (auto& i : input) {
            add_num(i);
            rebalance();
            medians.push_back(current_median());
        }
        
        // Prints the list of running medians.
        print_medians();
    }
    
};



int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    vector< int > a(n);

    for (int i = 0; i < n; i++) {
        int a_item;
        cin >> a_item;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        a[i] = a_item;
    }
    
    MedianFinder m;
    
    m.get_medians(a);
    
    return 0;
}
