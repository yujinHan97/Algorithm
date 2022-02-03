/* 
  정렬 -> ORDER BY 
  ORDER BY 절은 항상 SELECT의 맨 마지막 줄에 위치.
  기본은 오름차순이며, 내림차순을 하려면 ANIMAL_ID DESC -> DESC를 명시
*/
내림차순 하려면, ANIMAL_ID DESC
SELECT * 
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
