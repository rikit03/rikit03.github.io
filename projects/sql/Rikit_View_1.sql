--USE [AdventureWorksLT2019]
GO
--Name: rikit thapa
--student_id : 500232522

SELECT TOP (100) PERCENT ProductCategoryID, Name
FROM     SalesLT.ProductCategory
ORDER BY ProductCategoryID, Name

