#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
/*
    2798 블랙잭
    알고리즘 :
    1. 카드 3장의 합이 M 이하면, 그 합을 벡터에 추가
    2. 벡터를 내림차순 정렬하면, 제일 첫 번째 요소가 M에 가장 가까운 값
*/
int main() {
    int N, M;
    cin >> N >> M;

    int *card = new int[N];
    for(int i=0; i<N;i++) {
        cin >> card[i];
    }

    int sum = 0;
    vector<int> card_sum;
    for(int x = 0; x<N-2;x++) {
        for(int y = x+1; y<N-1;y++) {
            for(int z = y+1; z<N;z++) {
                sum = card[x] + card[y] + card[z];
                if(sum <= M) {
                    card_sum.push_back(sum);
                }
            }
        }
    }

    sort(card_sum.begin(), card_sum.end(), greater<>());
    cout << card_sum[0];
}