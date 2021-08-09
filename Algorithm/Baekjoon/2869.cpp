#include <iostream>
#include <cmath>
using namespace std;
/* 
	2869 달팽이는 올라가고 싶다
	알고리즘 --> 처음 생각했던 알고리즘은 올라간 만큼 높이에서 빼고, 내려가는 만큼 높이에서 더하는 과정 반복 ==> 시간초과
	
				그래서 생각한 다른 방법은 맨 마지막날에 올라가는 걸 먼저 높이에서 뺀 다음, 
				올라가는 높이랑 내려가는 높이를 뺀 총 이동량을 남은 높이에서 나눈다.
				나누는 과정에서 소수가 다 버려질 수 있으므로 ceil써서 올림
*/

int main() {
	double a, b, v;
	cin >> a >> b >> v;

	int days = 0;
	v -= a;
	days++;

	int num = ceil((v / (a - b)));
	days += num;
	cout << days;
}