-- 코드를 입력하세요
SELECT i.name, i.datetime
from animal_ins as i
where i.animal_id not in(select o.animal_id from animal_outs as o)
order by i.datetime asc
limit 3