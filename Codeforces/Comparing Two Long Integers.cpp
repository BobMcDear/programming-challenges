#include <iostream>
#include <string>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    string a, b, new_a = "", new_b = "";
    bool fa = true, fb = true;
    cin >> a >> b;
    for (int i=0; i<a.length(); i++){
        if (a[i] == '0' && fa){
            continue;
        }
        fa = false;
        new_a += a[i];
    }
    for (int i=0; i<b.length(); i++){
        if (b[i] == '0' && fb){
            continue;
        }
        fb = false;
        new_b += b[i];
    }
    if (new_a.length() < new_b.length()){
        cout << '<' << endl;
    }
    else if (new_a.length() > new_b.length()){
        cout << '>' << endl;
    }
    else{
        bool f = true;
        for (int i=0; i<new_a.length(); i++){
            if (new_a[i] < new_b[i]){
                cout << '<' << endl;
                f = false;
                break;
            }
            if (new_a[i] > new_b[i]){
                cout << '>' << endl;
                f = false;
                break;
            }
        }
        if (f){
            cout << '=' << endl;
        }
    }
    return 0;
}