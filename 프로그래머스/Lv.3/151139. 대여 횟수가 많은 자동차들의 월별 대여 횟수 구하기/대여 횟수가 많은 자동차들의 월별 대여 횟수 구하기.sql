-- 코드를 입력하세요
SELECT MONTH(start_date) as MONTH, car_id, count(history_id) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where car_id in (select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY where MONTH(start_date) in (8,9,10) group by car_id having count(history_id)>=5)
and month(start_date) in (8,9,10)
group by month,car_id
having count(history_id)>=1
order by month, car_id desc;



# SELECT MONTH(START_DATE) AS MONTH
#      , CAR_ID
#      , COUNT(HISTORY_ID) AS RECORDS
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# WHERE CAR_ID IN (SELECT CAR_ID
#                  FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
#                  WHERE MONTH(START_DATE) IN (8, 9, 10)
#                  GROUP BY CAR_ID
#                  HAVING COUNT(HISTORY_ID) >= 5)
#       AND MONTH(START_DATE) IN (8, 9, 10)
# GROUP BY MONTH, CAR_ID
# HAVING COUNT(HISTORY_ID) >= 1
# ORDER BY MONTH
#        , CAR_ID DESC;
