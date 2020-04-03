#include <bits/stdc++.h>
using namespace std;

string printer(vector<pair<int, char> > v) {
    string s = "";
    for(int i = 0; i<v.size(); i++) {
        s+=v[i].second;
    }
    return s;
}

bool compare(char a, char b){
    if (tolower(a) == tolower(b)){
        return (a < b);
    }
    return (tolower(a) < tolower(b));
}
int main(){
    int n;
    string s;
    cin >> n;
    while (n--){
        /*map<char, int> mp;
        cin >> s;
        vector<pair<int, char> > v;

        for(int i=0; i<s.size(); i++) {
            mp[s[i]] += 1;
        }

        int cnt = 0;

        for(int i = int('A'); i<=int('Z'); i++) {
            while(mp[char(i)]--) {
                v.push_back(make_pair(cnt*2, char(i)));
            }
            while(mp[i+int('a')-int('A')]--) {
                v.push_back(make_pair(cnt*2+1, char(i+int('a')-int('A'))));
            }
            cnt ++;
        }
        
        cout << printer(v) << endl;
        
        while (next_permutation(v.begin(), v.end())){
            cout << printer(v) << endl;
        }*/
        cin >> s;
        sort(s.begin(), s.end(), compare);
        cout << s << endl;
        while(next_permutation(s.begin(), s.end(), compare)){
			cout << s << endl;
        }
    }
    return 0;
}