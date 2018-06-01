#include "str_functions.h"
#include <iostream>
#include <string>
using namespace std;

/*
abcd
ef
*/

// Assumes two strings as input through cin. Prints the length of the two
// strings, the concatenation of the two strings, and the two strings separated
// by a space with their first elements swapped.
void strings(){

  string input1;
  string input2;
  int len1;
  int len2;
  char char1;
  char char2;
  string con;
  string output1;
  string output2;

  cin>>input1>>input2;

  len1 = input1.size();
  len2 = input2.size();

  char1 = input1[0];
  char2 = input2[0];

  con = input1 + input2;

  output1 = input1;
  output1[0] = char2;
  output2 = input2;
  output2[0] = char1;

  cout<<len1<<" "<<len2<<endl;
  cout<<con<<endl;
  cout<<output1<<" "<<output2;



}
