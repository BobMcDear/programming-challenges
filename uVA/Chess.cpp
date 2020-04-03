#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int n, r, c;
    char p;
    cin >> n;
    while(n--){
        cin >> p >> r >> c;
        if (p == 'r' || p == 'Q') cout << min(r, c) << endl;
        if (p == 'k') cout << int(((r * c) + 1) / 2) << endl;
        if (p == 'K') cout << int(((r + 1) / 2) * ((c + 1) / 2)) << endl;
    }
    return 0;
}