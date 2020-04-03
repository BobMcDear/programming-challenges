#include <iostream>
#include <string>
using namespace std;

string remove_chr(string s, int rm){
    string ans = "";
    for (int i = 0; i<s.length(); i++){
        if (i == rm){
            continue;
        }
        ans += s[i];
    }
    return ans;
}

int main(){
    int n, rm;
    string s;
    cin >> n >> s;
    rm = n - 1;
    for (int i = 0; i < n-1; i++){
        if (s[i] > s[i+1]){
            rm = i;
            break;
        }
    }
    cout << remove_chr(s, rm) << endl;
    return 0;
}