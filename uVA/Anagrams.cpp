#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

string initiate(string s){
    s.erase(remove(s.begin(), s.end(), ' '), s.end());
    sort(s.begin(), s.end());
    return s;
}

int main(){
    int n;
    string s;
    cin >> n;
    cin.ignore();
    cin.ignore();
    while (n--){
        vector<string> words;
        while (getline(cin, s) && s != "")
            words.push_back(s);
        sort(words.begin(), words.end());
        for (int i = 0;i<words.size() - 1;i++){
            for (int j = i + 1;j<words.size();j++){
                if (initiate(words[i]) == initiate(words[j])){
                    cout << words[i] << " = " << words[j] << endl;
                }
            }
        }
        if (n) cout << endl;
    }
    return 0;
}