#include <iostream>
#define PI 3.1415926535897932
using namespace std;
/*
	3053 택시 기하학
	알고리즘 --> 좌표상에서 그림을 그려보면, 택시 기하학에서 거리의 정의로 원을 그리면 마름모가 된다.
				따라서, 마름모의 넓이 구하는 법을 구현하면 된다.
*/
int main() {
	double r;
	cin >> r;

	cout << fixed;
	cout.precision(6);
	cout << PI * r * r << endl;

	cout << fixed;
	cout.precision(6);
	cout << 2 * r * r << endl;

}