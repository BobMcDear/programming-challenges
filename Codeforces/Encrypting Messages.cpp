#include <iostream>
using namespace std;

int main(){
    int n, m, c;
    cin >> n >> m >> c;
    int a[n], b[m];
    for (int i = 0;i<n;i++){
        cin >> a[i];
    }
    for (int i = 0;i<m;i++){
        cin >> b[i];
    }   
    for (int i = 0;i<=n-m;i++){
        for (int j = i;j<=i+m-1;j++){
            a[j] += b[j - i];
        }
    }
    for (int i = 0;i<n;i++){
        cout << a[i] % c;
        if (i != n -1) cout << " ";
    }
    cout << endl;
    return 0;
}