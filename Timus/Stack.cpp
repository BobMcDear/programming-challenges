#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
	vector<int> stacks[1001];

	// The number of actions
	int n;
	cin >> n;

	for (int i = 0;i < n;++i){
		string action;
		cin >> action;

		if (action == "PUSH"){
			int stack_num, new_item;
			cin >> stack_num;
			cin >> new_item;

			stacks[stack_num].push_back(new_item);
		}
		else{
			int pop_stack_num, pop_item;
			cin >> pop_stack_num;

			pop_item = stacks[pop_stack_num].back();
			stacks[pop_stack_num].pop_back();

			cout << pop_item << endl;

		}


	}

}