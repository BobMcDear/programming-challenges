#include <iostream>
#include <string>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    string s, res="";
    cin >> s;
    bool f = true;
    for (int i=0; i<s.length(); i++){
        if (s[i] == 'a'){
            res += s[i];
            continue;
        }
        if (f == false){
            res += s[i];
        }
        while (true && f && i < s.length()){
            if (s[i] == 'a'){
                res += 'a';
                f = false;
                break;
            }
            res += s[i] - 1;
            i++;
        }

    }
    if (res == s){
        if (s.length() == 1){
            res = 'z';
        }
        else{
            res = "";
            for (int i=0; i<=s.length()-2; i++){
                res += s[i];
            }
            res += 'z';
        }
    }
    cout << res << endl;
    return 0;
}