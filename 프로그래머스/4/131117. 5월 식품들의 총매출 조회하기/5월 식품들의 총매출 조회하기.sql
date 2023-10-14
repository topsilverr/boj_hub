-- 코드를 입력하세요
SELECT p.product_id, p.product_name, p.price * sum(o.amount) as 'total_sales'
from food_product as p
join food_order as o on p.product_id = o.product_id
where o.produce_date like '2022-05%'
group by p.product_id
order by total_sales desc, p.product_id asc;