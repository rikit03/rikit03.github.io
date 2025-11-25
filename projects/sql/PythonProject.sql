USE [AdventureWorksLT2019]
GO

/****** Object:  StoredProcedure [dbo].[PythonProject]    Script Date: 12/3/2024 4:05:57 PM ******/
--SUDENT NAME: RIKIT THAPA
--STUDENT NUMBER:500232522
--PROFESSOR: JOHN FRASCO


ALTER PROCEDURE [dbo].[PythonProject] @ProductCategoryID INT, @Percent DECIMAL(3,2)
AS
Select @ProductCategoryID

--Create Temporary table to TEST and to make sure records return VALID DATA for UPDATE
CREATE TABLE #ProductIDPython(
CategoryID int,
StandardCost Money,
Weight Decimal (8,2),
SizeCHAR varchar(5),
SizeDecimal Numeric (5,2)
)
BEGIN

--BEGIN UPDATE TO TEMP TABLE FOR VERIFICATION WITH DATASET

BEGIN
INSERT INTO #ProductIDPython(CategoryID,StandardCost,Weight,SizeCHAR,SizeDecimal )
SELECT
ProductCategoryID,
StandardCost * @Percent,
Weight * @Percent,
Size,
TRY_CAST (Size AS numeric(5,2)) * @Percent

FROM SalesLT.Product
WHERE ProductCategoryID = @ProductCategoryID

--END UPDATE TO TEMP TABLE FOR VERIFICATION WITH DATASET
--UPDATE #ProductIDPyibrthon SET SizeDecimal=(SELECT TRY_CAST ( [Size]AS decimal(3,0)) *1.05 AS DECIMAL
--FROM SalesLT.Product

UPDATE #ProductIDPython SET SizeCHAR = TRY_CAST (SizeDecimal AS CHAR (5))

END

--SELECT STATEMENTS TO REVIEW DATA
--SELECT ProductCategoryID, StandardCost, Weight, Size
--From SalesLT.Product
--WHERE (ProductcategoryID = @ProductcategoryID)

SELECT * FROM #ProductIDPython

UPDATE [SalesLT].[Product]
SET StandardCost = #ProductIDPython.StandardCost,
Weight = #ProductIDPython.Weight,
Size = #ProductIDPython.SizeCHAR
FROM #ProductIDPython INNER JOIN
            SalesLT.Product ON #ProductIDPython.CategoryID = SalesLT.Product.ProductCategoryID

END

