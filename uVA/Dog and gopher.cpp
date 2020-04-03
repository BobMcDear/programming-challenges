#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

double point_distance(double p1[], double p2[]){
	return (sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1])));
}

int main(){
	cout << fixed;
    cout << setprecision(3);
	int n;
	while (cin >> n){
		double g[2], d[2], holes[n][2];
		cin >> g[0];
		cin >> g[1];
		cin >> d[0];
		cin >> d[1];
		for (int i = 0; i < n; i++){
			double hole[2];
			cin >> hole[0];
			cin >> hole[1];
			holes[i][0] = hole[0];
			holes[i][1] = hole[1];
		}
		bool flag;
		flag = false;
		for (int i = 0; i < n; i++){
			double dd = point_distance(d, holes[i]);
			double gd = point_distance(g, holes[i]);
			if (gd <= (dd / 2)){
				cout << "The gopher can escape through the hole at (" << holes[i][0] << "," << holes[i][1] << ")." << endl;
				flag = true;
				break;
			}
		}
		if (!flag){
			cout << "The gopher cannot escape." << endl;
		}
	}

}