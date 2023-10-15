-- 코드를 입력하세요
SELECT p.product_code, sum(o.sales_amount)*p.price as total_sales
from product as p join offline_sale as o on p.product_id = o.product_id
group by p.product_code
order by total_sales desc, p.product_code asc