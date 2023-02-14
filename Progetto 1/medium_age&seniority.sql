with table1 as(
SELECT 
FirstName || ' ' || LastName as 'Employee' ,
(strftime('%Y','now') - strftime('%Y',BirthDate))  as 'Age',
(strftime('%Y','now') - strftime('%Y',HireDate)) as 'Seniority',
Title,
Country,
CASE 
	WHEN TitleOfCourtesy = 'Dr.' THEN 'YES'
	ELSE 'not'
END as Graduated

From Employees e )

select round(AVG(age),0) as 'Medium age' , AVG(Seniority) as 'Medium seniority'  from table1

