#include <iostream>
#include <cmath>
#include <vector>
#include <iomanip>
#include <algorithm>
using namespace std;
long double quadratic_solver(long double a, long double b, long double c){
	long double sq, x1, x2;
	sq = sqrt(b * b - 4 * a * c);
	x1 = (-b + sq) / (2 * a);
	x2 = (-b - sq) / (2 * a);
	return (x2 > 0) ? x2 : x1;
}
int main(){
	cout << setprecision(3) << fixed;
	vector<long double> mini;
	vector<long double> maxi;
	long double l, w;
	long double least_vol,max_vol;
	while (cin >> l >> w){
		max_vol = quadratic_solver(12, -4 * w - 4 * l, l * w);
		least_vol = min(l, w) / 2;
		mini.push_back(least_vol);
		maxi.push_back(max_vol);
	}
	for (int i = 0;i<mini.size();++i){
		cout << maxi[i] << " 0.000 " << mini[i] << endl;
	}
	return 0;
}