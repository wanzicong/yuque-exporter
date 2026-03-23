```sql
select
  count(bills_id) as record_count,
  bills_id,
  min(id)
from
  approve_bills_hi_actinst
where
  current_node_name = '样品移交'
group by
  bills_id
having
  count(bills_id) > 1
```



```sql
select
  *
from
  approve_bills_hi_actinst
where
  bills_id = '163402'
  and current_node_name = '样品移交'
  order by gmt_create asc 
```



```sql
select
  count(bills_id) as record_count,
  bills_id,
  min(id),current_node_name
from
  approve_bills_hi_actinst
where
  current_node_name in ('样品移交','样品签收','样品归还','样品收取')
group by
  bills_id , current_node_name
having
  count(bills_id) > 1


select
  min(id) as id 
from
  approve_bills_hi_actinst
where
  current_node_name in ('样品移交','样品签收','样品归还','样品收取')
group by
  bills_id , current_node_name
having
  count(bills_id) > 1


select
  *
from
  approve_bills_hi_actinst
where
  current_node_name in ('样品移交', '样品签收', '样品归还', '样品收取')
  and id not in (
    select
      min(id) as id
    from
      approve_bills_hi_actinst
    where
      current_node_name in ('样品移交', '样品签收', '样品归还', '样品收取')
    group by
      bills_id,
      current_node_name
    having
      count(bills_id) > 1
  )




```



<details class="lake-collapse"><summary id="u7bb14345"><span class="ne-text">流程修改</span></summary><p id="ub7814d4d" class="ne-p"><br></p><p id="ue0b56236" class="ne-p"><br></p><p id="ue1501c5b" class="ne-p"><br></p><p id="uce0e4898" class="ne-p"><br></p><p id="ub6824948" class="ne-p"><br></p></details>


[此处为语雀卡片，点击链接查看](about:blank#G23E0)





| done | 进行中 | 2023-06-09 | link |
| --- | --- | --- | --- |






