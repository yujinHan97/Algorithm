#include <iostream>
#include <string>
using namespace std;
/*
    2839 설탕배달
    알고리즘 --> 일단 설탕이 5로 나누어지면 그게 가장 최소의 개수
                나누어 지지 않으면, 설탕을 5로 나눈 몫을 빼면서 3으로 나누어 떨어지는지 확인
*/
int main() {
	int N;
	cin >> N;

	int oh = N / 5;
	int sam;

	while (1) {
		if (oh < 0) {
			cout << -1;
			return 0;
		}
		else {
			if ((N - (oh * 5))% 3 == 0) {
				cout << oh + ((N - (oh * 5)) / 3);
				return 0;
			}
		}
		oh--;
	}
	
	cout << -1;
}