#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

bool comperator(char a, char b){
    if (tolower(a) == tolower(b)) return (a < b);
    return tolower(a) < tolower(b);
}
int main(){
    int n;
    string s;
    cin >> n;
    while (n--){
        cin >> s;
        sort(s.begin(), s.end(), comperator);
        cout << s << endl;
        while (next_permutation(s.begin(), s.end(), comperator)){
            cout << s << endl;
        }
        cout << endl;
    }
    return 0;
}