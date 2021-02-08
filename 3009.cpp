#include <iostream>
using namespace std;
/*
	3009 네번째 점
	알고리즘 --> 좌표는 각각 쌍이 맞아야 한다. 
				따라서, 쌍이 없는 좌표가 네번째 점이 된다.
*/
int main() {
	int* x = new int[3];
	int* y = new int[3];
	int new_x, new_y;

	for (int i = 0; i < 3; i++) {
		cin >> x[i] >> y[i];
	}

	if (x[0] == x[1]) {
		new_x = x[2];
	}
	else if (x[0] == x[2]) {
		new_x = x[1];
	}
	else if (x[1] == x[2]) {
		new_x = x[0];
	}

	if (y[0] == y[1]) {
		new_y = y[2];
	}
	else if (y[0] == y[2]) {
		new_y = y[1];
	}
	else if (y[1] == y[2]) {
		new_y = y[0];
	}

	cout << new_x << ' ' << new_y;
}