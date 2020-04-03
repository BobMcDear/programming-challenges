#include <iostream>
#include <string>
#include <map>
using namespace std;

int main(){
    string s, t;
    getline(cin, s);
    getline(cin, t);
    map <char, int> mp;
    for (int i=0; i<t.length(); i++){
        mp[t[i]]++;
    }
    map <char, int> mp2;
    for (int i=0; i<s.length(); i++){
        mp2[s[i]]++;
    }
    for (const auto& [chr, num] : mp){
        if (mp2[chr] < num && chr != ' '){
            cout << "NO" << endl;
            return 0;
        }
    }
    cout << "YES" << endl;
    return 0;
}