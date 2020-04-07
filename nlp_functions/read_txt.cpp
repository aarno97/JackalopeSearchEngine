#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <list>
#include <cstdlib>
#include <stdio.h>
#include <pthread.h>
#include <sys/sysinfo.h>

using namespace std;

void* screenData( void *filename );
pthread_mutex_t lock;

int main () {
  string line;
	std::list<string> url_list;
	std::list<string>::iterator it;

	ifstream myfile ("search_domain.txt");
	int nprocs = get_nprocs();
	nprocs = 16;
	pthread_t thread[nprocs];

  if (myfile.is_open())
  {
    while ( getline (myfile,line) )
    {

	url_list.push_back(line);

    }
    myfile.close();
  }
	


  else cout << "Unable to open file"; 
	std::cout << "mylist contains:";
	//it=url_list.begin();
        int countlog;
	it=url_list.begin();
	string last_str;
	for (int countlog = 0; countlog < url_list.size(); countlog++){
		//nst char *filename1 = this_str;

	int threads_to_run = 0;
	if (pthread_mutex_init(&lock, NULL) != 0) { 
		printf("\n mutex init has failed\n"); 
		return 1; 
	    } 
  	for (int i = 0; i < nprocs; i++){
		countlog++;
		const char *strNew = it->c_str();

		++it;
		if( pthread_create( &thread[i], NULL, screenData, (void*)strNew)  != 0)
		{
			return 0;
		}

		if (countlog >= url_list.size()){
			break;
		}
		else{

			threads_to_run++;
		}
	}
	for (int j = 0; j < threads_to_run; j++){
        	pthread_join( thread[j], NULL);
	}
	pthread_mutex_destroy(&lock);
	}
  return 0;
}

void* screenData( void *filename )
{
        char* name;
        name = (char*)filename;

        if(filename)
        {
		string this_name = name;
		string url_val = this_name.substr(0,1);
		string url_link = this_name.substr(1);
		if(strcmp( url_val.c_str(), "0") != 0){
		//pthread_mutex_lock(&lock);

		system( ("timeout 2 python3.7 TextRipper/TextRipper.py " + url_link + " >> logged_results"+url_val + " 2>&1").c_str() );
		//pthread_mutex_unlock(&lock); 
		} 
		else{
		system( ("timeout 1 python3.7 TextRipper/Text_null_Ripper.py " + url_link + " 2>&1" ).c_str() ); 
		}
		


        }

        return 0;
}
