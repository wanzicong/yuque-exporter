修改表结构



店铺表

```sql
alter table item_shop
    add shop_grade_status tinyint null comment '店铺等级状态 0-未审核 1-审核中 2-已通过 3-未通过';

alter table item_shop
    add shop_grade tinyint null comment '店铺等级 ：0 旗舰店、1 专营店、2 专卖店、3 卖场型旗舰店、4 普通企业店铺';

alter table item_shop
    add upload_certificate varchar(1024) null comment '店铺等级资质资料';

alter table item_shop
    add shop_grade_sender varchar(64) null comment '店铺审核发起人';

alter table item_shop
    add shop_grade_send_time timestamp null comment '店铺等级上传时间';
```



资质表

```sql
alter table qualification_style_record
    add want_cooperate_anchors varchar(256) null comment '合作意向主播列表';


```



新增表结构



店铺审核记录表

```sql
create table item_shop_grade_audit
(
    id           bigint unsigned auto_increment comment '主键ID'
        primary key,
    gmt_create   timestamp default CURRENT_TIMESTAMP not null comment '创建时间',
    gmt_modified timestamp default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP comment '修改时间',
    creator      varchar(32)                         not null comment '创建人',
    modifier     varchar(32)                         not null comment '修改人',
    is_deleted   tinyint   default 0                 not null comment '是否删除：1(删除) 0(未删除)',
    shop_id      bigint                              null comment '店铺ID',
    submitter    varchar(32)                         null comment '提交人idauditor',
    auditor      varchar(32)                         null comment '审核人',
    audit_result tinyint                             null comment '审核结果 1通过 2不通过',
    audit_time   datetime                            null comment '审核时间',
    turn_reason  varchar(256)                        null comment '驳回原因'
)
    comment '店铺等级审核记录表';

```



资质绑定记录表

```sql

create table qualification_style_change
(
    id                   bigint unsigned auto_increment comment '主键ID'
        primary key,
    gmt_create           timestamp default CURRENT_TIMESTAMP not null comment '创建时间',
    gmt_modified         timestamp default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP comment '修改时间',
    creator              varchar(32)                         not null comment '创建人',
    modifier             varchar(32)                         not null comment '修改人',
    is_deleted           tinyint   default 0                 not null comment '是否删除：1(删除) 0(未删除)',
    record_id            varchar(128)                        null comment '记录id',
    style_code           varchar(128)                        null comment '样式id',
    before_anchors       varchar(256)                        null comment '变更前主播信息',
    after_anchors        varchar(256)                        null comment '变更后主播信息',
    change_date          timestamp                           null comment '变更时间',
    change_status        tinyint   default 1                 not null comment '变更状态 1 待处理 2 已处理',
    qualification_status varchar(64)                         null comment '资质审核状态',
    confirmor            varchar(64)                         null comment '确认人',
    confirm_time         timestamp                           null comment '确认时间'
)
    comment '款式合作意向主播变更记录表';


```



代码merge : [https://gitlab.xinc818.com/item/itemcenter/-/merge_requests/834](https://gitlab.xinc818.com/item/itemcenter/-/merge_requests/834)  to gray









