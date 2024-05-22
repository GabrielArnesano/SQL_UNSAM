if not exists (select * from information_schema.tables where table_name = 'dim_item') 
create table dim_item (
    item_code bigint primary key not null,
    item_name varchar(300) not null,
);