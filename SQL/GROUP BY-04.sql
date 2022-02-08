/* 
  (어려워서 참고한 문제!)
  HOUR변수와 시간이 같을때를 카운트 하기때문에 HOUR(DATETIME)과 HOUR변수 테이블이 같이 진행되며 COUNT를 시킨다.
*/
SET @HOUR := -1; # HOUR라는 변수 선언

SELECT (@HOUR := @HOUR +1) AS HOUR, # @HOUR가 0~ 23으로 출력될 수 있도록  
    (SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @HOUR) AS COUNT
FROM ANIMAL_OUTS 
WHERE @HOUR < 23 
