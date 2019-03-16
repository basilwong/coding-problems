#include "str_functions.h"
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

// Parsing a protocol where each element consists of a starting and ending tag,
// and there are attributes associated with each tag. Only starting tags can
// have attributes. We can call an attribute by referencing the tag, followed by
//  a tilde, '~' and the name of the attribute. The tags may also be nested.

// Parses a custom protocol. Sorry for the uber long function!
void atrbute_parser(){

  int N, Q;
  std::vector< int > tags_before; // the tag the index tag is contained in (0) if none
  tags_before.resize(11); // the max size referenced in the problem
  std::vector< std::vector< int > > tags_after; // the tag number that the index tags contains
  std::vector< std::vector< std::string > > attribute_names;
  std::vector< std::vector< std::string > > attribute_values;
  attribute_names.resize(11);
  attribute_values.resize(11);

  std::vector< int > a (10, 0);
  for (int i = 0; i < 11; i++) {
    tags_after.push_back(a);
  }

  std::cin>>N>>Q;

  std::string temp = "";
  std::string token;
  std::string value;
  std::string string_tag;
  int tag = 0;
  int current_tag = 0;

  for (int i = 0; i < N + 1; i++) {
    // Get one of the lines containing tag definitions.
    std::getline(std::cin, temp);
    std::stringstream ss(temp);
    // Processing each of the words.
    while (getline(ss, token, ' ')) {
      if (token.at(0) == '<') { // tag
        if (token.at(1) == '/') { //closing tag
          current_tag = tags_before[current_tag];
        } else { // opening tag
          string_tag = token.back();
          std::stringstream s1(string_tag);
          s1 >> tag;
          tags_after[current_tag][tag] = tag;
          tags_before[tag] = current_tag;
          current_tag = tag;
        }

      } else if (token.at(0) == '"') { // the token is a value
        value = token.substr (1,1000);
        value.pop_back();
        value.pop_back();
        attribute_values[current_tag].push_back(value);
      } else if (token.at(0) == '=') { // skip if it is an equals sign

      } else { // the call name for the values
        attribute_names[current_tag].push_back(token);
      }
    }
  }

  current_tag = 1;

  for (int j = 0; j < Q; j++) {
    // Get one of the lines containing tag definitions.
    std::getline(std::cin, temp);
    std::stringstream ss(temp);
    // Processing each of the words.
    while (getline(ss, token, '.')) {
      size_t tilda = token.find("~");
      if (tilda != std::string::npos) { // Requesting a value.
        string_tag = token.substr(3, (tilda - 3));
        std::stringstream s1(string_tag);
        s1 >> tag;
        current_tag = tag;
        value = token.substr(tilda + 1, 1000);
        ptrdiff_t pos = find(attribute_names[current_tag].begin(),
                             attribute_names[current_tag].end(), value) -
                             attribute_names[current_tag].begin();
        if(pos >= attribute_names[current_tag].size()) {
            std::cout << "Not Found!" << std::endl;
          } else {
            std::cout << attribute_values[current_tag][pos] << std::endl;
          }
        current_tag = 1;
      } else if (token.find("tag") == std::string::npos) { // requesting a value
          ptrdiff_t pos = find(attribute_names[current_tag].begin(),
                             attribute_names[current_tag].end(), token) -
                             attribute_names[current_tag].begin();
          if(pos >= attribute_names[current_tag].size()) {
            std::cout << attribute_values[current_tag][pos] << std::endl;
          } else {
            std::cout << "Not Found!" << std::endl;
          }
          current_tag = 1;
      } else { // specifying a tag
        string_tag = token.substr(3, 1000);
        std::stringstream s1(string_tag);
        s1 >> tag;
        current_tag = tag;
      }
    }
  }
}

/*

Custom Input:

12 8
<tag1 value = "HelloWorld">
<tag2 name = "Name1">
<tag3 name = "Name3">
</tag3>
<tag4 name = "Name4" text = "Super">
<tag6 buzz = "Buzz6">
</tag6>
</tag4>
<tag5>
</tag5>
</tag2>
</tag1>
tag1.tag2~name
tag1~name
tag1~value
tag1.tag2.tag3~name
tag1.tag2.tag3~value
tag1.tag2.tag4~text
tag1.tag2.tag4.tag6~text
tag1.tag2.tag4.tag6~buzz

*/

int main() {
  atrbute_parser();
  return 0;
}
