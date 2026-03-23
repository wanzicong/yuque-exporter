



```plain
-- auto-generated definition
create table cps_remark_record
(
    id               bigint unsigned auto_increment comment '主键id'
        primary key,
    gmt_create       timestamp default CURRENT_TIMESTAMP not null comment '创建时间',
    gmt_modified     timestamp default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP comment '修改时间',
    creator          varchar(32)                         not null comment '创建人',
    modifier         varchar(32)                         not null comment '修改人',
    is_deleted       tinyint   default 0                 not null comment '是否删除：0-未删除,1-删除',
    seq_code         varchar(128)                        not null comment '直播清单seq_code',
    remark_type_name varchar(128)                        not null comment '自由备注类型名字',
    remark_type_id   varchar(128)                        not null comment '自由备注类型id',
    modifier_name    varchar(64)                         not null comment '更新人名字',
    content_type     varchar(32)                         not null comment '备注内容类型 1:文字 2:图片',
    word_des         varchar(1024)                        null comment '文字内容描述',
    picture_des      varchar(256)                        null comment '图片内容描述'
)
    comment '自由备注记录表';

-- auto-generated definition
create table cps_remark_type
(
    id           bigint unsigned auto_increment comment '主键id'
        primary key,
    gmt_create   timestamp default CURRENT_TIMESTAMP not null comment '创建时间',
    gmt_modified timestamp default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP comment '修改时间',
    creator      varchar(32)                         not null comment '创建人',
    modifier     varchar(32)                         not null comment '修改人',
    is_deleted   tinyint   default 0                 not null comment '是否删除：0-未删除,1-删除',
    live_plan_id varchar(128)                        not null comment '直播场次id',
    remark_type  varchar(128)                        not null comment '自由备注类型'
)
    comment '自由备注类型';

create table cps_remark_record_log
(
    id               bigint unsigned auto_increment comment '主键id'
        primary key,
    gmt_create       timestamp default CURRENT_TIMESTAMP not null comment '创建时间',
    gmt_modified     timestamp default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP comment '修改时间',
    creator          varchar(32)                         not null comment '创建人',
    modifier         varchar(32)                         not null comment '修改人',
    is_deleted       tinyint   default 0                 not null comment '是否删除：0-未删除,1-删除',
    record_id        varchar(128)                        not null comment '备注记录id',
    operator         varchar(64)                         not null comment '操作人',
    operate_des      varchar(1024)                        null comment '操作内容',
    remark_type_name varchar(128)                        not null comment '备注类型',
    operate_source   varchar(32)                         null comment '操作来源 1 excel 2 手动操作',
    operate_type     varchar(32)                         null comment '操作类型',
    seq_code         varchar(64)                         not null comment '直播清单商品code'
)
    comment '自由备注记录日志表';










```





