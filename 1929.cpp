#include <iostream>
using namespace std;
/*
	1929 소수 구하기
	알고리즘 --> 에라토스테네스 채 사용
*/
int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int M, N;
	cin >> M;
	cin >> N;

	for (int i = M; i <= N; i++) {
		if (i == 1) {
			continue;
		}
		bool is_sosu = true;
		for (int j = 2; j * j <= i; j++) {
			if (i % j == 0) {
				is_sosu = false;
				break;
			}
		}
		if (is_sosu == true) {
			cout << i<<'\n';
		}
	}
}

