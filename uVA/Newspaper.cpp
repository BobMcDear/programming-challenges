#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout << setprecision(2) << fixed;
    int n, k, m, v;
    double r;
    char c;
    string s;
    cin >> n;
    while (n--){
        r = 0;
        cin >> k;
        map<char, int> mp;
        while (k--){
            cin >> c >> v;
            mp[c] = v;           
        }
        cin >> m;
        getline(cin, s);
        while (m--){
            getline(cin, s);
            for (int i = 0; i < s.size(); i++){
                r += mp[s[i]];
            }
        }
        cout << r / 100 << "$" << endl;
    }
    return 0;
}