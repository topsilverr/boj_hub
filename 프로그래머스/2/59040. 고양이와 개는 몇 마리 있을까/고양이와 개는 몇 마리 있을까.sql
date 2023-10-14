select ANIMAL_TYPE,
       count(*) as COUNT
from animal_ins
where animal_type = 'Cat' or ANIMAL_TYPE = 'Dog'
group by ANIMAL_TYPE
order by field(ANIMAL_TYPE,'Cat','Dog')