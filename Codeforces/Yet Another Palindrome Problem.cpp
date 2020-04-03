#include <iostream>
#include <string>
using namespace std;

int main(){
    int t, n;
    bool f;
    cin >> t;
    while (t--){
        f = true;
        cin >> n;
        int a[n];
        for (int i=0; i<n; i++){
            cin >> a[i];
        }
        for (int i=0; i<=n-3; i++){
            for (int j=i+2; j<=n-1; j++){
                if (a[i] == a[j] && f){
                    cout << "YES"  << endl;
                    f = false;
                }
            }
        }
        if (f){
            cout << "NO" << endl;
        }
    }
    return 0;
}