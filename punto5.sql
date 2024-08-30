-- 5. Escribe una consulta SQL para encontrar los nombres de los empleados que han gestionado pedidos de productos
-- de la categoría “Beverages” (Bebidas). Incluye en el resultado el EmployeeID, FirstName, LastName, OrderID, 
--ProductName y CategoryName.Basarse en el siguiente diagrama.


select EMP.EmployeeID, EMP.FirstName, EMP.LastName, ORD.OrderID, PRO.ProductName, CAT.CategoryName 
    from Employees EMP
    INNER JOIN Orders ORD ON EMP.EmployeeID = ORD.EmployeeID
    INNER JOIN OrderDetails ORDD ON ORD.OrderID = ORDD.OrderID
    INNER JOIN Products PRO ON PRO.Productid = ORDD.Productid
    INNER JOIN Categories CAT ON CAT.CategoryID = PRO.CategoryID
    where CAT.CategoryName = 'Beverages'
