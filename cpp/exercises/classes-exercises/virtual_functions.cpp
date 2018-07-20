/*
Create three classes Person, Professor and Student.
The class Person should have data members name and age. The classes Professor
and Student should inherit from the class Person.

The class Professor should have two integer members: publications and cur_id.
  - There will be two member functions: getdata and putdata.
    - The function getdata should get the input from the user: the name, age and
     publications of the professor.
    - The function putdata should print the name, age, publications and the
     cur_id of the professor.

The class Student should have two data members: marks, which is an array of size
6 and cur_id.
  - It has two member functions: getdata and putdata.
    - The function getdata should get the input from the user: the name, age,
     and the marks of the student in subjects.
    - The function putdata should print the name, age, sum of the marks and the
     cur_id of the student.

For each object being created of the Professor or the Student class, sequential
id's should be assigned to them starting from .

Virtual functions, constructors and static variables.

Input Format:

The first line of input contains the number of objects that are being created.
If the first line of input for each object is 1, it means that the object being
created is of the Professor class, auto input the name, age and publications of
the professor.

If the first line of input for each object is 2, it means that the object is of
the Student class, auto input the name, age and the marks of the student in 6
subjects.

Output Format:

There are two types of output depending on the object.

If the object is of type Professor, print the space separated name, age,
publications and id on a new line.

If the object is of the Student class, print the space separated name, age, the
sum of the marks in  subjects and id on a new line.

Sample Input:

4
1
Walter 56 99
2
Jesse 18 50 48 97 76 34 98
2
Pinkman 22 10 12 0 18 45 50
1
White 58 87

*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

static int professors = 0;
static int students = 0;


class Person {
public:
    string name;
    int age;
    virtual void getdata() {
    cin >> name >> age;
    }
    virtual void putdata() {
        cout << name << " " << age << endl;
    }

 };

class Professor: public Person {
  public:
    int cur_id;
    int publications;
// Get the input from the user: the name, age and
// publications of the professor.
    void getdata () {
      cin >> name;
      cin >> age;
      cin >> publications;
      cur_id = ++professors;
    }
// Print the name, age, publications and the
// cur_id of the professor.
    void putdata () {
      cout << name << ' ' << age << ' ' << publications << ' ' << cur_id << endl;
    }
};

class Student: public Person {
  public:
    int cur_id;
    int marks[6];

// - The function getdata should get the input from the user: the name, age,
// and the marks of the student in subjects.
    void getdata () {
      cin >> name;
      cin >> age;
      for (int i = 0; i < 6; i++) {
        cin >> marks[i];
      }
      cur_id = ++students;
    }

// - The function putdata should print the name, age, sum of the marks and the
// cur_id of the student.
    void putdata () {
      int sum = 0;
      for (int i = 0; i < 6; i++) {
        sum += marks[i];
      }
      cout << name <<' ' << age <<' ' << sum <<' ' << cur_id << endl;
    }

  };


int main(){

  int n, val;
  cin>>n; //The number of objects that is going to be created.
  Person *per[n];

  for(int i = 0;i < n;i++){

    cin>>val;
    if(val == 1){
        // If val is 1 current object is of type Professor
      per[i] = new Professor;

    }
    else per[i] = new Student; // Else the current object is of type Student

    per[i]->getdata(); // Get the data from the user.

  }

  for(int i=0;i<n;i++)
    per[i]->putdata(); // Print the required output for each object.

  return 0;
}
