#include <cstdio>
#include <iostream>
using namespace std;

int solve(int n, int k, int r){
    if (n == 0) return int(r / k);
    return n + solve(int(n / k) + int(r / k), k, (r % k) + (n % k));
}

int main(){
    int n, k, sum, remain;
    while (scanf("%d%d", &n, &k) == 2){
       cout << solve(n, k, 0) << endl;
    }
    return 0;
}