#include <iostream>
#include <algorithm>
using namespace std;

const int INF = 100000;

int main(){
    int q, n, x, y, d, r ,u, l;
    cin >> q;
    while (q--){
        cin >> n;
        pair<int, int>x_range;
        pair<int, int>y_range;
        x_range.first = -INF;
        x_range.second = INF;
        y_range.first = -INF;
        y_range.second = INF;
        while (n--){
            cin >> x >> y >> l >> u >> r >> d;
            if(!d) y_range.first = max(y_range.first, y);
            if(!u) y_range.second = min(y_range.second, y);
            if(!l) x_range.first = max(x_range.first, x);
            if(!r) x_range.second = min(x_range.second, x);
        }
        if(x_range.first > x_range.second || y_range.first > y_range.second) cout << 0 << endl;
        else{
            cout << 1 << " " << x_range.first << " " << y_range.first << endl;
        }
    }    
}