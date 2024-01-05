-- 코드를 입력하세요
SELECT animal_id, name
from animal_ins
where name like "%el%" and animal_type = "dog"
order by name

# SELECT animal_id, name
# from animal_ins
# where animal_type = 'dog' and name like '%el%'
# order by name