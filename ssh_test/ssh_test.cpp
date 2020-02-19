#include <iostream>
using namespace std;

//This program tests out the ssh system call. It should be compiled and ran from the Ubuntu terminal on your Windos machine

// compile with $ g++ ssh_test.cpp -o runthisc
// run with $ ./runthisc

int main() {
    system("pwd");
    system("sshpass -p 'somepassword' ssh -Y username@192.168.1.xxx"); //use this line if you have installed sshpass
    //system("ssh -Y username@192.168.1.xxx"); //use this line if you have disabled the password for the server

    return 0;
}
