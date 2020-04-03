#include <iostream>
using namespace std;



//The number of steps it takes to reach 1 using the collatz conjecture
long long collatzSteps(long long n){
	// The answer
	long long res = 0;

	// A copy of n
	long long copy_n = n;

	// Apply the 3n + 1 rule as long as n != 1
	while (n != 1){
		// If n is even, half it
		if (n % 2 == 0){
			n >>= 1;
			res += 1;
		}

		// If not, multiply it by 3 and add 1
		else{
			n = (n * 3 + 1) / 2;

			// We're doing 2 steps at once so add 2 to the number of cycles so far
			res += 2;
		}

	}

	// Add 1 to res because we didn't count the last step(When n is equal to 1)
	res += 1;

	// Add the new number to collatz
	//collatz[copy_n] = res;

	return res;
}


int main(){
	int i, j;

	// While you get an input:
	while ( scanf ("%d %d", &i, &j) != EOF ){
		long long ans = 1;

		// Copy of i and j before swaping
		int copy_i_before = i;
		int copy_j_before = j;

		// I assumed i <= j so swap the values of i and j if j < i
		if (j < i){
			swap(i, j);
		}

		// A copy of i after swaps
		int  copy_i = i;

		while (i <= j){
			// The number of cycles it takes to get to 1 from n using the collatz conjecture algorithm
			long long c = collatzSteps(i);

			if (c > ans){
				ans = c;
			}

			// Go to n + 1
			i += 1;

		}

		// Print out the result
		cout << copy_i_before << " " << copy_j_before << " " << ans << endl;

	}

	return 0;
}