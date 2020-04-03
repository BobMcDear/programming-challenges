#include <iostream>
#include <string>
using namespace std;

int move_on(string s, int *l, int index, char action, int curr_value){
    int curr_indx = index;
    if(action == '>'){
        while(s[index+1] == '<') {
            index ++;
        }
        for(int i = index; i>=curr_indx; i--, curr_value--) {
            l[i] = curr_value;
        }
        return curr_value;
    }
    else
    {
        return curr_value;
    }
}

int main(){
    ios::sync_with_stdio(false);
    int t, n;
    string st;
    cin >> t;
    while (t--){
        cin >> n >> st;
        int c=1, s[n+10] = {0}, l[n+10] = {0};
        for (int i=n-2; i>=0; i--){
            if (st[i] == '>'){
                s[i+1] = c;
                c++;
            }
        }
        int mx = n;
        mx = move_on(st, s, 0, '>', mx)

        for (int i=1; i<=n-2; i++){
            if (st[i] == '<'){
                
            }
        }
    }
    return 0;
}