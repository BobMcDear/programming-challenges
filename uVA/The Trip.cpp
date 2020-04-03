#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

// The amount that should be exchanged in order for everyone to pay an equal amount
double exchange_amount(double prices[], int num_students){
	// The average price that everyone pays
	double average = 0.00;

	for (int i = 0;i < num_students;i++){
		average += prices[i];
	}
	average /= num_students;

	// neg_dif is the amount that people who paid less should pay.pos_dif is the amount that people who paid more should receive
	double neg_dif = 0.00;
	double pos_dif = 0.00;


	for (int i = 0;i < num_students;i++){
		// If the person paid less, add the amount that he has to pay to neg_dif(Negative).Otherwise, add the amount that should be received to pos_dif
		if (prices[i] < average){
			// For reaching only 2 decimals
			neg_dif += (double) (long) ((prices[i] - average) * 100.0) / 100.0;
		}

		else{
			// For reaching only 2 decimals
			pos_dif += (double) (long) ((prices[i] - average) * 100.0) / 100.0;
		}
	}

	// If abs(neg_dif) is bigger, return abs(neg_dif).Otherwise, return pos_dif
	return (-neg_dif > pos_dif) ? -neg_dif : pos_dif;
}

int main(){
	// The output(Answer)
	vector<double> answer;

	int num_students;
	// As long as the number of students isn't 0, continue
	while (scanf("%d", &num_students) && num_students != 0){
		// Includes the amount each student paid
		double prices[num_students] = {0.00};

		double price;
		for (int i = 0;i < num_students;i++){
			// The prices
			cin >> price;

			prices[i] = price;
		}
		// The amount needed to be exchanged for the current students
		double exhange_curr;
		exhange_curr = exchange_amount(prices, num_students);

		answer.push_back(exhange_curr);
	}

	for ( auto i = answer.begin(); i != answer.end(); i++ ) {
    	// Print each exchange amount needed to be done
    	cout << fixed;
    	cout << setprecision(2);
    	cout << "$" << *i << endl;
	}

	return 0;
}