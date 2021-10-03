create database liquors_castle4;
use liquors_castle4;

create table Suppliers (
  Supplier_id VARCHAR(50) UNIQUE NOT NULL,
 Name VARCHAR(50) NOT NULL,
 Surname VARCHAR(50),
 Aadhar_No CHAR(12) UNIQUE NOT NULL,
 Licence_No VARCHAR(50) UNIQUE NOT NULL,
 Owner_address VARCHAR(50) NOT NULL,
	 Shop_address VARCHAR(50) NOT NULL,
 Contact_No VARCHAR(10) UNIQUE NOT NULL,
 email VARCHAR(50) UNIQUE NOT NULL,
 City_Serveable VARCHAR(50) NOT NULL,
 password VARCHAR(50) NOT NULL,
 PRIMARY KEY(Supplier_id)
);

create index supplierID_i on Suppliers(Supplier_id);
create index supplierName_i on Suppliers(Name);

insert into Suppliers (Supplier_id, Name, Surname, Aadhar_No, Licence_No, Owner_address, Shop_address, Contact_No, email, City_Serveable, password) values ('1000', 'Merry', 'Kenningham', '543645676781', '22-7856580', '1152 Algoma Alley', '1 Karol Bagh', '7801753624', 'mkenningham0@multiply.com', 'Rust’avi','abc');
insert into Suppliers (Supplier_id, Name, Surname, Aadhar_No, Licence_No, Owner_address, Shop_address, Contact_No, email, City_Serveable, password) values (1001, 'Carlotta', 'Creber', '873645676781', '07-3368701', '5313 Logan Road', '2 Karol Bagh', '8292639898', 'ccreber1@flavors.me', 'Soras','bcd');
insert into Suppliers (Supplier_id, Name, Surname, Aadhar_No, Licence_No, Owner_address, Shop_address, Contact_No, email, City_Serveable, password) values (1002, 'Talia', 'Felgate', '987645676781', '00-5337482', '5 Cambridge Street', '3 Karol Bagh', '6081903769', 'tfelgate2@apple.com', 'Sandouping','bdd');
insert into Suppliers (Supplier_id, Name, Surname, Aadhar_No, Licence_No, Owner_address, Shop_address, Contact_No, email, City_Serveable, password) values (1003, 'Ginger', 'Avrashin', '879645676781', '10-1480536', '979 Swallow Hill', '4 Karol Bagh', '4391704148', 'gavrashin3@csmonitor.com', 'Bayan-Ovoo','jdnkjd');

 create table Item (
 item_id VARCHAR(50),
 Name varchar(20),
 Item_type varchar(20),
 Supplier_id VARCHAR(50),
 Item_available_status VARCHAR(50),
 Places_item_available VARCHAR(50),
 Price  INT,
 Image VARCHAR(200),

 PRIMARY KEY (`item_id`),

 foreign key(Supplier_id) references Suppliers(Supplier_id)
);

create index name_i on Item(Name);
create index type_i on Item(item_type);





insert into Item (item_id, Name, Item_type, Supplier_id, Item_available_status, Places_item_available, Price ,Image) values ('80-8120408', 'Rammstien', 'Rum', '1000', 'Available', 'Delhi', 1995,'https://shop.rammstein.de/img/katalog/1617/2048/flasche-rum-null-1.jpg');
insert into Item (item_id, Name, Item_type, Supplier_id, Item_available_status, Places_item_available, Price ,Image) values ('63-1435626', 'Bombay Saphire', 'Dry Gin', '1002', 'Available', 'Rajasthan', 1802,'https://products0.imgix.drizly.com/ci-bombay-sapphire-4967085f606d9efa.jpeg?auto=format%2Ccompress&fm=jpg&q=20');
insert into Item (item_id, Name, Item_type, Supplier_id, Item_available_status, Places_item_available, Price ,Image) values ('44-2094172', 'Jose Cuervo','Tequila', '1003', 'Available', 'Haryana', 224,'https://products0.imgix.drizly.com/ci-jose-cuervo-especial-silver-tequila-b4511db8b8f76297.png?auto=format%2Ccompress&fm=jpg&q=20');



create table Customer (
 Customer_id VARCHAR(50) UNIQUE NOT NULL,
 Customer_name VARCHAR(50) NOT NULL,
 Surname VARCHAR(50),
 email VARCHAR(50) UNIQUE NOT NULL,
 DOB DATE NOT NULL,
 state VARCHAR(50) NOT NULL,
 city VARCHAR(50) NOT NULL,
 address VARCHAR(50) NOT NULL,
 delivery_Phone_no VARCHAR(10) UNIQUE NOT NULL,
 pass_word VARCHAR(50) NOT NULL,
 aadhar_no CHAR(12) NOT NULL UNIQUE,
 PRIMARY KEY(Customer_id)
);
create index CustomerName_i on Customer(Customer_name);
create index CustomerID_i on Customer(Customer_id);
insert into Customer (Customer_id, Customer_name, Surname, email, DOB, state, city, address, delivery_Phone_no, pass_word, aadhar_no) values ('100001', 'Kaiman', 'Yadav', 'yadavkaiman@gmail.com', '1990-12-22', 'Delhi', 'Girsereng', '598 Delladonna Avenue', '9900887766', 'qWs9ClCt', '543232123456');
insert into Customer (Customer_id, Customer_name, Surname, email, DOB, state, city, address, delivery_Phone_no, pass_word, aadhar_no) values ('100002', 'Ankit', 'McGlaud', 'Mcglaudankit@gmail.com', '1991-12-22', 'Ontario', 'North Bay', '46 Vidon Trail', '9876543211', 'vmM2rH4skpa', '675868569565');
insert into Customer (Customer_id, Customer_name, Surname, email, DOB, state, city, address, delivery_Phone_no, pass_word, aadhar_no) values ('100003', 'Yashraj', 'Alchin', 'alchinyashraj@gmail.com', '1989-12-22', 'Mumbai', 'Zherdevka', '23854 Boyd Drive', '9878987898', 'y6L5lYb8', '324354678798');







create table add_to_cart (

item_id varchar(50),
Customer_id VARCHAR(50),
Primary key(item_id),
FOREIGN KEY(item_id) REFERENCES Item(item_id),
 Foreign key(Customer_id) REFERENCES Customer(Customer_id)
);




Create table discounttypes(
 Discounttype varchar(10),
 Discount int,
 Primary key(Discounttype)
);
create index discountpercent_i on discounttypes(Discount);
insert into discounttypes (Discounttype,Discount) values ('a',10);
insert into discounttypes (Discounttype,Discount) values ('b',10);
insert into discounttypes (Discounttype,Discount) values ('c',10);
create index percent_i on discounttypes(Discount);

create table Deals (
 Deal_ID VARCHAR(50),
 item_id VARCHAR(50) NOT NULL ,
 Discounttype varchar(10) ,
	PRIMARY KEY (Deal_ID,item_Id),
	FOREIGN KEY(item_id) REFERENCES Item(item_id) ON update cascade ON delete cascade,
FOREIGN KEY(Discounttype) REFERENCES discounttypes(Discounttype) ON update cascade ON delete cascade
	
);

insert into Deals (Deal_ID, item_id, Discounttype) values ('2T3BFRE', '44-2094172', 'a');
insert into Deals (Deal_ID, item_id, Discounttype) values ('1GYFK668', '63-1435626', 'b');
insert into Deals (Deal_ID, item_id, Discounttype) values ('WBAKB0C', '80-8120408', 'c');



create table Transaction (
 transaction_id INT NOT NULL AUTO_INCREMENT,
Customer_id VARCHAR(50) NOT NULL,
 account_id varchar(20),
 item_id VARCHAR(50) not null,
 transacted_money VARCHAR(50) not null,
 transaction_time VARCHAR(50) not null,
 transaction_date DATE,
 payment_mode varchar(30) not null,
 
	PRIMARY KEY (transaction_id,account_id),
	FOREIGN KEY(item_id) REFERENCES Item(item_id) on update cascade,
FOREIGN KEY(Customer_id) REFERENCES Customer(Customer_id) on update cascade

	);

create table accounts(
 account_id varchar(20),
 Customer_id VARCHAR(50),
 primary key(account_id),
 foreign key(customer_id) references customer(customer_id)
);

create index accounts_id on accounts(account_id);


create trigger cust_acc
after INSERT 
on Transaction
for each row 
insert into accounts (account_id,Customer_id) values (NEW.account_id ,NEW.Customer_id);

insert into Transaction (Customer_id, item_id, transacted_money, transaction_time, transaction_date,payment_mode,account_id) values ( '100001','80-8120408', '1656.75', '10:46 AM', '1978-11-01','paytm','123456');
insert into Transaction (Customer_id, item_id,transacted_money, transaction_time, transaction_date,payment_mode,account_id) values ( '100002', '63-1435626', '19317.08', '9:46 AM', '1978-11-02','debitcard','123457');
insert into Transaction (Customer_id, item_id, transacted_money, transaction_time, transaction_date,payment_mode,account_id) values ( '100003','44-2094172', '5472.95', '9:42 AM', '1978-11-03','creditcard','123458');


create table Order1 (
 Order_id INT UNIQUE NOT NULL AUTO_INCREMENT,
 item_id VARCHAR(50) NOT NULL,
 Customer_id VARCHAR(50) NOT NULL,
 Quantity INT ,
 Contact_No VARCHAR(50) NOT NULL,
 Order_date DATE NOT NULL,
 Delivery_address VARCHAR(50) NOT NULL,
 PRIMARY KEY(Order_id,Customer_id),
 
 FOREIGN KEY(item_id) REFERENCES Item(item_id),
 
 FOREIGN KEY(Customer_id) REFERENCES Customer(Customer_id)
 
);
create index OrderID_i on Order1(Order_id);
create index OrderDate_i on Order1(Order_date);
create table Order_Status (
 Order_id INT,
 take_date DATE NOT NULL  ,
status boolean,
duedate_gone Boolean,

 PRIMARY KEY(Order_id),


 FOREIGN KEY(Order_id) REFERENCES Order1(Order_id) ON update cascade
	
);



create trigger order_up	
after INSERT 
on Order1
for each row 
insert into Order_Status (Order_id, take_date ,status,duedate_gone) values (NEW.Order_id,( NEW.Order_date + 2 ),false,false);








insert into Order1 (Order_id, item_id, Customer_id, Quantity, Contact_No, Order_date, Delivery_address) values ('1000000', '44-2094172', '100001', 2, '2142169709', '2020-01-12', '342 Dottie Center');
insert into Order1 (Order_id, item_id, Customer_id, Quantity, Contact_No, Order_date, Delivery_address) values ('1000001', '63-1435626', '100002',  4, '6863806243', '2020-01-13', '4 Michigan Plaza');




create table Rejected_Order (
 Order_id  VARCHAR(50) UNIQUE NOT NULL,
 Item_ID VARCHAR(50) NOT NULL,
Customer_id VARCHAR(50) NOT NULL,
reason varchar(30) NOT NULL,
 
	 
 PRIMARY KEY(Order_id),
foreign key(Customer_id) REFERENCES Customer(Customer_id) on delete cascade,
 FOREIGN KEY(Item_id) REFERENCES Item(Item_id) on delete cascade
 
);


create index RejectedOrderItem_i on Rejected_Order(Item_id);
create index RejectedOrder_i on Rejected_Order(Order_id);
insert into Rejected_Order (Order_id, Item_id, Customer_id,reason) values ('JA32U2FUXDU044717', '44-2094172', '100001','wkeijnr');




