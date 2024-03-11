-- 코드를 작성해주세요
select YEAR(YM) as YEAR,
      round(AVG(PM_VAL1),2) as PM10,
      round(AVG(PM_VAL2),2) as 'PM2.5'
from air_pollution
where location2="수원"
group by YEAR(YM)
order by YEAR(YM) asc;

# select year(ym) AS year, 
#     round(avg(pm_val1), 2) as pm10
# ,   round(avg(pm_val2), 2) as `pm2.5`
# from air_pollution
# where location2 = '수원'
# group by year
# order by year;