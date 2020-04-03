#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){
    int n;
    cin >> n;
    while (n--){
        string s, t;
        cin >> s >> t;
        vector<char>s_keys;
        vector<char>t_keys;
        vector<int>s_values;
        vector<int>t_values;
        int i, j, same, s_len, t_len;
        s_len = s.length();
        t_len = t.length();
        i = 0;
        while (i < s_len){
            //cout << i << "KOS" << endl;
            same = 0;
            j = i;
            while (s[i] == s[j]){
                same++;
                j++;
                if (j == s_len){
                    break;
                }
            }
            s_keys.push_back(s[i]);
            s_values.push_back(same);
            i = j;
            if (i >= s_len){
                break;
            } 
        }
        i = 0;
        while (i < t_len){
            //cout << i << "KOON" << endl;
            same = 0;
            j = i;
            while (t[i] == t[j]){
                same++;
                j++;
                if (j == t_len){
                    break;
                }
            }
            t_keys.push_back(t[i]);
            t_values.push_back(same);
            i = j;
            if (i >= t_len){
                break;
            }
        }
        if (s_keys.size() != t_keys.size()){
            cout << "NO" << endl;
            continue;
        }
        bool f = true;
        for (int i = 0; i<s_keys.size(); i++){
            if (s_keys[i] != t_keys[i] || s_values[i] > t_values[i]){
                cout << "NO" << endl;
                f = false;
                break;
            }
        }
        if (f){
            cout << "YES" << endl;
        }


    }
    return 0;
}