#include <iostream>
using namespace std;
 
int main(){
    int n, r = 0;
    cin >> n;
    for (int i = 0; i<=n-1; i++){
        r += (i + 1) * (n - i) - i;
    }
    cout << r << endl;
    return 0;
}