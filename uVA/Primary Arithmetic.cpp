#include <iostream>
#include <string>
using namespace std;

int main(){
    int n, m, s, r;
    string a, b;
    while (true){
        cin >> n >> m;
        if (n == 0 && m == 0) break;
        r = 0;
        s = n + m;
        string a = to_string(n), b = to_string(m), c = to_string(s);
        if (a.size() >= b.size()){
            for (int i = 0;i < a.size();i++){
                if (a[i] > c[i]) r++;
            }
            if (a.size() < c.size()) r++;
        }
        else{
            for (int i = 0;i < b.size();i++){
                if (b[i] > c[i])cout<<b[i] << " " << c[i] << endl; r++;
            }
            if (b.size() < c.size()) r++;
        }
        if (r == 0) cout << "No carry operation." << endl;
        else cout << r << " carry operations." << endl;
    }
    return 0;
}