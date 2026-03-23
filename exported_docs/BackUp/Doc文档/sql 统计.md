

```sql
SELECT table_name,create_time,UPDATE_TIME ,TABLE_ROWS ,table_comment,TABLE_SCHEMA ,CHECK_TIME FROM information_schema.TABLES
where table_schema = 'outway'  order by  TABLE_ROWS desc ;

SELECT table_name,create_time,UPDATE_TIME ,TABLE_ROWS ,table_comment,TABLE_SCHEMA ,CHECK_TIME FROM information_schema.TABLES
where table_schema = 'outway'  order by  CREATE_TIME desc ;

select * from (SELECT table_name,create_time,UPDATE_TIME ,TABLE_ROWS ,table_comment,TABLE_SCHEMA ,CHECK_TIME FROM information_schema.TABLES
where table_schema = 'outway' ) a where TABLE_NAME like '%task%' or TABLE_NAME like '%job%' order by  create_time desc;

# 查询字段 ks_sync_task  ks_sync_sub_task
select COLUMN_NAME,
       COLUMN_COMMENT,
       (CASE WHEN DATA_TYPE = 'bigint' THEN 'int' WHEN DATA_TYPE = 'tinyint' THEN 'int' WHEN DATA_TYPE = 'timestamp' THEN 'datetime' WHEN DATA_TYPE = 'int' THEN 'int' WHEN DATA_TYPE = 'varchar' THEN 'varchar' WHEN DATA_TYPE = 'datetime' THEN 'datetime' END) AS DATA_TYPE,
        IS_NULLABLE,
        COLUMN_DEFAULT from information_schema.COLUMNS
where TABLE_NAME = 'ks_sync_task' and TABLE_SCHEMA = 'outway'  and COLUMN_NAME not in ('id','creator','gmt_create','gmt_modified','is_deleted','modifier') order by COLUMN_NAME;

select COLUMN_NAME,
       COLUMN_COMMENT,
       (CASE WHEN DATA_TYPE = 'bigint' THEN 'int' WHEN DATA_TYPE = 'tinyint' THEN 'int' WHEN DATA_TYPE = 'timestamp' THEN 'datetime' WHEN DATA_TYPE = 'int' THEN 'int' WHEN DATA_TYPE = 'varchar' THEN 'varchar' WHEN DATA_TYPE = 'datetime' THEN 'datetime' END) AS DATA_TYPE,
        IS_NULLABLE,
        COLUMN_DEFAULT from information_schema.COLUMNS
where TABLE_NAME = 'ks_sync_sub_task' and TABLE_SCHEMA = 'outway'  and COLUMN_NAME not in ('id','creator','gmt_create','gmt_modified','is_deleted','modifier') order by COLUMN_NAME;



# 取交集
select a.* from (select COLUMN_NAME,
       COLUMN_COMMENT,
       (CASE WHEN DATA_TYPE = 'bigint' THEN 'int' WHEN DATA_TYPE = 'tinyint' THEN 'int' WHEN DATA_TYPE = 'timestamp' THEN 'datetime' WHEN DATA_TYPE = 'int' THEN 'int' WHEN DATA_TYPE = 'varchar' THEN 'varchar' WHEN DATA_TYPE = 'datetime' THEN 'datetime' END) AS DATA_TYPE,
        IS_NULLABLE,
        COLUMN_DEFAULT from information_schema.COLUMNS
where TABLE_NAME = 'ks_sync_task' and TABLE_SCHEMA = 'outway'  and COLUMN_NAME not in ('id','creator','gmt_create','gmt_modified','is_deleted','modifier') order by DATA_TYPE) as a inner join (select COLUMN_NAME,
       COLUMN_COMMENT,
       (CASE WHEN DATA_TYPE = 'bigint' THEN 'int' WHEN DATA_TYPE = 'tinyint' THEN 'int' WHEN DATA_TYPE = 'timestamp' THEN 'datetime' WHEN DATA_TYPE = 'int' THEN 'int' WHEN DATA_TYPE = 'varchar' THEN 'varchar' WHEN DATA_TYPE = 'datetime' THEN 'datetime' END) AS DATA_TYPE,
        IS_NULLABLE,
        COLUMN_DEFAULT from information_schema.COLUMNS
where TABLE_NAME = 'ks_sync_sub_task' and TABLE_SCHEMA = 'outway'  and COLUMN_NAME not in ('id','creator','gmt_create','gmt_modified','is_deleted','modifier') order by DATA_TYPE) as b on a.COLUMN_NAME = b.COLUMN_NAME;


# 查询字段： sync_data_task
select COLUMN_NAME,
       COLUMN_COMMENT,
       (CASE WHEN DATA_TYPE = 'bigint' THEN 'int' WHEN DATA_TYPE = 'tinyint' THEN 'int' WHEN DATA_TYPE = 'timestamp' THEN 'datetime' WHEN DATA_TYPE = 'int' THEN 'int' WHEN DATA_TYPE = 'varchar' THEN 'varchar' WHEN DATA_TYPE = 'datetime' THEN 'datetime' END) AS DATA_TYPE,
        IS_NULLABLE,
        COLUMN_DEFAULT from information_schema.COLUMNS
where TABLE_NAME = 'sync_data_task' and TABLE_SCHEMA = 'outway'  and COLUMN_NAME not in ('id','creator','gmt_create','gmt_modified','is_deleted','modifier') order by DATA_TYPE;

# 查询字段： sync_task_job
select COLUMN_NAME,
       COLUMN_COMMENT,
       (CASE WHEN DATA_TYPE = 'bigint' THEN 'int' WHEN DATA_TYPE = 'tinyint' THEN 'int' WHEN DATA_TYPE = 'timestamp' THEN 'datetime' WHEN DATA_TYPE = 'int' THEN 'int' WHEN DATA_TYPE = 'varchar' THEN 'varchar' WHEN DATA_TYPE = 'datetime' THEN 'datetime' END) AS DATA_TYPE,
        IS_NULLABLE,
        COLUMN_DEFAULT from information_schema.COLUMNS
where TABLE_NAME = 'sync_task_job' and TABLE_SCHEMA = 'outway'  and COLUMN_NAME not in ('id','creator','gmt_create','gmt_modified','is_deleted','modifier') order by DATA_TYPE;


# 查询字段： sync_job
select COLUMN_NAME,
       COLUMN_COMMENT,
       (CASE WHEN DATA_TYPE = 'bigint' THEN 'int' WHEN DATA_TYPE = 'tinyint' THEN 'int' WHEN DATA_TYPE = 'timestamp' THEN 'datetime' WHEN DATA_TYPE = 'int' THEN 'int' WHEN DATA_TYPE = 'varchar' THEN 'varchar' WHEN DATA_TYPE = 'datetime' THEN 'datetime' END) AS DATA_TYPE,
        IS_NULLABLE,
        COLUMN_DEFAULT from information_schema.COLUMNS
where TABLE_NAME = 'sync_job' and TABLE_SCHEMA = 'outway'  and COLUMN_NAME not in ('id','creator','gmt_create','gmt_modified','is_deleted','modifier') order by DATA_TYPE;

# 查询字段： item_sync_task
select COLUMN_NAME,
       COLUMN_COMMENT,
       (CASE WHEN DATA_TYPE = 'bigint' THEN 'int' WHEN DATA_TYPE = 'tinyint' THEN 'int' WHEN DATA_TYPE = 'timestamp' THEN 'datetime' WHEN DATA_TYPE = 'int' THEN 'int' WHEN DATA_TYPE = 'varchar' THEN 'varchar' WHEN DATA_TYPE = 'datetime' THEN 'datetime' END) AS DATA_TYPE,
        IS_NULLABLE,
        COLUMN_DEFAULT from information_schema.COLUMNS
where TABLE_NAME = 'item_sync_task' and TABLE_SCHEMA = 'outway'  and COLUMN_NAME not in ('id','creator','gmt_create','gmt_modified','is_deleted','modifier') order by DATA_TYPE;


# 查询字段： ks_cps_comment_task
select COLUMN_NAME,
       COLUMN_COMMENT,
       (CASE WHEN DATA_TYPE = 'bigint' THEN 'int' WHEN DATA_TYPE = 'tinyint' THEN 'int' WHEN DATA_TYPE = 'timestamp' THEN 'datetime' WHEN DATA_TYPE = 'int' THEN 'int' WHEN DATA_TYPE = 'varchar' THEN 'varchar' WHEN DATA_TYPE = 'datetime' THEN 'datetime' END) AS DATA_TYPE,
        IS_NULLABLE,
        COLUMN_DEFAULT from information_schema.COLUMNS
where TABLE_NAME = 'ks_cps_comment_task' and TABLE_SCHEMA = 'outway'  and COLUMN_NAME not in ('id','creator','gmt_create','gmt_modified','is_deleted','modifier') order by DATA_TYPE;


# 测试用的
select COLUMN_NAME,
       COLUMN_COMMENT,
       (CASE WHEN DATA_TYPE = 'bigint' THEN 'int' WHEN DATA_TYPE = 'tinyint' THEN 'int' WHEN DATA_TYPE = 'timestamp' THEN 'datetime' WHEN DATA_TYPE = 'int' THEN 'int' WHEN DATA_TYPE = 'varchar' THEN 'varchar' WHEN DATA_TYPE = 'datetime' THEN 'datetime' END) AS DATA_TYPE,
        IS_NULLABLE,
        COLUMN_DEFAULT from information_schema.COLUMNS
        where TABLE_NAME = 'ks_sync_sub_task'
          and TABLE_SCHEMA = 'outway'
          and COLUMN_NAME not in ('id','creator','gmt_create','gmt_modified','is_deleted','modifier')
        order by DATA_TYPE;


select * from sync_job ;
```

