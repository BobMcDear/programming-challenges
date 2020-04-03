#include <iostream>
#include <algorithm>
using namespace std;

bool intervals_dont_share_num(int l1, int h1, int l2, int h2){
    return (h1 < l2) || (h2 < l1);
}

void interval(int (&l1)[1], int (&h1)[1], int l2[1], int h2[1]){
    int l_tmp, h_tmp;
    l_tmp = max(l1[0], l2[0]);
    h_tmp = min(h1[0], h2[0]);
    l1[0] = l_tmp;
    h1[0] = h_tmp;
}

int main(){
    int q, n, m, t, l[1], h[1], prev_time = 0, l1[1], h1[1], dif_time;
    cin >> q;
    bool f;
    while (q--){
        f = true;
        cin >> n >> m;
        l1[0] = m;
        h1[0] = m;
        prev_time = 0;
        while (n--){
            cin >> t >> l[0] >> h[0];
            if (!f){
                continue;
            }
            dif_time = t - prev_time;
            prev_time = t;
            l1[0] -= dif_time;
            h1[0] += dif_time;
            //cout << l1[0] << ' ' << h1[0] << endl;
            if (intervals_dont_share_num(l1[0], h1[0], l[0], h[0])){
                cout << "NO" << endl;
                f = false;
            }
            interval(l1, h1, l, h);
        }
        if (f){
            cout << "YES" << endl;
        }
    }
    return 0;
}