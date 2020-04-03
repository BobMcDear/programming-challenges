#include <iostream>
#include <cmath>
using namespace std;

typedef struct{
double a;
double b;
double c;
} line;

typedef struct{
	double x;
	double y;
} point;

//Get two points and find the line equation for them
void points_to_line(point p1, point p2, line *l){
	if (p1.x == p2.x){
		l -> a = 1;
		l -> b = 0;
		l -> c = -p1.x;
	}
	else{
		l -> b = 1;
		l -> a = (p1.y - p2.y) / (p1.x - p2.x);
		l -> c = -(l -> a * p1.x) - (l -> b * p1.y);
	}
}

//Distance between two points
double distance_points(point p1, point p2){
	return sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y)); 
}

//Distance between a line and a point
double distance_line_point(line l, point p){
	return abs(l.a * p.x + l.b * p.y + l.c) / sqrt(l.a * l.a + l.b * l.b);
}

//Says whether a line is crosses a circle or not
bool crosses_circle(line l, double r){
	point origin;
	origin.x = 0;
	origin.y = 0;
	if (distance_line_point(l, origin) < r){
		return true;
	}
	return false;
}

int main(){
	int n;
	double r;
	cin >> n;
	while (n != 0){
		line l;
		n--;
		point p1, p2;
		cin >> p1.x;
		cin >> p1.y;
		cin >> p2.x;
		cin >> p2.y;
		cin >> r;
		points_to_line(p1, p2, *l)
		if (crosses_circle(l, r)){
				
		}

	}

	return 0;
}