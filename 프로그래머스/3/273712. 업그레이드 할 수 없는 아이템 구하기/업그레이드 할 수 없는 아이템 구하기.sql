-- 코드를 작성해주세요

# select i.item_id, i.item_name, i.rarity
# from item_info i
# left join item_tree t
# on i.item_id = t.item_id
# where

select i.item_id, i.item_name, i.rarity
from item_info i
left join item_tree t
on i.item_id = t.parent_item_id
where t.parent_item_id is null
order by item_id desc;