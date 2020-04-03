#include <iostream>
#include <string>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    string s;
    int m, l, r, n, add;
    cin >> s;
    n = s.length();
    int same_l[n] = {0}, same_r[n] = {0};
    for (int i=1; i<n; i++){
        add = 0;
        if (s[i-1] == s[i]){
            add = 1;
        }
        same_l[i] = same_l[i-1] + add;
        //cout << "l: " << i << ' ' << same_l[i] << endl;
    }
    for (int i=n-2; i>=0; i--){
        add = 0;
        if (s[i] == s[i+1]){
            add = 1;
        }
        same_r[i] = same_r[i+1] + add;
        //cout << "r: " << i << ' ' << same_r[i] << endl;
    }
    //cout << same_r[0] << ' ' << same_l[2] << ' ' << same_r[3] << endl;
    cin >> m;
    while (m--){
        cin >> l >> r;
        cout << same_r[0] - same_l[l-1] - same_r[r-1] << endl;
    }
    return 0;
}