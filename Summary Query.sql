select category, `condition`, avg(sourcing_price) * 100 / avg(Retail_price) as AVG_Q1
from scrapped_diff_thredup_tbl
group by category,`condition`;
 
select category, `condition`, avg(sourcing_price) * 100 / avg(Retail_price) as AVG_Q2
from scrapped_diff_thredup_tbl
where mark_down ='mark_down'
group by category,`condition`
union
select a.Category, a.`Condition`, avg(a.sourcing_price) * 100 / avg(a.Retail_price) as AVG_Q2 from scrapped_diff_thredup_tbl as a 
inner join scrapped_diff_thredup_tbl as b
on a.category=b.category and a.item_number=b.item_number 
and a.`Condition` not in ('No-Filter')
and b.mark_down='mark_down'
group by a.category,a.`condition`;

-- Q3
Select (select Sum(sales_price) from  scrapped_diff_thredup_tbl
where mark_down='mark_down')  * 100 / 
   (select Sum(sales_price) from  scrapped_diff_thredup_tbl) as Total_Sales; 
 
 
 select category, `condition`, avg(sourcing_price) * 100 / avg(Retail_price) as AVG_Q4
from scrapped_diff_thredup_tbl
where mark_down ='new_arrival'
group by category,`condition`
union
select a.Category, a.`Condition`, avg(a.sourcing_price) * 100 / avg(a.Retail_price) as AVG_Q4 from scrapped_diff_thredup_tbl as a 
inner join scrapped_diff_thredup_tbl as b
on a.category=b.category and a.item_number=b.item_number 
and a.`Condition` not in ('No-Filter')
and b.mark_down='new_arrival'
group by a.category,a.`condition`;
