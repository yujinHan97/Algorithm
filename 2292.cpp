#include <iostream>
using namespace std;
/*  
    2292 : 벌집
	알고리즘 --> 6 * 1 + 1
			     6 * 3 + 1
				 6 * 6 + 1
				 6 * 10 + 1
				1 --> (+2) 3 --> (+3) 6 --> (+4) 10 --> (+5) 15 ..
				괄호안에 더해주는 수를 b, 원래수와 b를 더해 a를 만드는 규칙 
*/
int main() {
	int N;
	cin >> N;

	int start = 1;
	int num = 1;
	int a = 1;
	int b = 2;

	while (1) {
		if (N == 1) {
			cout << num;
			break;
		}
		if (N <= start + a * 6) {
			cout << num + 1;
			break;
		}
		else {
			a = a + b;
			b++;
			num++;
		}
	}
}