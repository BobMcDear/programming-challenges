#include <iostream>
#include <string>
#include <ctype.h>
using namespace std;

int main(){
    int t;
    string s;
    cin >> t;
    while (t--){
        cin >> s;
        int u=0, l=0, d=0;
        for (int i=0; i<s.length(); i++){
            if (isupper(s[i])){
                u++;
            }
            else if (islower(s[i])){
                l++;
            }
            else{
                d++;
            }
        }
        if (u*l*d != 0){
            cout << s << endl;
        }
        else{
            string new_s="";
            bool f;
            if (u == 0){
                f = true;
                if (l > d){
                    for (int i=0; i<s.length(); i++){
                        if (islower(s[i]) && f){
                            new_s += 'A';
                            f = false;
                            l--;
                            continue;
                        }
                        new_s += s[i];
                    }
                }
                else{
                    for (int i=0; i<s.length(); i++){
                        if (isdigit(s[i]) && f){
                            new_s += 'A';
                            f = false;
                            d--;
                            continue;
                        }
                        new_s += s[i];
                    }
                }

                u = 1;
                s = new_s;
                new_s = "";
            }
            if (l == 0){
                f = true;
                if (u > d){
                    for (int i=0; i<s.length(); i++){
                        if (isupper(s[i]) && f){
                            new_s += 'a';
                            f = false;
                            u--;
                            continue;
                        }
                        new_s += s[i];
                    }
                }
                else{
                    for (int i=0; i<s.length(); i++){
                        if (isdigit(s[i]) && f){
                            new_s += 'a';
                            f = false;
                            d--;
                            continue;
                        }
                        new_s += s[i];
                    }
                }
                l = 1;
                s = new_s;
                new_s = "";
            }
            if (d == 0){
                f = true;
                if (u > l){
                    for (int i=0; i<s.length(); i++){
                        if (isupper(s[i]) && f){
                            new_s += '1';
                            f = false;
                            u--;
                            continue;
                        }
                        new_s += s[i];
                    }
                }
                else{
                    for (int i=0; i<s.length(); i++){
                        if (islower(s[i]) && f){
                            new_s += '1';
                            f = false;
                            l--;
                            continue;
                        }
                        new_s += s[i];
                    }
                }
                l = 1;
                s = new_s;
            }
            cout << s << endl;
        }
    }
    return 0;
}