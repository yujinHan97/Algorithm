/*
  DATE_FORMAT(DATE, 형식)
  형식에는 다음과 같은 것들이 온다 (이 외에도 많이 존재)
  1. %Y = 4자리 연도
  2. %y = 2자리 연도
  3. %M = 월을 영어로 출력(January to December)
  4. %m = 월을 숫자로 출력(00-12)
  5. %D = 영어 포함(7th, 1st)
  6. %d = 일을 숫자로 출력
  7. %H = 24시간 시간 출력
  8. %h = 12시간 시간 출력
  9. %i = 분 출력
  10. %s = 초 출력
*/
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS '날짜'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
