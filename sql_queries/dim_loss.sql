if not exists (select 1 from sys.tables where name = 'dim_loss')
create table dim_loss(
    item_code bigint not null,
    item_name varchar(300) null,
    loss_rate float null
);