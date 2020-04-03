#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

bool is_pal(string s){
    string s_copy = s;
    reverse(s.begin(), s.end());
    return (s_copy == s);
}

string add(string s, char c, int i){
    string r = "";
    if (i == s.length() - 1){
        r = s;
        r += c;
    }
    else if (i == -1){
        r += c;
        r += s;
    }
    else{
        for (int j=0; j<s.length(); j++){
            r += s[j];
            if (i == j){
                r += c;
            }
        }
    }
    return r;
}

int main(){
    string s, t;
    cin >> s;
    for (int j=int('a'); j<=int('z'); j++){
        t = add(s, char(j), -1);
        if (is_pal(t)){
            cout << t << endl;
            return 0;
        }
    }
    for (int i=0; i<s.length(); i++){
        for (int j=int('a'); j<=int('z'); j++){
            t = add(s, char(j), i);
            if (is_pal(t)){
                cout << t << endl;
                return 0;
            }
        }
    }
    cout << "NA" << endl;
    return 0;
}