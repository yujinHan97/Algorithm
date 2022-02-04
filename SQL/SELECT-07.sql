/*
    상위 N개 레코드 -> LIMIT 사용
    LIMIT 1 : 맨 위에서부터 1개까지의 정보 조회
    LIMIT 3 : 맨 위에서부터 3개까지의 정보 조회
    LIMIT 2, 6 : 위에서 2번째부터 6번째까지의 정보 조회
    먼저 DATETIME으로 정렬해야 가장 먼저 들어온 동물 알 수 있다. 
*/
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1
