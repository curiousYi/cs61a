.read sp17data.sql
.read fa17data.sql

CREATE TABLE obedience AS
  SELECT seven, denero, hilfinger FROM students;

CREATE TABLE smallest_int AS
  SELECT time, smallest FROM students WHERE smallest > 18 ORDER BY smallest LIMIT 20;

CREATE TABLE greatstudents AS
  SELECT fall.date, fall.color, fall.pet, fall.number, spring.number FROM students as fall, sp17students as spring 
  WHERE fall.color = spring.color AND fall.date = spring.date AND fall.pet = spring.pet;

CREATE TABLE sevens AS
  SELECT students.seven
  FROM students, checkboxes
  WHERE students.time = checkboxes.time AND students.number = 7 AND checkboxes.'7' = 'True';

CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color
  FROM students AS a, students AS b
  WHERE a.time < b.time AND a.pet = b.pet AND a.song = b.song;