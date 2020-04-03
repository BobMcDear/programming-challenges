#include <iostream>
using namespace std;

int main(){
    int n, f, s, a, g, r;
    cin >> n;
    while (n--){
        cin >> f;
        r = 0;
        while (f--){
            cin >> s >> a >> g;
            r += s * g;
        }
        cout << r << endl;
    }
    return 0;
}