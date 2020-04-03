#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

int main(){
    bool f;
    int t, a, b, c, die_roll, tail, head;
    cin >> t;
    while (t--){
        f = false;
        cin >> a >> b >> c;
        int players[a];
        fill_n(players, a, 1);
        //cout << 13123123 << " " << players[2] << endl;
        map<int, int> snakes;
        while(b--){
            cin >> head >> tail;
            snakes[head] = tail;
        }
        for(int i = 0;i < c;i++){
            cin >> die_roll;
            if (f) continue;
            players[(i % a)] += die_roll;
            if (snakes.count(players[(i % a)])){
                players[(i % a)] = snakes[players[(i % a)]];
            }
            if (players[(i % a)] >= 100){ 
                players[(i % a)] = 100;
                f = true;
            }
        }
        for (int i = 0; i < a;i++){
            cout << "Position of player " << i + 1 <<  " is " << players[i] << "." << endl;
        }        

    }
}