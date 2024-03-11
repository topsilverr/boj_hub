-- 코드를 작성해주세요
SELECT S.EMP_NO
     , E.EMP_NAME
     , CASE WHEN S.SCORE >= 96 THEN 'S'
            WHEN S.SCORE >= 90 THEN 'A'
            WHEN S.SCORE >= 80 THEN 'B'
            ELSE 'C'
            END AS GRADE
     , CASE WHEN S.SCORE >= 96 THEN E.SAL*0.2
            WHEN S.SCORE >= 90 THEN E.SAL*0.15
            WHEN S.SCORE >= 80 THEN E.SAL*0.1
            ELSE 0
            END AS BONUS
FROM (
    SELECT EMP_NO, AVG(SCORE) AS SCORE
    FROM HR_GRADE
    GROUP BY EMP_NO
) AS S
LEFT JOIN HR_EMPLOYEES E
    ON S.EMP_NO = E.EMP_NO
        
# select emp_no,emp_name,
#        case when score >= 96 then "S"
#             when score >= 90 and score < 96 then "A" 
#             when score >= 80 and score < 90 then "C"
#             else "C"
#             end as GRADE,
#         case when grade = "S" then sal*0.2
#              when grade = "A" then sal*0.15
#              when grade = "C" then sal*10
#              else 0
#              end as BONUS
# from 