select f.flavor
from first_half f 
join july j on f.flavor = j.flavor
group by flavor
order by sum(f.total_order + j.total_order) desc
limit 3;