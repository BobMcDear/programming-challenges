#include <iostream>
#include <cstdlib>
using namespace std;

int min_val(int a[]){
    int mn = 999999999;
    for (int i = 0;i < sizeof(a)/sizeof(a[0]);i++){
        if (a[i] < mn) mn = a[i];
    }
    return (mn);
}

int max_val(int a[]){
    int mx = 0;
    for (int i = 0;i < sizeof(a)/sizeof(a[0]);i++){
        if (a[i] > mx) mx = a[i];
    }
    return (mx);
}

int main(){
    int q, n, k, mn, mx, b;
    cin >> q;
    while (q--){
        cin >> n >> k;
        int a[n];
        for (int i = 0;i<n;i++){
            cin >> a[i];
        }
        mn = min_val(a);
        mx = max_val(a);
        b = mn + k;
        if (abs(mx - b) > k) cout << "-1" << endl;
        else cout << b << endl;
    }
    return 0;
}