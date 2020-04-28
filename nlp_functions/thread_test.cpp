#include <pthread.h> 
#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <unistd.h> 

void* screenData( void *filename );

int main(int argc, char *argv[])
{
	pthread_t thread[2];
	const char *filename1 = "some_directory/some_other/";
	const char *filename2 = "yet_some_directory/some_other/";
	/*your code was passing a pthread_t** instead of pthread_t* */
	if( pthread_create( &thread[0], NULL, screenData, (void*)filename1)  != 0)
	{
		return 0;
	}
	if( pthread_create( &thread[1], NULL, screenData, (void*)filename2)  != 0)
	{
		return 0;
	}
	pthread_join( thread[0], NULL);
	pthread_join( thread[1], NULL);
	return 0;
}

void* screenData( void *filename )
{
	char* name;
	if(filename)
	{
		name = (char*)filename;
		/*check your format specifier*/
		printf("In SD=%s, %x\n", name, name );
	}
	return 0;
}
