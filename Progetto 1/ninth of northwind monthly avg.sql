WITH temp1 AS 
	(
	SELECT 
		 SUM(od.UnitPrice * od.Quantity) as TotalSold
		,STRFTIME('%Y', o.OrderDate) as "Year"
	FROM
		"Order Details" od 
	LEFT JOIN
		Orders o ON od.OrderID = o.OrderID
	WHERE 
		strftime('%Y %m',o.OrderDate) != "2016 07" AND
		strftime('%Y %m',o.OrderDate) != "2018 05"
	GROUP BY
		2
	)
	
SELECT
	ROUND(temp1.TotalSold / (5*9), 0) AS ComparisonAvg
	,temp1."Year"
FROM
	temp1
WHERE 
	"Year" = '2016'

UNION ALL 

SELECT
	ROUND(temp1.TotalSold / (12*9),0) AS ComparisonAvg
	,temp1."Year"
FROM 
	temp1
WHERE 
	"Year" = '2017'

UNION ALL

SELECT
	ROUND(temp1.TotalSold / (4*9),0) AS ComparisonAvg
	,temp1."Year"
FROM 
	temp1
WHERE 
	"Year" = '2018'
	
	