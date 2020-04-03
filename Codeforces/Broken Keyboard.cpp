#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    int t, curr_length;
    string s;
    char prev_letter;
    cin >> t;
    while (t--){
        cin >> s;
        vector<char>res;
        map<char, int>added;
        prev_letter = s[0];
        curr_length = 0;
        for (int i=0; i<s.length(); i++){
            if (prev_letter == s[i]){
                curr_length++;
            }
            else
            {
                if (curr_length % 2 == 1 && added[prev_letter] == 0){
                    res.push_back(prev_letter);
                    added[prev_letter] = 1;
                }
                prev_letter = s[i];
                curr_length = 1;
            }
            
        }
        if (curr_length % 2 == 1 && added[prev_letter] == 0){
            res.push_back(prev_letter);
        }
        /*if (res.size() == 0){
            cout << 
        }*/
        sort(res.begin(), res.end());
        for (int i=0; i<res.size(); i++){
            cout << res[i];
        }
        cout << endl;
    }
    return 0;
}