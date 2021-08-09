#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	while (1) {
		int a, b, c;
		cin >> a >> b >> c;

		vector<int> tri;
		tri.push_back(a);
		tri.push_back(b);
		tri.push_back(c);
		sort(tri.begin(), tri.end());

		if (a == 0 && b == 0 && c == 0) {
			break;
		}

		int x, y, z;
		x = pow(tri[0], 2);
		y = pow(tri[1], 2);
		z = pow(tri[2], 2);
		if (z== x + y) {
			cout << "right" << '\n';
		}
		else {
			cout << "wrong" << '\n';
		}
	}
}
