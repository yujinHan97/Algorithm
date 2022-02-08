/*
  IN() 함수 -> 컬럼에서 값들에 해당되는 행만 조회
  WHERE 컬럼명 IN('값', '값2', '값3' ...) 
*/
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS 
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID
