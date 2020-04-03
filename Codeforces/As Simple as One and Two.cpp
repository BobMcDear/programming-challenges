#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){
    int t;
    string s, curr_sub;
    cin >> t;
    while (t--){
        cin >> s;
        vector<int> to_remove;
        if (s.length() <= 2){
            cout << 0 << endl << endl;
            continue;
        }
        /*if (s[0] == 't' && s[1] == 'w' && s[2] == 'o'){
            if (s[3] == 'n' && s[4] == 'e'){
                to_remove.push_back(2);
            }
            else{
                to_remove.push_back(0);
            }
        }
        else if (s[0] == 'o' && s[1] == 'n' && s[2] == 'e'){
            to_remove.push_back(0);
        }*/
        for (int i=0; i<=s.length()-3; i++){
            curr_sub = "";
            curr_sub += s[i];
            curr_sub += s[i+1];
            curr_sub += s[i+2];
            if (curr_sub == "two"){
                if (s[i+3] == 'n' && s[i+4] == 'e'){
                    to_remove.push_back(i+2);
                }
                else{
                    to_remove.push_back(i+1);
                }
            }
            else if (curr_sub == "one" && (s[i-1] != 'w' || s[i-2] != 't')){
                to_remove.push_back(i+1);
            }
        }
        cout << to_remove.size() << endl;
        for (int i=0; i<to_remove.size(); i++){
            cout <<  to_remove[i] + 1;
            if (i < to_remove.size()-1){
                cout << ' ';
            }
        }
        cout << endl;
    }
}