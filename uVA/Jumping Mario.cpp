#include <iostream>
using namespace std;

int main(){
    int t, n, h, w, highs = 0, lows = 0, c = 1;
    cin >> t;
    while (t--){
        cin >> n;
        cin >> h;
        n--;
        while (n--){
            cin >> w;
            if (w > h) highs++;
            if (h > w) lows++;
            h = w;
        }
        cout  << "Case " << c << ": " << highs << ' ' << lows << endl;
        highs = 0;
        lows = 0;
        c++;
    }

    return 0;
}