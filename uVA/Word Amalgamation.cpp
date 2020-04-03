#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    int c = 0, k = 0;
    string s;
    vector<string>dic;
    while (c < 2){
        cin >> s;
        if (s == "XXXXXX"){
            c++;
            continue;
        }
        if (c == 0) dic.push_back(s);
        if (c == 1){
            sort(s.begin(), s.end());
            if(find(dic.begin(), dic.end(), s) != dic.end()) {
                cout << s << endl;
                k++;
            }
            while (next_permutation(s.begin(), s.end())){
                if(find(dic.begin(), dic.end(), s) != dic.end()) {
                    cout << s << endl;
                    k++;
                }
            }
            if (k == 0) cout << "NOT A VALID WORD" << endl;
            cout << "******" << endl;
            k = 0;
        }
    }
}