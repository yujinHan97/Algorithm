#include <iostream>
using namespace std;
/*
	4948 베르트랑 공준
	알고리즘 --> 에라토스테네스의 채 사용
*/

void count_sosu(int n) {
	int count = 0;

	for (int i = n + 1; i <= 2 * n; i++) {
		bool is_sosu = true;
		for (int j = 2; j *j <= i; j++) {
			if (i % j == 0) {
				is_sosu = false;
				break;
			}
		}

		if (is_sosu) {
			count++;
		}
	}

	cout << count << '\n';
}

int main() {
	while (1) {
		int n;
		cin >> n;

		if (n == 0) {
			break;
		}

		count_sosu(n);
	}
}
