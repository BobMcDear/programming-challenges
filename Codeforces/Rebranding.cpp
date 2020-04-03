#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

int main(){
    int n, m;
    string s, next_str="";
    char alph[26];
    char x, y;
    cin >> n >> m;
    cin >> s;
    for (int i=0; i<=25; i++){
        alph[i] = i + 'a';
    }
    while (m--){
        cin >> x >> y;
        for (int i=0; i<=25; i++){
            if (alph[i] == x){
                alph[i] = y;
            }
            else if (alph[i] == y){
                alph[i] = x;
            }
        }
    }
    for (int i=0; i<n; i++){
        next_str += alph[s[i]-'a'];
    }
    cout << next_str << endl;
    return 0;
}