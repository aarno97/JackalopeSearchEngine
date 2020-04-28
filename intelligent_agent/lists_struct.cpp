#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <list>
#include <vector> 
#include <iterator>

//g++11 -o runthisc intelligent_agent/Link_list.cpp intelligent_agent/Link_list.h intelligent_agent/main.cpp 
using namespace std;


struct Url_list_member{

	string url_str;
	list<list<float>> a_list;
	list<list<int>> temp_list;
	list<list<int>> b_list;
	list<list<int>> c_list;
	};

int main (){
		
	string line;
	std::list<string> url_list;
	std::list<string>::iterator it;

	ifstream myfile ("example_nlp_output");

	if (myfile.is_open())
	{
	while ( getline (myfile,line) )
	{

	url_list.push_back(line);

	}
	myfile.close();																											   
	}

	else cout << "Unable to open file";


	int countlog;
	int first_url = 1;
	int query_end = 0;
	int halt_pos = 0;
	int next_url = 0;
	int kill_switch = 0;
	float special = 0.0;
	it=url_list.begin();
	string last_url = "";
	string temp_str;
	list<Url_list_member> member_list;
	list<Url_list_member>::iterator url_it;
	url_it = member_list.begin();
	Url_list_member new_member;

	int last_webpage_pos;
	int webpage_pos;
	int query_pos;
	string url_str;
	float nlp_comp;


	list<list<float>>::iterator a_it;
	list<list<int>>::iterator b_it;
	list<list<int>>::iterator c_it;


	list<float>::iterator a_x_it;
	list<float> new_list;

	for (int countlog = 0; countlog < url_list.size(); countlog++){
		//url_str = *it;
		++it;
		countlog++;
		temp_str = *it;
		query_pos = std::stoi(temp_str);
		++it;
		countlog++;
		temp_str = *it;
		last_webpage_pos = webpage_pos;	
		webpage_pos = std::stoi(temp_str);  

		++it;
		countlog++;
		temp_str = *it;

		nlp_comp = std::stof(temp_str);  
		
		countlog++;
		if (countlog < url_list.size()){
			++it;
			}
		if (first_url == 0 && query_pos == 0){
			query_end = 1;
		}
		
		if(first_url == 1){
			//last_url = url_str;	
			first_url = 0;
			
			new_list.clear();
			new_list.push_back(nlp_comp);
				
			new_member.a_list.push_back(new_list);
		}
		else if(query_end == 0){
			halt_pos++;
			new_list.clear();
			new_list.push_back(nlp_comp);
			new_member.a_list.push_back(new_list);
		}

		else if(last_webpage_pos <= webpage_pos){


			a_it = new_member.a_list.begin();
			
			for(int i = 0; i < query_pos; i++){

			a_it++;
			}
			new_list.clear();
			new_list = *a_it;
			new_list.push_back(nlp_comp);
			*a_it = new_list;				


		}
		
		else{

			std::advance(it,-8);
			url_str = *it;
			std::advance(it,8);

			//cout<< "URL  " << url_str << " \n";
			//cout<< "Memebers  " << new_member.a_list.size() << " \n";
			a_it = new_member.a_list.begin();
			new_list.clear();
			new_list = *a_it;
			if(next_url == 1){
				cout<< "POP! \n";
				new_list.push_front(special);
				*a_it = new_list;
				}
			/*
			cout<< "List  " << new_list.size() << " \n";
			cout<< "Front " << new_list.front() << " \n";
			cout<< "Last  " << new_list.back() << " \n";
			++a_it;
			new_list = *a_it;
			cout<< "List  " << new_list.size() << " \n";
			cout<< "Front " << new_list.front() << " \n";
			cout<< "Last  " << new_list.back() << " \n";
			++a_it;
			new_list = *a_it;
			cout<< "List  " << new_list.size() << " \n";
			cout<< "Front " << new_list.front() << " \n";
			cout<< "Last  " << new_list.back() << " \n";
			*/
			
			member_list.push_back(new_member);
			a_it = new_member.a_list.begin();
			
			list<float> newer_list;
			
			for (int i = 0; i<= halt_pos; i++){
				newer_list = *a_it;
				newer_list.clear();
				*a_it = newer_list;
				a_it++;
			}
				
			
			last_url = url_str;	
			
			special = nlp_comp;
			
			next_url = 1;
			
			kill_switch++;
			if (kill_switch > 1){
				break;
				}
			
		}
		
	
	}

	cout<< "URL List  " << member_list.size() << " \n";
	url_it = member_list.begin();
	std::list<float>::iterator f_it;
	for (int i = 0; i< member_list.size(); i++){
		Url_list_member this_member = *url_it;
		cout << "This mem size " << this_member.a_list.size() << " \n";
		a_it = this_member.a_list.begin();
		list<list<int>> hit_matrix;
		for (int j = 0; j < this_member.a_list.size(); j++){
			list<float> sub_list = *a_it;
			cout << "This sub mem size " << sub_list.size() << " \n";

			float k_var = 0;
			float x_var = 0;
			float y_var = 0;
			float z_var = 0;
			f_it = sub_list.begin();
			list<int> pos_hit_locs;
			int hit_loc = 0;
			for(int k = 0; k < sub_list.size(); k++){
				k_var = *f_it;
				if(k_var > 0.0){
					x_var++;
				}
				y_var += k_var;
				++f_it;
				}
			float raw_ave = y_var/x_var;
			raw_ave = (raw_ave + 0.5)/2;
			f_it = sub_list.begin();
			
			for(int k = 0; k < sub_list.size(); k++){
				k_var = *f_it;
				if(k_var > raw_ave){
					pos_hit_locs.push_back(hit_loc);
					z_var++;
				}
				hit_loc++;
				++f_it;
				}
			cout<< " Positive comps :: "<< x_var << " \n";
			cout<< " sum :: "<< y_var << " \n";
			cout<< " ave :: "<< raw_ave << " \n";
			
			cout<< " Positive ave :: "<< y_var/x_var << " \n";
			cout<< " Positive ave hits :: "<< z_var << " \n";
			for (auto v : pos_hit_locs){
				std::cout << v << " ";
			}
			hit_matrix.push_back(pos_hit_locs);	
		cout<<" \n";
		a_it++;
		
		}
		this_member.temp_list = hit_matrix;
		*url_it = this_member;
		++url_it;
		
		}
	url_it = member_list.begin();
	std::list<list<int>>::iterator temp_it_0;
	std::list<list<int>>::iterator temp_it_1;

	std::list<int>::iterator sub_it_0;
	std::list<int>::iterator sub_it_1;

	for (int i = 0; i< member_list.size(); i++){
		Url_list_member this_member = *url_it;
		temp_it_0 = this_member.temp_list.begin();
		temp_it_1 = this_member.temp_list.begin();
		++temp_it_1;

		for (int j = 1; j < this_member.temp_list.size(); j++){
			list<int> temp_b_list;
			list<int> sub_temp_0 = *temp_it_0;

			sub_it_0 = sub_temp_0.begin();

			for (int sub_0 = 0; sub_0 < sub_temp_0.size(); sub_0++){
				int int_0 = *sub_it_0;
				list<int> sub_temp_1 = *temp_it_1;
				sub_it_1 = sub_temp_1.begin();
				for (int sub_1 = 0; sub_1 < sub_temp_1.size(); sub_1++){
					int int_1 = *sub_it_1;
					if (int_0 < int_1){
						temp_b_list.push_back(int_0);
						temp_b_list.push_back(int_1);
						temp_b_list.push_back(int_1-int_0);
						break;
					}
					++sub_it_1;
	
				}

				++sub_it_0; 
				}
			this_member.b_list.push_back(temp_b_list);	
			++temp_it_0;	
			++temp_it_1;		
			}
		temp_it_0 = this_member.temp_list.begin();
		temp_it_1 = this_member.temp_list.begin();
		++temp_it_1;
		++temp_it_1;
		for (int j = 2; j < this_member.temp_list.size(); j++){
			list<int> temp_b_list;
			list<int> sub_temp_0 = *temp_it_0;

			sub_it_0 = sub_temp_0.begin();

			for (int sub_0 = 0; sub_0 < sub_temp_0.size(); sub_0++){
				int int_0 = *sub_it_0;
				list<int> sub_temp_1 = *temp_it_1;
				sub_it_1 = sub_temp_1.begin();
				for (int sub_1 = 0; sub_1 < sub_temp_1.size(); sub_1++){
					int int_1 = *sub_it_1;
					if (int_0 < int_1){
						temp_b_list.push_back(int_0);
						temp_b_list.push_back(int_1);
						temp_b_list.push_back(int_1-int_0);
						break;
					}
					++sub_it_1;
	
				}

				++sub_it_0; 
				}
			this_member.c_list.push_back(temp_b_list);	
			++temp_it_0;	
			++temp_it_1;		
			}
		*url_it = this_member;
		++url_it;
		}

	return 0;
	}			

