-- 코드를 작성해주세요

select sum(g.score) as SCORE,
       e.emp_no,e.emp_name,e.position,e.email
from hr_grade g
join hr_employees e
on g.emp_no = e.emp_no
group by e.emp_no
order by score desc 
limit 1