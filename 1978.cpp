#include <iostream>
using namespace std;
/*
	1978 소수찾기
	알고리즘 --> 어떤 수가 2부터 자기 자신보다 작은 수로 나누어지면 소수가 아닌걸로 판단
*/
int main() {
	int N;
	cin >> N;

	int* arr = new int[N];
	int count = N;
	for (int i = 0; i < N; i++) {
		cin >> arr[i];

		if (arr[i] == 1) { 
			count--;
		}

		for (int j = 2; j < arr[i]; j++) {
			if (arr[i] % j == 0) {
				count--;
				break;
			}
		}
	}

	cout << count << endl;
}