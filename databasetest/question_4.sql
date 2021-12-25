select count(id) from students
where score > (
    select avg(score) from students
);