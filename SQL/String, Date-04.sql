/*
  DATE 타입끼리는 기본적인 연산 가능
  따라서, DATETIME의 차이를 내림차순 정렬하면, 가장 긴 보호시간 동물을 알 수 있고, LIMIT 2로 2마리만 출력
*/
SELECT AI.ANIMAL_ID, AI.NAME
FROM ANIMAL_INS AI, ANIMAL_OUTS AO
WHERE AI.ANIMAL_ID = AO.ANIMAL_ID
ORDER BY AO.DATETIME - AI.DATETIME DESC
LIMIT 2
