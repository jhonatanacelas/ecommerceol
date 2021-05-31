-- SQL for orders paid

select orders.order_id
from orders
         join
     (select order_id, sum(value) paid
      from installment
      group by (order_id) ) as orders_paid
     on orders.order_id = orders_paid.order_id
where orders.total_value == orders_paid.paid