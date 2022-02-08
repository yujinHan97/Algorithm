/* 
  GROUP BY -> 그룹으로 묶기 (유형별로 갯수를 알고 싶을 떄)
  1. GROUP BY : 특정 컬럼을 그룹화 
  2. HAVING : 특정 컬럼을 그룹화한 결과에 조건을 부여
  (WHERE는 그룹화 하기 전이고, HAVING은 그룹화 후의 조건)
*/
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS 'count'
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE
