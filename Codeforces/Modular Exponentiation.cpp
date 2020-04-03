#include <iostream>
using namespace std;

int pow(int a, int b){
    int t = 1;
    while (b--){
        t *= a;
    }
    return t;
}

int main(){
    int n, m;
    cin >> n >> m;
    if (n <= 30) cout << m % pow(2, n) << endl;
    else cout << m << endl;
    return 0;
}