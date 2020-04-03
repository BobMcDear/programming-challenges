#include <string>
#include <iostream>
using namespace std;

bool is_pal(string s){
    string rev = "";
    for (int i=s.length()-1; i>=0; i--){
        rev += s[i];
    }
    return (rev == s);
}

string ind(string s, int a, int b){
    string res = "";
    for (int i=a-1; i<b; i++){
        res += s[i];
    }
    return res;
}

int main(){
    string s;
    int k;
    cin >> s >> k;
    if (s.length() % k != 0){
        cout << "NO" << endl;
        return 0;
    }
    int chert = k;
    int i=1;
    while (chert--){
        string curr = ind(s, i, i + (s.length()/k) - 1);
        if (!is_pal(curr)){
            cout << "NO" << endl;
            return 0;
        }
        i += (s.length()/k);
    }
    cout << "YES" << endl;
    return 0;
}