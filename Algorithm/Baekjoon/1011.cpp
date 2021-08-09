#include <iostream>
#include <vector>
using namespace std;
/* 
    1011 Fly me to alpha centuri
*/
int main() {
	int T;
	cin >> T;

	vector<int> v;
	for (int i = 0; i < T; i++) {
		int x, y;
		cin >> x >> y;
		v.push_back(y - x);
	}

	for(int i=0; i<T;i++) {
		int count = 0;
		int dist = v[i];
		int k = 1;
		bool even = false;

		while (dist > 0) {
			dist -= k;
			count++;

			if (even) {
				k = k+1;
				even = false;
			}
			else {
				even = true;
			}
		}

		cout << count << endl;
	}
}