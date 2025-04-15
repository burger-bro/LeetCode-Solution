USE exe1;
CREATE TABLE Person (
    personId INT PRIMARY KEY,
    lastName VARCHAR(10),
    firstName VARCHAR(10)
);

INSERT INTO Person (personId, lastName, firstName)
VALUES 
    (1, "Wang", "Allen"),
    (2, "Alice", "Bob");

DROP TABLE IF EXISTS Address;

CREATE TABLE Address (
    addressId INT PRIMARY KEY,
    personId INT,
    city VARCHAR(10),
    state VARCHAR(10)
);

INSERT INTO Address (addressId, personId, city, state)
VALUES 
    (1, 2, "NYC", "NY"),
    (2, 3, "LC", "CA");

SELECT firstName, lastName, city, state FROM address a 
RIGHT JOIN person p 
ON p.personId = a.personId;

SELECT firstName, lastName, city, state FROM person p 
LEFT join address a 
ON p.personId = a.personId;

SELECT firstName, lastName, city, state FROM person p, address a
WHERE p.personId = a.personId
UNION
SELECT firstName, lastName, NULL, NULL FROM person p
WHERE p.personId NOT IN (SELECT personId FROM address)


SELECT firstName, lastName, city, state FROM person p 
INNER JOIN address a 
ON p.personId = a.personId;

SELECT MAX(personId) from person p
UNION
SELECT personId from person p


SELECT personId
FROM
  (SELECT MAX(personId) from person p
UNION
SELECT p.personId from person p) a
  LEFT JOIN (SELECT MAX(personId) from person p) b
    ON a.personId = b.personId 
WHERE b.personId IS NULL 

SELECT a1.machine_id, round(avg(a1.timestamp-a2.TIMESTAMP), 3) as p 
FROM activity a1
JOIN activity a2
ON a1.activity_type = 'end' and a2.activity_type = 'start'
and a1.machine_id = a2.machine_id and a1.process_id = a2.process_id
GROUP BY a1.machine_id


SELECT MAX(salary) FROM employee as M
SELECT -salary FROM employee

SELECT salary FROM employee ORDER BY salary DESC;

SELECT MIN(e4.salary) as SecondHighestSalary FROM
(SELECT e3.salary FROM 
(SELECT e1.salary
FROM employee e1
inner JOIN employee e2 on e1.salary = e2.salary) e3
ORDER BY e3.salary DESC LIMIT 2) e4

SELECT MAX(salary) AS SecondHighestSalary
FROM employee
WHERE salary < (SELECT MAX(salary) FROM employee);

SELECT DISTINCT salary AS SecondHighestSalary
FROM employee
ORDER BY salary DESC
LIMIT 1,1; 

SELECT MAX(E.salary) as SecondHighestSalary 
FROM (SELECT salary FROM Employee WHERE salary < 
(SELECT MAX(salary) FROM Employee)) E

/* SELECT e1.id
FROM employee e1
JOIN SELECT e2.id, MAX(salary) FROM employee e2
ON e1.id = e2.id
GROUP BY e1.id */


Create table If Not Exists Queue (person_id int, person_name varchar(30), weight int, turn int);
Truncate table Queue;
insert into Queue (person_id, person_name, weight, turn) values ('5', 'Alice', '250', '1');
insert into Queue (person_id, person_name, weight, turn) values ('4', 'Bob', '175', '5');
insert into Queue (person_id, person_name, weight, turn) values ('3', 'Alex', '350', '2');
insert into Queue (person_id, person_name, weight, turn) values ('6', 'John Cena', '400', '3');
insert into Queue (person_id, person_name, weight, turn) values ('1', 'Winston', '500', '6');
insert into Queue (person_id, person_name, weight, turn) values ('2', 'Marie', '200', '4');


SELECT * FROM queue ORDER BY turn 

# 思路：从已排序的turn列中，按顺序累加weight列，取累加weight列最大且小于1000的id
SELECT ACCUM.person_name FROM
(SELECT 
        person_id,
        person_name,
        turn, 
        weight,
        SUM(weight) OVER (ORDER BY turn) AS cumulative_weight
    FROM queue) ACCUM
WHERE ACCUM.cumulative_weight <= 1000
ORDER BY ACCUM.cumulative_weight DESC
LIMIT 1

SELECT 
    q1.person_name, q1.turn, q2.turn
FROM Queue q1 JOIN Queue q2 ON q1.turn >= q2.turn ORDER BY q1.turn
