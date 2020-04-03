#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int n, ans = 0;
    cin >> n;
    while (n--){
        ans = 0;
        int a[3];
        cin >> a[0] >> a[1] >> a[2];
        sort(a, a+3);
        if (a[2] - a[1] <= a[0]){
            a[0] -= a[2] - a[1];
            ans += a[2] - a[1];
            a[2] = a[1];
            a[0] = int(a[0]/2);
            ans += a[0] * 2;
            a[2] -= a[0];
            a[1] -= a[0];
            ans += a[1];
        }
        else{
            a[2] -= a[0];
            ans += a[0];
            ans += a[1];
        }
        cout << ans << endl;
    }
    return 0;
}