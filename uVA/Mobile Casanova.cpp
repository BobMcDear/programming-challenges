#include <iostream>
#include <string>
#include<utility>
using namespace std;

int main(){
    int n, p, prev_p, c = 1;
    while (true){
        cin >> n;
        if (n == 0) break;
        cout << "Case " << c << ":" << endl;
        c++;
        pair<int, int>curr_seq;
        cin >> prev_p;
        curr_seq = make_pair(prev_p, 0); 
        n--;
        for(int i = 0; i<n; i++){
            cin >> p;
            //See if the consecutiveness still holds
            if (p - prev_p == 1){
                curr_seq.second++;
            }
            //If it's broken
            else{
                //If there's only one number, print it
                if (curr_seq.second == 0){
                    cout << "0" << curr_seq.first << endl;
                    curr_seq = make_pair(p, 0);
                    prev_p = p;

                    continue;
                }
                string a = to_string(curr_seq.first), b = to_string(curr_seq.first + curr_seq.second);
                if (a.size() < b.size()){
                    cout << "0" << a << "-" << b << endl;
                    curr_seq = make_pair(p, 0);
                    prev_p = p;

                    continue;
                }
                bool f = true;
                cout << "0" << a << "-";
                for (int i = 0;i<a.size();i++){
                    if (a[i] == b[i] && f) continue;
                    cout << b[i]; 
                    f = false;
                }
                cout << endl;
                curr_seq = make_pair(p, 0);

            }
            prev_p = p;
        }
        //fekvjelrgk
        //If there's only one number, print it
        if (curr_seq.second == 0){
            cout << "0" << curr_seq.first << endl;
            curr_seq = make_pair(p, 0);
            cout << endl;
            continue;
        }
        string a = to_string(curr_seq.first), b = to_string(curr_seq.first + curr_seq.second);
        if (a.size() != b.size()){
            cout << "0" << a << "-" << b << endl;
            curr_seq = make_pair(p, 0);
            cout << endl;
            continue;
        }
        cout << "0" << a << "-";
        bool f = true;
        for (int i = 0;i<a.size();i++){
            if (a[i] == b[i] && f) continue;
            cout << b[i]; 
            f = false;
        }
        cout << endl;
        curr_seq = make_pair(p, 0);
        cout << "\n";
    }

    return 0;
}