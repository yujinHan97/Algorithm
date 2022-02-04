/*
    조건 -> WHERE
    문자열은 작은 따옴표로 묶는다
*/
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'
