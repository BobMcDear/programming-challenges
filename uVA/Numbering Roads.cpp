#include <iostream>
#include <vector>
using namespace std;
int main(){
    int r, n, q, c = 1;
    while (true){
        cin >> r >> n;
        if (r == 0 && n == 0) break;
        for(int i = r; i <= 30000; i++){
            if (i % n == 0){
                q = (i / n) - 1;
                break;
            }
        }
        if (q > 26) cout << "Case " << c << ": " << "impossible" << endl;
        else cout << "Case " << c << ": " << q << endl;
        c++;
    }
    return 0;
}