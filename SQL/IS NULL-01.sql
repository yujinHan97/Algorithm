/* 
  IS NULL -> NULL 값인지 확인
  IS NOT NULL -> NULL 값이 아닌지 확인
*/
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL
ORDER BY ANIMAL_ID
