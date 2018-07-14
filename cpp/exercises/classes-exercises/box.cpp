#include "headerc.h"
#include <iostream>
#include <sstream>
using namespace std;

class Box {
private:
  long l;
  long b;
  long h;
public:
  Box(): l(0), b(0), h(0) {}

  Box(int length, int breadth, int height): l(length), b(breadth), h(height) {}

  friend bool operator<(Box& a, Box& b) {
    if (a.l < b.l) {
      return true;
    }
    if ((a.b < b.b) && (a.l == b.l)) {
      return true;
    }
    if ((a.h < b.h) && (a.b == b.b) && (a.l == b.l)) {
      return true;
    }
    return false;
  }

  friend ostream& operator<<(ostream& out, Box& B) {
    out << B.l << " " << B.b << " " << B.h;
    return out;
  }

  // Return box's length
  int getLength() {
    return l;
  }

  // Return box's breadth
  int getBreadth() {
    return b;
  }

  // Return box's height
  int getHeight() {
    return h;
  }

  // Return the volume of the box
  long long CalculateVolume() {
    long long volume = l * b * h;
    return volume;
  }

};
