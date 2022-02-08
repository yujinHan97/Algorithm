/* 
  COUNT() 함수 -> WHERE 절에 지정된 기준을 충족하는 행의 수(NULL이 아닌 값)를 반환
  
  COUNT() 함수의 매개변수로는 4개의 종류가 들어갈 수 있다.
  1. ALL -> 모든 값에 적용(NULL이 아닌 값의 수를 반환)
  2. DISTINCT -> 중복 값을 무시(유니크하며 NULL이 아닌 값의 수를 반환)
  3. expression	-> 단일 상수, 변수, 스칼라 함수 또는 열 이름으로 구성된 식
  4. *	-> NULL 포함 여부에 관계없이 대상 테이블의 모든 행의 개수 

  ex) COUNT(*) : 존재하는 모든 행의 개수 (NULL 포함)
      COUNT(NAME) : NAME 컬럼에 존재하는 행의 개수 (NULL 제외)
*/
SELECT COUNT(*) AS 'count'
FROM ANIMAL_INS
