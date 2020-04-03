#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int a1, a2, t = 0, time_needed;
    cin >> a1 >> a2;
    while (true){
        if (a1 > a2) swap(a1, a2);
        if (a1 == 0 || a1 * a2 == 1) break;
        a1 += 1;
        a2 -= 2;
        t += 1;
    }
    cout << t << endl;
    return 0;
}