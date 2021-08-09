#include <iostream>
#include <vector>
using namespace std;
/*
	11653 소인수분해
	자료구조 --> 벡터 2개 
				첫번째 벡터 : 약수를 저장할 벡터
				두번째 벡터 : 약수중에서 소수만 저장할 벡터
	알고리즘 --> N을 자기 약수 중에서 소수로 나누기를 반복
				소수의 개수만큼 반복하다가 N이 1이 되면 소인수 분해가 끝남
*/
int main() {
	int N;
	cin >> N;

	vector<int> yaksu;
	vector<int> sosu;
	// 약수 구하기 (1은 제외)
	for (int i = 2; i <= N; i++) {
		if (N % i == 0) { 
			yaksu.push_back(i);
		}
	}
	
	// 약수 중에서 소수 구하기
	for (int i = 0; i < yaksu.size(); i++) {
		bool is_sosu = true;
		for (int j = 2; j < yaksu[i]; j++) {
			if (yaksu[i] % j == 0) {
				is_sosu = false;
				break;
			}
		}
		if (is_sosu) {
			sosu.push_back(yaksu[i]);
		}
	}

	for (int i = 0; i < sosu.size(); i++) {
		while (1) {
			cout << sosu[i] << '\n';
			N /= sosu[i];

			if ((N == 1) || (N % sosu[i] != 0)) {
				break;
			}
		}
	}
}

