#include <iostream>
using namespace std;

int main() {
    system("pwd");
    system("sshpass -p 'somepassword' ssh -Y username@192.168.1.xxx");
    //system("pwd");

    return 0;
}