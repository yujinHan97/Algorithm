/*
  LIKE -> 특정 부분이 일치하는 데이터 찾기
  % : 글자 수와 상관없이 모든 글자를 의미
  _ : 글자 하나를 의미
*/
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Dog' AND NAME LIKE '%el%'
ORDER BY NAME
