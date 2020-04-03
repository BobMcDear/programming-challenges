#include <iostream>
#include <string>
using namespace std;

bool is_interesting(string n){
    int s = 0;
    for (int i = 0;i < n.size();i++){
        s += n[i] - '0';
    }
    return (s % 4 == 0);

}
int main(){
    int a;
    cin >> a;
    for (int i = a;i <= 20000;i++){
        if (is_interesting(to_string(i))){
            cout << i << endl;
            break;
        }
    }
    return 0;
}