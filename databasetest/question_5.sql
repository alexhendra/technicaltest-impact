select userId, avg(duration) duration
from (
    select userId, avg(duration) duration, count(userId) count_session
    from sessions
) tmp
where tmp.count_session > 1;
