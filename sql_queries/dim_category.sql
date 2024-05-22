if not exists (select 1 from information_schema.tables where table_name = 'dim_category') 
create table dim_category (
    category_code bigint primary key not null,
    category_name varchar(300) not null,
);