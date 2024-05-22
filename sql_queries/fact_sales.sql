if not exists (select * from sys.tables where name = 'fact_sales')
create table fact_sales(
    date date not null,
    time time not null,
    item_code bigint not null,
    quantity_sold float not null,
    unit_selling_price float not null,
    sale_or_return varchar(10) not null,
    discount varchar(3) not null,
    pk_sale int identity(1,1) primary key
);