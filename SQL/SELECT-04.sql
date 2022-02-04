/*
    WHERE 절에서의 부정:
    1. 컬럼명 != 값
    2. NOT 컬럼명 = 값
    3. 컬럼명 <> 값
*/
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged'
# WHERE NOT INTAKE_CONDITION = 'Aged'
# WHERE INTAKE_CONDITION <> 'Aged'
