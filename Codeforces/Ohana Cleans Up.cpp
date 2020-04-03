#include <iostream>
#include <string>
#include <map>
using namespace std;

int main(){
    int n;
    cin >> n;
    map <string, int> occ;
    string curr;
    for (int i=0; i<n; i++){
        cin >> curr;
        occ[curr] += 1;
    }
    int mx = -1;
    for (auto const& [key, val] : occ){
        if (val > mx){
            mx = val;
        }
    }
    cout << mx << endl;
    return 0;
}