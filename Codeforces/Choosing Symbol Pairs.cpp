#include <string>
#include <iostream>
#include <map>
using namespace std;

long long chert(long long n){
    return n * (n-1);
}

int main(){
    string s;
    cin >> s;
    map <char, long long> mp;
    for (int i=0; i<s.length(); i++){
        mp[s[i]]++;
    }
    long long r=0;
    for (const auto& [k1, v1] : mp){
        r += chert(v1) + v1;
    }
    cout << r << endl;

}