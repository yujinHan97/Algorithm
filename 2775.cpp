#include <iostream>
#include <string>
using namespace std;
/*
	2775 부녀회장이 될 테야 
	자료구조 --> 2차원 배열 (0으로 초기화) 
	            0층부터 14층은 15칸, 1호부터 14호는 14칸이 필요하지만 그냥 [15][15]로 하고 0호는 그냥 0으로 놔둠
	알고리즘 --> 0층의 i호들을 미리 초기화 한다
				[k][n]을 구하려면 바로 옆집이랑 바로 아랫집을 더하면 된다
*/
int main() {
	int T;
	cin >> T;

	int arr[15][15] = { 0, };
	for (int i = 1; i < 15; i++) {
		arr[0][i] = i;
	}

	for (int i = 0; i < T; i++) {
		int sum = 0;
		int k, n;
		cin >> k >> n;

		for (int i = 1; i <= k; i++) {
			for (int j = 1; j <= n; j++) {
				arr[i][j] = arr[i][j - 1] + arr[i - 1][j];
			}
		}

		cout << arr[k][n] << '\n';
	}
}