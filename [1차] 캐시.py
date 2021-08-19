'''
    알고리즘:
    1. 캐시니까 dict 자료구조 사용, 캐시의 알고리즘은 LRU(최근에 사용되지 않은 것 먼저 제거) 사용하므로,
    2. cache hit인 경우, 해당 단어를 삭제하고 다시 추가해서 순서를 뒤로가게 한다
    3. cache miss인 경우,
        - 이미 cache 사이즈가 꽉 찬 경우, 첫 번째 요소 삭제하고 새로운 요소 넣기
        - 아직 cache 사이즈가 남아 있는 경우, 새로운 요소 넣기
    ** cache size가 애초에 0인 경우는 모두 캐시 미스 --> test case 해보고 틀린걸 알았다. 처음부터 고려하고 코딩했어야 하는 부분! 주의!!
'''
def solution(cacheSize, cities):
    answer = 0
    
    # 캐시의 사이즈가 0이면 모두 캐시 미스
    if cacheSize == 0:
        return 5 * len(cities)

    cache = {}
    for city in cities:
        city = city.lower()

        if city in cache.keys(): # cache hit
            del(cache[city])
            cache[city] = 1
            answer += 1
        else: # cache miss
            if len(cache) == cacheSize:
                # 첫 번째 요소 찾은 후, 삭제
                for key, value in cache.items():
                    temp = key
                    break
                del(cache[temp])

            cache[city] = 1
            answer += 5

    return answer
