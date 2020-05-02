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

int done01 = 1; 

pthread_barrier_t mybarrier;
string search_term;
int number_of_terms;
void* screenData( void *filename );
pthread_mutex_t lock;

void finalfunc();

struct Url_score{
	string url_str;
	int jump_score;
	int path_score;
	};

list<Url_score> perfect_list(list<Url_score> sort_list , int n, int m) {  
	int temp_n;
	std::list<Url_score>::iterator it;
	std::list<Url_score>::iterator i_it;
	std::list<Url_score>::iterator j_it;
	Url_score this_score;
	Url_score this_out;
	list<Url_score> return_out;
	it = sort_list.begin();
	for (int i = 0; i < sort_list.size(); i++) {
		this_score = *it;
		if (n == this_score.jump_score){ 
			if(m == this_score.path_score ) {
				return_out.push_front(this_score);
				}
			else if ( return_out.size() == 0){
				
				return_out.push_front(this_score);
				}

			else {
				j_it = return_out.begin();
				int back_flag = 0;
				for (int j = 0; j < return_out.size(); j++)	{
					this_out = *j_it;
					if(this_out.path_score > this_score.path_score) {
						return_out.insert(j_it, this_score);
						back_flag = 1;
						break;
						}
					++j_it;			
					}	
				if( back_flag == 0){

					return_out.push_back(this_score);
					}	
				} 
			}
		++it;
		}
	return return_out;
	}

void print_list(list<Url_score> sort_list ) { 
	int i;
	std::list<Url_score>::iterator i_it;
	Url_score temp_i;
	int score_i, score_j;
	i_it = sort_list.begin();
	for (i=0; i < sort_list.size(); i++){ 
		temp_i = *i_it;
		cout << temp_i.url_str << endl;
		cout << temp_i.jump_score << endl;
		cout << temp_i.path_score << endl;
		++i_it;
		}	
	}

int removeDupWord(string str){
	int return_out;
	return_out = 1;
	string word = "";
	for (auto x : str) {
		if (x == ' ')
		{
		   return_out++;
		}
		}
	return return_out;
	}

void write_list(list<Url_score> sort_list, string write_to_file, int n, int m) { 
	int i;
	std::list<Url_score>::iterator i_it;
	Url_score temp_i;
	int score_i, score_j;
	i_it = sort_list.begin();
	system( ("rm "+write_to_file ).c_str() );
	ofstream write_to;
	write_to.open(write_to_file.c_str());
	for (i=0; i < sort_list.size(); i++){ 
		temp_i = *i_it;
		write_to << temp_i.url_str << endl;
		if (temp_i.jump_score == n) {
			if (temp_i.path_score == m) {
				write_to << "Perfect Match. " << endl;
				}
			else {
				double this_rating = sort_list.size() - i;
				this_rating = this_rating/sort_list.size();
				this_rating = this_rating *100;
				std::string rating_str = std::to_string(this_rating);
				string sub_str = rating_str.substr(0, 5);
				string statement = "Near Perfect Match. Rated: " + sub_str +" Percent";
				write_to << statement << endl;
				}
			}
		else{

			if (temp_i.path_score == m) {
				write_to << "Strong Partial  Match. " << endl;
				}
			else {
				double this_rating = sort_list.size() - i;
				this_rating = this_rating/sort_list.size();
				this_rating = this_rating *100;
				std::string rating_str = std::to_string(this_rating);
				string statement = "Weak Match. Rated: " + rating_str +" Percent";
				write_to << statement << endl;
				}
			}
		
		++i_it;
		}	
	}

int main(int argc, char** argv) {
	string line;
	std::list<string> url_list;
	std::list<string>::iterator it;
	ifstream myfile ("multicore_index");

	int nprocs = 16;
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
	search_term = argv[1];
	
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

		if( pthread_create( &thread[i], NULL, screenData, (void*)strNew)  != 0) {
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
	printf("BING DONE\n");
	finalfunc();
	return 0;
	}


void finalfunc(){

	string line;
	std::list<string> url_list;
	std::list<string>::iterator it;

	

	

	std::list<string> collation_list;

	ifstream log_file01 ("nlp_01_log");

	if (log_file01.is_open())	{
		while ( getline (log_file01,line) )
		{
			collation_list.push_back(line);
		}
		log_file01.close();
	}


	ifstream log_file02 ("nlp_02_log");

	if (log_file02.is_open())	{
		while ( getline (log_file02,line) )
		{
			collation_list.push_back(line);
		}
		log_file02.close();
	}

	ifstream log_file03 ("nlp_03_log");

	if (log_file03.is_open())	{
		while ( getline (log_file03,line) )
		{
			collation_list.push_back(line);
		}
		log_file03.close();
	}

	ifstream log_file05 ("nlp_05_log");

	if (log_file05.is_open())	{
		while ( getline (log_file05,line) )
		{
			collation_list.push_back(line);
		}
		log_file05.close();
	}

	ifstream log_file06 ("nlp_06_log");

	if (log_file06.is_open())	{
		while ( getline (log_file06,line) )
		{
			collation_list.push_back(line);
		}
		log_file06.close();
	}

	ifstream log_file07 ("nlp_07_log");

	if (log_file07.is_open())	{
		while ( getline (log_file07,line) )
		{
			collation_list.push_back(line);
		}
		log_file07.close();
	}

	ifstream log_file08 ("nlp_08_log");

	if (log_file08.is_open())	{
		while ( getline (log_file08,line) )
		{
			collation_list.push_back(line);
		}
		log_file08.close();
	}

	ifstream log_file09 ("nlp_09_log");

	if (log_file09.is_open())	{
		while ( getline (log_file09,line) )
		{
			collation_list.push_back(line);
		}
		log_file09.close();
	}

	ifstream log_file10 ("nlp_10_log");

	if (log_file10.is_open())	{
		while ( getline (log_file10,line) )
		{
			collation_list.push_back(line);
		}
		log_file10.close();
	}

	ifstream log_file11 ("nlp_11_log");

	if (log_file11.is_open())	{
		while ( getline (log_file11,line) )
		{
			collation_list.push_back(line);
		}
		log_file11.close();
	}

	ifstream log_file12 ("nlp_12_log");

	if (log_file12.is_open())	{
		while ( getline (log_file12,line) )
		{
			collation_list.push_back(line);
		}
		log_file12.close();
	}

	ifstream log_file13 ("nlp_13_log");

	if (log_file13.is_open())	{
		while ( getline (log_file13,line) )
		{
			collation_list.push_back(line);
		}
		log_file13.close();
	}


	ifstream log_file14 ("nlp_14_log");

	if (log_file14.is_open())	{
		while ( getline (log_file14,line) )
		{
			collation_list.push_back(line);
		}
		log_file14.close();
	}

	ifstream log_file15 ("nlp_15_log");

	if (log_file15.is_open())	{
		while ( getline (log_file15,line) )
		{
			collation_list.push_back(line);
		}
		log_file15.close();
	}

	ifstream log_file16 ("nlp_16_log");

	if (log_file16.is_open())	{
		while ( getline (log_file16,line) )
		{
			collation_list.push_back(line);
		}
		log_file16.close();
	}


	it=collation_list.begin();
	string url_str;
	string temp_str;
	int jump_score;
	int path_score;
	list<Url_score> final_list;
	for (int countlog = 0; countlog < collation_list.size(); countlog++){
		Url_score new_mem;	
		url_str = *it;	
		++it;
		countlog++;
		temp_str = *it;
		jump_score = atoi(temp_str.c_str());		
		++it;
		countlog++;
		temp_str = *it;
		path_score = atoi(temp_str.c_str());		
		++it;
		new_mem.url_str = url_str;
		new_mem.jump_score = jump_score;
		new_mem.path_score = path_score;
		final_list.push_back(new_mem);
		}
	list<Url_score> all_urls;
	list<Url_score> ok_urls;
	std::list<Url_score>::iterator score_it;
	number_of_terms = removeDupWord(search_term);
	all_urls = perfect_list(final_list, number_of_terms, 1);
	ok_urls = perfect_list(final_list, number_of_terms-1, 1);
	//all_urls.merge(ok_urls);
	score_it = ok_urls.begin();
	Url_score temp_score;
	for (int i = 0; i < ok_urls.size(); i++){
		temp_score = *score_it;
		all_urls.push_back(temp_score);		
		++score_it;	
		}
	write_list(all_urls, "output_list", 3, 1);
	cout<< number_of_terms << endl;
	}

void* screenData( void *filename ) {
	char* name;
	name = (char*)filename;

        if(filename)
        {
		string this_name = name;
		string url_val = this_name.substr(0,2);
		string url_name = this_name.substr(2,this_name.length());
		system( ("SPACY_WARNING_IGNORE=W008 python3.7 nlp_functions/run_nlp.py '"+ search_term  +"' '"+ url_name +"' > nlp_"+url_val).c_str());
		system( ("timeout 240 ./run_agent 'nlp_"+url_val+"'").c_str() );
		//system( ("timeout 2 python3.7 TextRipper/TextRipper.py " + url_link + " >> logged_results"+url_val + " 2>&1").c_str() );
		
		
	}	
	return 0;
}
