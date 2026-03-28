# Database-3

## Aggregation

### COUNT()
Counts the number of rows.
```
SELECT COUNT(*)
FROM employees;
```

P.S : Number of employees in IT.

```
SELECT COUNT(*) FROM employees WHERE department='IT';
```

### SUM()
Calculates total value.

P.S : Total salary paid by company.
```
SELECT SUM(salary) FROM employees;
```

with-alias :
```
SELECT SUM(salary) as total_salary_paid FROM employees;
```

### AVG()
Calculates average value

P.S : average salary of employees
```
SELECT AVG(salary) FROM employees;
```

### MIN() and MAX()

Lowest Salary :
```
SELECT MIN(salary) FROM employees;
```

Highest Salary :
```
SELECT MAX(salary) FROM employees;
```

### Nested Query

P.S : Employee name with the highest salary

With Order by and Limit
```
select name, salary from employees order by salary desc limit 1;
```
With nested/sub-query :
```
select * from employees
where salary=(
    SELECT MAX(salary) FROM employees
);
```
## GROUP BY

GROUP BY groups rows based on column values.

Then aggregate functions are applied per group.

P.S : What is the average salary per department?

```
SELECT department, AVG(salary)
FROM employees
GROUP BY department;
```

P.S : Count employees per city.
```
SELECT city, count(*) FROM employees
GROUP BY city;
```

## HAVING
HAVING filters groups, not rows.

P.S : Departments with average salary above 70000.
```
SELECT department, AVG(salary) as avg_salary FROM employees
GROUP BY department
HAVING avg_salary > 70000;
```

without-alias :
```
SELECT department, AVG(salary) 
FROM employees
GROUP BY department
HAVING AVG(salary) > 70000;
```

## WHERE vs HAVING
| Feature         | WHERE    | HAVING         |
| --------------- | -------- | -------------- |
| Filters         | rows     | groups         |
| Used before     | GROUP BY | after GROUP BY |
| Uses aggregates | ❌        | ✅              |

## FLOW OF QUERY
```
SELECT department, AVG(salary)
FROM employees
WHERE city='Delhi'
GROUP BY department
HAVING AVG(salary) > 70000
ORDER BY AVG(salary) DESC
LIMIT 3;
```

The above query is giving top 3 department by salary from city delhi with Average salary greater than 70000

```
FROM --> WHERE --> GROUP BY --> HAVING --> SELECT --> ORDER BY --> LIMIT
```

FILTER -> GET final DATA -> Arrange --> Limit the output

df.head(2)

## JOINS

- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- FULL JOIN

To use joins, you need multiple tables.

Creating tables for JOINS topic :
```
CREATE TABLE departments (
    dept_id INTEGER PRIMARY KEY,
    dept_name TEXT NOT NULL
);


CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    salary INTEGER,
    dept_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY,
    project_name TEXT
);

CREATE TABLE employee_projects (
    emp_id INTEGER,
    project_id INTEGER,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
  
);
```

Inserting data in tables above to perform JOINS :
```
INSERT INTO departments VALUES (1,'IT');
INSERT INTO departments VALUES (2,'HR');
INSERT INTO departments VALUES (3,'Finance');
INSERT INTO departments VALUES (4,'Marketing');

INSERT INTO employees VALUES (1,'Rahul',70000,1);
INSERT INTO employees VALUES (2,'Neha',60000,2);
INSERT INTO employees VALUES (3,'Aman',80000,1);
INSERT INTO employees VALUES (4,'Sara',75000,3);
INSERT INTO employees VALUES (5,'John',65000,2);
INSERT INTO employees VALUES (6,'Riya',90000,1);
INSERT INTO employees VALUES (7,'David',72000,NULL);

INSERT INTO projects VALUES (1,'AI Platform');
INSERT INTO projects VALUES (2,'HR Automation');
INSERT INTO projects VALUES (3,'Finance Dashboard');

INSERT INTO employee_projects VALUES (1,1);
INSERT INTO employee_projects VALUES (3,1);
INSERT INTO employee_projects VALUES (2,2);
INSERT INTO employee_projects VALUES (4,3);
INSERT INTO employee_projects VALUES (6,1);
```

P.S (JOINS) : Get employee name and department name.

select name, dept_id from employees;

### Inner Join
INNER JOIN returns only rows where matching data exists in both tables.

Query :
```
SELECT employees.name, departments.dept_name
FROM employees
INNER JOIN departments
ON employees.dept_id = departments.dept_id;
```

Query-with-alias :
```
SELECT emp.name, dept.dept_name
FROM employees as emp
INNER JOIN departments as dept
ON emp.dept_id = dept.dept_id;
```