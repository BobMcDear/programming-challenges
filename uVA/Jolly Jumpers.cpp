#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int absVal(int a){
	return (a < 0) ? -a : a;
}

int main(){
	int n;
	while (scanf("%d", &n) != EOF){
		int sequence[n];

		for (int i = 0;i < n; i++){
			cin >> sequence[i];
		}
		bool jolly = true;
		int differences[n - 1];

		for (int i = 1;i < n; i++){
			differences[i - 1] = absVal(sequence[i] - sequence[i - 1]);
		}

		sort(differences, differences + n - 1);

		for (int i = 0;i < n - 1;i++){
			if (differences[i] != i + 1){
				jolly = false;
			}
		}      

		if (jolly){
			cout << "Jolly" << endl;
		}
		else{
			cout << "Not jolly" << endl;
		}


	}
	return 0;
}