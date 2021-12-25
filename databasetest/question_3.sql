select man.id, man.name, COUNT (emp.id) AS number_of_employees
from employees emp inner join employees man
ON emp.managerId = man.id
GROUP BY man.id, man.name;