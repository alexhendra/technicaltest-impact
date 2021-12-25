select i.name, s.name
from items i inner join sellers s
on s.id = i.sellerId
where s.rating > 4;