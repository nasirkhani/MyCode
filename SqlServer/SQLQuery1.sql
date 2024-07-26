use NikamoozDB;
Go

--دیدن برخی از فیلد های جدول 
select
	OrderID, CustomerID, EmployeeID, OrderDate
from dbo.Orders;
go

-- استفاده از alias در بخش from

select
	o.Freight,o.ShipperID
from dbo.Orders as o;
go

select *
from OrderDetails;
go

-- مشاهده اسکیمای پیش فرض
select SCHEMA_NAME();
go

-- مشاهده فهرستی از اسکیماهای دیتابیس
select * from sys.schemas;
go

-- بررسی وجود اسکیما و حذف آن
drop schema if exists myschema;
go

-- نحوه ایجاد اسکیما
create schema myschema;
go

-- حذف جدول در صورت وجود
drop table if exists myschema.tbl1;
go

-- ایجاد یک جدول در یک اسکیما
create table myschema.tbl1
(
	id int
);
go

-- دسترسی به اسکیمای یک جدول
select * from INFORMATION_SCHEMA.TABLES /*تمامی اسکیماهای مرتبط با جداول یک دیتابیس*/
	where TABLE_NAME = 'tbl1';
go

-- درج رکورد در جدول
insert into myschema.tbl1
	values (1),(2),(3),(4),(5);
go

select * from myschema.tbl1;
	drop schema myschema;
go

select
	OrderID,year(orderdate) as od
from dbo.Orders
	where year(OrderDate) > 2015;
go

select
	EmployeeID, YEAR(orderdate) as orderyear
from dbo.Orders
	where CustomerID = 71
order by EmployeeID desc;
go

select
	Freight, YEAR(OrderDate) as orderyear
from dbo.Orders
	where orders.CustomerID = 71
order by orderyear desc;
go

select
	EmployeeID, Region, City
from dbo.Employees
order by Region, City;
go

select
	EmployeeID, FirstName, LastName, State
from dbo.Employees
order by City;
go

select * from dbo.Employees;


SELECT 
	EmployeeID, YEAR(OrderDate) as OrderYear
FROM dbo.Orders
	where CustomerID = 71
ORDER BY EmployeeID;
go

SELECT 
	DISTINCT EmployeeID, YEAR(OrderDate) as OrderYear
FROM dbo.Orders
	where CustomerID = 71
ORDER BY EmployeeID;
go

select distinct State, EmployeeID
from dbo.Employees
order by EmployeeID;
go

select
	distinct State, EmployeeID
from dbo.Employees
order by EmployeeID desc;
go

select
	OrderID, OrderDate
from dbo.Orders
order by OrderDate desc;
go

select 
	top (5) OrderID, OrderDate
from dbo.Orders
order by OrderDate desc;
go

select 
	top (5) OrderID, OrderDate
from dbo.Orders
order by OrderDate;
go


<<<<<<< HEAD
select
	OrderID, CustomerID
from dbo.Orders
	where CustomerID = 71;
go

select
	OrderID, CustomerID, OrderDate
from dbo.Orders
	where OrderID in (10248,10253,10320);
go

select
	OrderID, OrderDate
from dbo.Orders
	where OrderID not in (10248,10253,10320);
go

select
	OrderID, EmployeeID
from dbo.Orders
	where EmployeeID between 3 and 7;
go

select
	OrderID, EmployeeID
from dbo.Orders
	where EmployeeID in (3,4,5,6,7);
go

select
	FirstName, LastName
from dbo.Employees
	where LastName like N'ا%';
go

select
	FirstName, LastName
from dbo.Employees
	where LastName like N'[^ا]%';
go

select
	FirstName, LastName
from dbo.Employees
	where LastName not like N'ا%';
go
=======
select 
	top (5) percent OrderID, OrderDate
from dbo.Orders
order by OrderDate desc;
go

select 
	top (5) OrderID, OrderDate
from dbo.Orders;
go

--انتخاب جدیدتری پنج سفارش ثبت شده با در نظر گرفتن ساید مقادیر برابر
select 
	top (5) with ties OrderID, OrderDate, CustomerID, EmployeeID
from dbo.Orders
order by OrderDate desc;
go


select 
	OrderID, OrderDate, CustomerID, EmployeeID
from dbo.Orders
order by OrderDate desc
offset 0 row fetch next 10 row only;
go

select 
	OrderID, OrderDate, CustomerID, EmployeeID
from dbo.Orders
order by OrderDate desc
offset 10 row fetch next 5 row only;
go

select 
	OrderID, OrderDate, CustomerID, EmployeeID
from dbo.Orders
order by OrderDate desc, OrderID desc
offset 10 row;
go

select
	CustomerID, State, Region, City
from dbo.Customers
	where Region = N'جنوب';
go

select
	CustomerID, State, Region, City
from dbo.Customers
	where Region <> N'جنوب';
go

--عدم تاثیر روی مقادیر unknown
select
	CustomerID, State, Region, City
from dbo.Customers
	where Region = NULL;
go

select
	CustomerID, State, Region, City
from dbo.Customers
	where Region is null;
go

select
	CustomerID, State, Region, City
from dbo.Customers
	where Region <> N'جنوب' or Region is null;
go

declare @str1 varchar(100) = null;
select ISNULL(@str1,'NULL Value');
go

select
	CustomerID, State, Region, City
from dbo.Customers
	where ISNULL(Region,'') <> N'جنوب' ;
go

-- Reject False
drop table if exists ChkConstraint;
go

create table ChkConstraint
(
	ID		int not null identity,
	family  nvarchar(100),
	score	int constraint CHK_Positive1 check(score >= 0)
);
go
-- پذیرش مقدار True
insert into dbo.ChkConstraint(family, score)
	values (N'سعیدی',100);
go

-- پذیرش مقدار null
insert into dbo.ChkConstraint(family)
	values (N'پرتوی');
go

--عدم پذیرش مقدار False
insert into dbo.ChkConstraint(family)
	values (N'احمدی',-10);
go

select
	OrderID,
	YEAR(OrderDate) as OrderYear,
	YEAR(OrderDate) + 1 as NextYear
from dbo.Orders;
go

-- searched case
select
	CustomerID,
	case
		when Region IS null then N'فاقد موقعیت'
		else Region
	end as case_value
from dbo.Customers


select 
	ProductID, ProductName, CategoryID
from dbo.Products;
go

--simple case در این حالت بلافاصله بعد از کیس اسم فیلد را میاریم
select
	ProductID, ProductName, CategoryID,
	case CategoryID
		when 1 then N'نوشیدنی'
		when 2 then N'ادویه جات'
		when 3 then N'مربا'
		when 4 then N'محصولات لبنی'
		when 5 then N'حبوبات'
		when 6 then N'گوشت و مرغ'
		when 7 then N'ارگانیک'
		when 8 then N'دریایی'
		else N'متفرقه'
	end as CategoryName
from dbo.Products
order by CategoryName;
go

select 
	ProductID, UnitPrice
from dbo.OrderDetails;
go

-- searched case
select
	ProductID, UnitPrice,
	case
		when UnitPrice < 50 then N'کمتر از 50'
		when UnitPrice between 50 and 100 then N'بین 50 تا 100'
		when UnitPrice > 100 then N'بیشتر از 100'
	else N'نامشخص'
	end as UnitPriceCategory
from dbo.OrderDetails
order by UnitPrice;
go

select
	EmployeeID, FirstName, TitleofCourtesy,
	case
--		when TitleofCourtesy = 'Ms.' then 'Female'
--		when TitleofCourtesy = 'Mrs.' then 'Female'
		when TitleofCourtesy in ('Ms.', 'Mrs.') then 'Female'
		when TitleofCourtesy = 'Mr.' then 'Male'
		else N'نامشخص'
	end as Gender
from dbo.Employees;
go

-- 
select 
	City,
	case City
		when N'تهران'	then N'پایتخت'
	end as N'نوع شهر'
from dbo.Customers;
go

select
	CustomerID, Region
from dbo.Customers
order by
	case when Region IS NULL then 1 else 0 end, Region;
go

select
	CustomerID, Region
from dbo.Customers
order by
	case when Region IS NULL then 1 else 0 end, Region, CustomerID DESC;
go

select
	distinct EmployeeID, CustomerID
from dbo.Orders
order by EmployeeID,CustomerID;
go

select
	EmployeeID, CustomerID
from dbo.Orders
group by EmployeeID, CustomerID;
go

