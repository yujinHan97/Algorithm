#include <iostream>
#include <cmath>
using namespace std;
/*
    1002 터렛
    알고리즘 --> 먼저, 두 사람의 중심이 같은경우와 다른 경우로 크게 분류
				두 사람의 중심이 같은 경우, 반지름이 같으면 두 원이 일치 --> -1 (무한대)
										   반지름이 다르면 만나지 않음 --> 0
				두 사람의 중심이 다른 경우, 두점에서 만나면 2 / 외접, 내접하면 1 / 만나지 않으면 0
*/
int main() {
	int T;
	cin >> T;

	int position;
	int x1, y1, r1, x2, y2, r2;
	for (int i = 0; i < T; i++) {
		cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;

		int square_x = pow(x2 - x1, 2);
		int square_y = pow(y2 - y1, 2);
		double dist = sqrt(square_x + square_y);

		if (x1 == x2 && y1 == y2) {
			if (r1 == r2) { // 중심, 반지름 모두 완전 일치하는 경우
				position = -1;
			}
			else { // 중심만 일치하고, 반지름은 일치하지 않는 경우
				position = 0;
			}
		}
		else {
			if (abs(r1 - r2) < dist && dist < r1 + r2) { // 두 점에서 만나는 경우
				position = 2;
			}
			else if (dist == r1 + r2) { // 외접하는 경우
				position = 1;
			}
			else if (abs(r1 - r2) == dist) { // 내접하는 경우
				position = 1;
			}
			else {
				position = 0;
			}

		}

		cout << position << endl;
	}
}
