#include <iostream>
using namespace std;

#define ll (long long)

int main(){
    long long n, k, num_even, num_odd;
    cin >> n >> k;
    if (n % 2 == 0){
        num_even = ll(n/2);
        num_odd = ll(n/2);
    }
    else{
        num_even = ll(n/2) - 1;
        num_odd = ll(n/2) + 1;
    }
    if (k <= num_odd){
        cout << 2 * k - 1 << endl;
    }
    else{
        k -= num_odd;
        cout << 2 * k << endl;
    }
    return 0;
}