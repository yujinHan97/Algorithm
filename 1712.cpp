#include <iostream>
using namespace std;
/* 
    1712 손익분기점
    알고리즘 --> A + B*n < C*n 를 만족하면 손익분기점이 발생한다. 
                따라서, n> A/(C-B) 인 경우에 손익 분기점이 발생하고, 나눗셈은 나머지를 버리게되므로, +1을 해줘야 한다
                따라서, B가 C 이상인 경우에는 손익분기점은 절대 발생하지 않는다.
                
*/
int main() {
    int A, B, C;
    cin >> A >> B >> C;

    if(B>=C) { 
        cout << -1;
    }
    else {
        cout << A / (C-B) + 1;
    }
}
