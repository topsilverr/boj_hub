select b.category,
       sum(bs.sales) as 'TOTAL_SALES'
from book as b
join book_sales as bs on b.book_id = bs.book_id
where bs.sales_date like '2022-01%'
group by b.category
order by b.category asc;