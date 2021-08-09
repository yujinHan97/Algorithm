#include <iostream>
#include <string>
#include <cmath>
using namespace std;
/*
    10250 ACM 호텔
*/
int main() {
	int T, H, W, N;
	cin >> T;
	
	string ch, ho;

	for (int i = 0; i < T; i++) {
		cin >> H >> W >> N;

		int** hotel = new int* [H];
		for (int i = 0; i < H; i++) {
			hotel[i] = new int[W];
		}

		int floor = N % H;
		if (floor == 0) {
			floor = H;
		}
		int hosu = ceil((double)N / H);

		ch = to_string(floor);
		ho = to_string(hosu);

		if (hosu >= 10) {
			cout << ch + ho << '\n';
		}
		else {
			cout << ch + "0" + ho << '\n';
		}
	}
}