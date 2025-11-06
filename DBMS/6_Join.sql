-- Join Query
SELECT s.name, c.course FROM Students s INNER JOIN Courses c ON s.id=c.student_id;
