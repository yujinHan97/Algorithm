#include <iostream>
#include <vector>
using namespace std;
/*
	9020 골드바흐의 추측
	알고리즘 --> n보다 작은 소수들을 벡터에 차례대로 넣는다.
				그 소수들을 탐색하면서 소수끼리의 합이 n과 같으면 part1, part2를 지정하는데,
				part1, part2끼리의 차를 diff로 저장하고 반복을 할 때마다 diff가 작은 소수 합을 찾는다
*/
int main() {
	int T;
	cin >> T;

	for (int t = 0; t < T; t++) {
		int n;
		cin >> n;

		// sosu 벡터에 n의 소수 넣기
		vector<int> sosu;
		for (int i = 2; i < n; i++) {
			bool is_sosu = true;
			for (int j = 2; j * j <= i; j++) {
				if (i % j == 0) {
					is_sosu = false;
					break;
				}
				else {
					is_sosu = true;
				}
			}
			if(is_sosu) sosu.push_back(i);
		}

		int diff = n; // 소수끼리의 차이 (소수 끼리의 차이가 아무리 커도 n보다는 작다)
		int part1, part2;
		for (int x = 0; x < sosu.size(); x++) {
			for (int y = x; y < sosu.size(); y++) {
				if (sosu[x] + sosu[y] == n) {
					if (diff > sosu[y] - sosu[x]) { // 소수 파티션의 차이가 작은 것 찾기
						diff = sosu[y] - sosu[x];
						part1 = sosu[x];
						part2 = sosu[y];
					}
				}
			}
		}

		cout << part1 << ' ' << part2 << '\n';
	}
}