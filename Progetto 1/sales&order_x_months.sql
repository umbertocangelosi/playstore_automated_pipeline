select 
	ROUND(SUM(od.UnitPrice * od.Quantity),2) as Amount_Of_Sales,
	count(DISTINCT o.OrderID) as Amount_of_order,
	STRFTIME('%Y', OrderDate) as year,
	STRFTIME('%m',OrderDate) as month
from
	Orders o 
join
	"Order Details" od on o.OrderID = od.OrderID 
group by
	YEAR,MONTH  

	