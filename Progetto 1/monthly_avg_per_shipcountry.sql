WITH temp1 AS 

	(
	SELECT
		SUM(UnitPrice * Quantity) as OrderAmount
		,od.OrderID
		,strftime('%Y %m',o.OrderDate) as OrderDate
		,STRFTIME('%Y', o.OrderDate) as YearOfSale 
	FROM
		"Order Details" od
	LEFT JOIN
		Orders o ON o.OrderID = od.OrderID		
	WHERE
		strftime('%Y %m',o.OrderDate) != "2016 07" AND
		strftime('%Y %m',o.OrderDate) != "2018 05"
	GROUP BY
		2		
	),
		
	temp2 AS 
	
	(
	SELECT 
		ShipCountry	AS Country 
		,SUM(temp1.OrderAmount) as TotalSold
		,temp1.YearOfSale
	FROM
		Orders o 
	LEFT JOIN
		temp1 ON o.OrderID = temp1.OrderID
	GROUP BY 
		1, 3
	ORDER BY
		2 DESC
	),
	
	temp2016 AS
	
	(
	SELECT
		temp2.Country
		,ROUND(temp2.TotalSold / 5,0) AS MonthlyAvg
		,temp2.YearOfSale
	FROM 
		temp2
	WHERE 
		YearOfSale = '2016'
	ORDER BY
		1
	),
	
	temp2017 AS
	
	(
	SELECT
		temp2.Country
		,ROUND(temp2.TotalSold / 12,0) AS MonthlyAvg
		,temp2.YearOfSale		
	FROM
		temp2
	WHERE 
		YearOfSale = '2017'
	ORDER BY
		1
	),

	temp2018 AS
	
	(
	SELECT
		temp2.Country
		,ROUND(temp2.TotalSold / 4, 0) AS MonthlyAvg
		,temp2.YearOfSale
		
	FROM
		temp2
	WHERE
		YearOfSale = '2018'
	ORDER BY
		1
	)
	
SELECT * FROM temp2016
UNION ALL
SELECT * FROM temp2017
UNION ALL
SELECT * FROM temp2018