#include <iostream>
#include <vector>
using namespace std;
/*
    2581 소수
    알고리즘 --> M<=  <= N 인 수에 대해서 에라토스테네스의 채를 이용해 소수 판별 후, 소수이면 벡터에 넣어서 출력값들 출력
*/
int main() {
	int M, N;
	cin >> M;
	cin >> N;

	int sum =0, min;
	vector<int> sosu;

	for(int i=M; i<=N;i++) {
		if(i == 1) {
			continue;
		}
		bool is_sosu = true;
		for(int j=2; j*j<=i;j++) {
			if(i % j == 0) {
				is_sosu = false;
				break;
			}
		}
		if(is_sosu == true) {
			sosu.push_back(i);
			sum += i;
		}
	}

	if(sosu.empty()) {
		cout << -1;
	}
	else {
		min = sosu[0];
		cout << sum << '\n';
		cout << min << '\n';
	}
}
