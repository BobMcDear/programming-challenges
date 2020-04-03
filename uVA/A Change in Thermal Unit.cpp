#include <iostream>
#include <iomanip>
using namespace std;
double f_c(int f){
    double ans = (f - 32) * 5 / 9;
    return (ans);
}
double c_f(int c){
    double ans = 9 / 5 * c + 32;
    return (ans);
}
int main(){
    int t, c, d;
    cout << setprecision(2) << fixed;
    cin >> t;
    while (t--){
        cin >> c >> d;
        cout << f_c(c_f(c) + d) << endl;
    }
    return 0;
}