#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <cstdlib>
#include <stdio.h>

using namespace std;

int main () {
  string line;
  ifstream myfile ("search_domain.txt");
  if (myfile.is_open())
  {
    while ( getline (myfile,line) )
    {

      string url_val = line.substr(0,1);
      string url_link = line.substr(1);
      if(strcmp( url_val.c_str(), "0") != 0){
      	cout << line.at(0) << '\n';
      	system( ("timeout 2 python3.7 TextRipper/TextRipper.py " + url_link).c_str() );
        } 
      else{
      	cout << line.at(0) << '\n';
      	system( ("timeout 1 python3.7 TextRipper/Text_null_Ripper.py " + url_link).c_str() ); 
	}
    }
    myfile.close();
  }

  else cout << "Unable to open file"; 

  return 0;
}
