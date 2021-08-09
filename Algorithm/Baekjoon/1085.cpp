#include <iostream>
using namespace std;
int main() {
	int x, y, w, h;
	cin >> x >> y >> w >> h;

	int* dist = new int[4];
	dist[0] = x;
	dist[1] = y;
	dist[2] = h - y;
	dist[3] = w - x;

	int min = dist[0];
	for (int i = 1; i < 4; i++) {
		if (dist[i] < min) {
			min = dist[i];
		}
	}

	cout << min << endl;
}