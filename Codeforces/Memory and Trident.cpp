#include <iostream>
#include <algorithm>
//#include <cmath>
#include <string>
using namespace std;

int count(string s, char c){
    int r = 0;
    for (int i=0; i<s.length(); i++){
        r += (c == s[i]);
    }
    return r;
}

int main(){
    string s;
    cin >> s;
    if (s.length() % 2 == 1){
        cout << "-1" << endl;
        return 0;
    }
    int needed[4] = {count(s, 'U'), count(s, 'R'), count(s, 'D'), count(s, 'L')};
    char chrs[4] = {'U', 'R', 'D', 'L'};
    int temp = needed[0];
    needed[0] -= min(needed[0], needed[2]);
    needed[2] -= min(temp, needed[2]);
    temp = needed[1];
    needed[1] -= min(needed[1], needed[3]);
    needed[3] -= min(temp, needed[3]);
    int r = 0;
    if (needed[0] > needed[2]){
        if (needed[1] > needed[3]){
            temp = needed[0];
            r += min(temp, needed[1]);
            needed[0] -= min(needed[0], needed[1]);
            needed[1] -= min(temp, needed[1]);
            temp = needed[2];
            r += min(temp, needed[3]);
            needed[2] -= min(temp, needed[3]);
            needed[3] -= min(temp, needed[3]);
        }
        else{
            temp = needed[0];
            r += min(temp, needed[3]);
            needed[0] -= min(needed[0], needed[3]);
            needed[3] -= min(temp, needed[3]);
            temp = needed[2];
            r += min(temp, needed[1]);
            needed[2] -= min(temp, needed[1]);
            needed[1] -= min(temp, needed[1]);
        }
    }
    else{
        if (needed[1] > needed[3]){
            temp = needed[2];
            r += min(temp, needed[1]);
            needed[2] -= min(needed[2], needed[1]);
            needed[1] -= min(temp, needed[1]);
            temp = needed[0];
            r += min(temp, needed[3]);
            needed[0] -= min(temp, needed[3]);
            needed[3] -= min(temp, needed[3]);
        }
        else{
            temp = needed[2];
            r += min(temp, needed[3]);
            needed[2] -= min(needed[2], needed[3]);
            needed[3] -= min(temp, needed[3]);
            temp = needed[0];
            r += min(temp, needed[1]);
            needed[0] -= min(temp, needed[1]);
            needed[1] -= min(temp, needed[1]);
        }
    } 
    for (int i=0; i<4; i++){
        if (needed[i] == 0){
            continue;
        }
        r += int(needed[i]/2);
    }
    cout << r << endl;
    return 0;
}