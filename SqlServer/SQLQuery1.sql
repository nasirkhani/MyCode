﻿use NikamoozDB;
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

