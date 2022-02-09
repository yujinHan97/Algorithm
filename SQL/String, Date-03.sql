/*
  IF문
  SELECT A, 
  IF (A에 관한 조건식, 참일 때 값, 거짓일 때 값) AS ~
*/
SELECT ANIMAL_ID, NAME, 
IF(SEX_UPON_INTAKE LIKE '%Neutered%' OR SEX_UPON_INTAKE LIKE '%Spayed%', 'O', 'X') AS '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID

/*
  CASE문
  SELECT A,
  CASE
      WHEN (A에 관한 식) THEN 값,
      WHEN ...
  ELSE 값
  END AS ~
*/
SELECT ANIMAL_ID, NAME,
CASE 
    WHEN SEX_UPON_INTAKE LIKE '%Neutered%' OR SEX_UPON_INTAKE LIKE '%Spayed%' THEN 'O'
    ELSE 'X'
    END AS '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
