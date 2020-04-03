#include <iostream>
#include <string>
using namespace std;

char next_letter(char c){
    int ascii = int(c);
    if (ascii == 122){
        return 'a';
    }
    return char(ascii + 1);
}

int main(){
    string s;
    cin >> s;
    string res = "";
    int n = s.length();
    char to_add = s[0];
    if (n == 1){
        cout << s << endl;
        return 0;
    }
    else if (n == 2){
        if (s[0] == s[1]){
            cout << s[0] << next_letter(s[1]) << endl;
        }
        else{
            cout << s << endl;
        }
        return 0;
    }
    for (int i=0; i<=n-3; i++){
        res += to_add;
        if (res[i]   == s[i+1]){
            to_add = next_letter(s[i+1]);
            if (to_add == s[i+2]){
                to_add = next_letter(to_add);
            }
        }
        else{
            to_add = s[i+1];
        }
    }
    res += to_add;
    if (res[n-2] != s[n-1]){
        to_add = s[n-1];
    }
    else{
        to_add = next_letter(s[n-1]);
    }
    res += to_add;
    cout << res << endl;
    return 0;
}