-- 코드를 입력하세요
SELECT o.animal_id, o.name
from animal_outs o
left join animal_ins i on o.animal_id = i.animal_id
order by (datediff(o.datetime,i.datetime)) desc
limit 2


# SELECT O.ANIMAL_ID, O.NAME
# FROM ANIMAL_OUTS O
# LEFT JOIN ANIMAL_INS I
# ON O.ANIMAL_ID = I.ANIMAL_ID
# ORDER BY (DATEDIFF(O.DATETIME,I.DATETIME)) DESC
# LIMIT 2