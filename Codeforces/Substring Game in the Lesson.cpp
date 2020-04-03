#include <string>
#include <iostream>
using namespace std;

int main(){
    string s;
    cin >> s;
    char best_before=s[0];
    for (int i=0; i<s.length(); i++){
        if (i==0){
            cout << "Mike" << endl;
        }
        else{
            if (best_before >= s[i]){
                cout << "Mike" << endl;
                best_before = s[i];
            }
            else{
                cout << "Ann" << endl;
            }
        }

    }
    return 0;
}