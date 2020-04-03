#include <iostream>
using namespace std;

int num_odds(int a[], int n){
    int r = 0;
    for (int i = 0; i<n; i++){
        if (a[i] % 2 != 0) r++;
    }
    return r;
}

int sum(int a[], int n){
    int r = 0;
    for (int i = 0; i<n; i++){
        r += a[i]&1;
    }
    return r;
}

int main(){
    int q, n, k, c;
    cin >> q;
    while (q--){
        cin >> n >> k;
        int a[n];
        for (int i = 0; i<n; i++){
            cin >> a[i];
        }
        if (num_odds(a, n) < k || sum(a, n) % 2 != k%2) cout << "NO" << endl;
        else{
            cout << "YES" << endl;
            c = 0;
            for (int i = 0; i<n; i++){
                if (c == k - 1){
                    cout << n << endl;
                    break;
                }
                if (a[i] % 2 != 0){
                    c++;
                    cout << i + 1;
                    if (c < k) cout << " ";
                }
            }
        }
    }
}