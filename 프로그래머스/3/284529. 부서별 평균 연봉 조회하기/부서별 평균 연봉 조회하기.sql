-- 코드를 작성해주세요

select emp.dept_id,dept.dept_name_en,
       round(AVG(emp.SAL),0) as AVG_SAL
from HR_EMPLOYEES as emp
join HR_DEPARTMENT as dept
on emp.dept_id = dept.dept_id
group by emp.dept_id
order by AVG_SAL desc;

# SELECT
#     EMPLOYEES.DEPT_ID,
#     DEPARTMENT.DEPT_NAME_EN,
#     ROUND(AVG(EMPLOYEES.SAL), 0) AS  AVG_SAL
# FROM
#     HR_EMPLOYEES AS EMPLOYEES
# JOIN
#     HR_DEPARTMENT AS DEPARTMENT
# ON
#     EMPLOYEES.DEPT_ID = DEPARTMENT.DEPT_ID
# GROUP BY
#     EMPLOYEES.DEPT_ID
# ORDER BY
#     AVG_SAL DESC