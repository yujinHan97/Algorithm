#include <iostream>
using namespace std;
/*
    1193 분수찾기
*/
int main() {
	int N;
	cin >> N;

	int index = 0;
	for (int i = 0; ;i++) {
		int a = i * (i + 1) / 2;
		int b = (i + 1) * (i + 2) / 2;

		if (a <= N && b >= N) {
			index = i + 1;
			break;
		}
	}

	int low = ((index -1) * index / 2) + 1;
	int dist = N - low;
	int sum = index + 1;
	int mo, ja;
	if (index % 2 == 0) {
		mo = index;
		ja = 1;
		for (int i = 0; i < dist; i++) {
			mo--;
			ja++;
		}
	}
	else {
		mo = 1;
		ja = index;
		for (int i = 0; i < dist; i++) {
			mo++;
			ja--;
		}
	}

	cout << ja << "/" << mo << endl;
}