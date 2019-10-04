#include <iostream>
#include <cstdio>
using namespace std;


void forLoop() {

    string printed [10] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

    int bottom, top;

    cin>>bottom>>top;

    for (int i = bottom; i <= top; i++) {
        if (i <= 9) {
            cout<<printed[i]<<endl;
        } else if (i%2 ==0){
            cout<<"even"<<endl;
        }else {
            cout<<"odd"<<endl;
        }

    }
}
