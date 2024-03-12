-- 코드를 작성해주세요

select i.item_id, item_name
from item_info i
where i.item_id in (select item_id from item_tree where parent_item_id is null)
order by i.item_id asc;