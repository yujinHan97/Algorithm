/*
    여러 기준 정렬 -> ORDER BY에서 나열하면 된다
*/
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME ASC, DATETIME DESC
