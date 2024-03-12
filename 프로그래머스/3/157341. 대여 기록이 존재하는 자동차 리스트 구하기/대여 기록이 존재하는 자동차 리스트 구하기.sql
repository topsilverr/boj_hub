-- 코드를 입력하세요
SELECT distinct(c.car_id)
from CAR_RENTAL_COMPANY_CAR c
join CAR_RENTAL_COMPANY_RENTAL_HISTORY r
on c.car_id = r.car_id
where car_type = "세단" and month(r.START_DATE) = 10
order by c.car_id desc;
# SELECT DISTINCT(r.CAR_ID)
# FROM CAR_RENTAL_COMPANY_CAR r 
# JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY h
# ON r.CAR_ID = h.CAR_ID
# WHERE r.CAR_TYPE = "세단" AND MONTH(h.START_DATE) = 10
# ORDER BY r.CAR_ID DESC;