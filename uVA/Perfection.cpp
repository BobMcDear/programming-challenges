#include <iostream>
#include <cstdio>
using namespace std;

int main(){
    int n, sm;
    cout << "PERFECTION OUTPUT" << endl;
    while (cin >> n){
        if (n == 0) break;
        sm = 0;
        for (int i = 1; i < n;i++){
            if (n % i == 0) sm += i;
        }
        printf("%5d  ", n);
        if (sm == n) cout << "PERFECT" << endl;
        if (sm < n) cout << "DEFICIENT" << endl;
        if (sm > n) cout << "ABUNDANT" << endl;
    }
    cout << "END OF OUTPUT" << endl;
    return 0;
}