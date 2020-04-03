#include <iostream>
#include <cmath>
#include <iomanip>
#include <vector>
using namespace std;

long double mycos(long double x, long double y, long double z){
	return -((z * z - y * y - x * x) / (2 * x * y));
}
int main(){
	vector<long double> v;
	long double x,y,z,r;
	cout << setprecision(3) << fixed;
	while (cin >> x >> y >> z){
		if (x * y * z == 0){
			v.push_back(0);
			continue;
		}
		r = x* sqrt(y*y  - pow((mycos(x,y,z) * y),2) ) /(x+y+z);
		v.push_back(r);
	}
	for (int i = 0;i<v.size();i++){
		cout << "The radius of the round table is: " << v[i] << endl;
	}
	return 0;
}