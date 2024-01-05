-- 코드를 입력하세요
SELECT O.animal_id, O.name
from animal_outs O
left join animal_ins on O.animal_id = animal_ins.animal_id
where animal_ins.animal_id is null
order by animal_id


# SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME FROM ANIMAL_OUTS
# LEFT JOIN ANIMAL_INS ON ANIMAL_OUTS.ANIMAL_ID = ANIMAL_INS.ANIMAL_ID
# WHERE ANIMAL_INS.ANIMAL_ID IS NULL
# ORDER BY ANIMAL_ID