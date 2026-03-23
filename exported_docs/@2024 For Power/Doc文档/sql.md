

```plain
CREATE TABLE IF NOT EXISTS jnpf_industry.`mall_order_refund_reply` (
  `F_Id` BIGINT NOT NULL COMMENT '主键id',
  `F_EnabledMark` INT DEFAULT NULL COMMENT '禁用启用',
  `F_Description` VARCHAR(255) DEFAULT NULL COMMENT '描述或说明',
  `F_CREATORTIME` DATETIME DEFAULT NULL COMMENT '创建时间',
  `F_CREATORUSERID` VARCHAR(50) DEFAULT NULL COMMENT '创建用户ID',
  `F_CreatorUserName` VARCHAR(50) DEFAULT NULL COMMENT '创建用户名字',
  `F_LASTMODIFYTIME` DATETIME DEFAULT NULL COMMENT '修改时间',
  `F_LastModifyUserName` VARCHAR(50) DEFAULT NULL COMMENT '修改用户名称',
  `F_LASTMODIFYUSERID` VARCHAR(50) DEFAULT NULL COMMENT '修改用户',
  `F_DELETEMARK` INT DEFAULT NULL COMMENT '删除标志',
  `F_DELETETIME` DATETIME DEFAULT NULL COMMENT '删除时间',
  `F_DELETEUSERID` VARCHAR(50) DEFAULT NULL COMMENT '删除用户',
  `F_Version` INT DEFAULT 0 COMMENT '表设计版本号',
  `F_OrganizeId` VARCHAR(50) DEFAULT NULL COMMENT '组织ID',
  `F_OrderId` BIGINT DEFAULT NULL COMMENT '订单ID',
  `F_OrderNo` VARCHAR(100) DEFAULT NULL COMMENT '订单号',
  `F_MerchantId` BIGINT DEFAULT NULL COMMENT '商家ID',
  `F_OrderDetailId` BIGINT DEFAULT NULL COMMENT '订单明细ID',
  `F_RefundReason` VARCHAR(255) DEFAULT NULL COMMENT '退款原因',
  `F_Phone` VARCHAR(20) DEFAULT NULL COMMENT '联系电话',
  `F_RefundAmount` DECIMAL(18,2) DEFAULT NULL COMMENT '退款金额',
  `F_AuditStatus` INT DEFAULT NULL COMMENT '审批状态 [1：申请退款；2：商家受理中；3：退款成功，4 取消退款，5 受理成功，6 受理拒绝]',
  `F_AuditContent` VARCHAR(255) DEFAULT NULL COMMENT '审批描述',
  `F_AuditUserId` VARCHAR(50) DEFAULT NULL COMMENT '审批操作人ID',
  `F_AuditUserName` VARCHAR(50) DEFAULT NULL COMMENT '审批操作人名称',
  `F_ApplyTime` DATETIME DEFAULT NULL COMMENT '申请时间',
  `F_AuditTime` DATETIME DEFAULT NULL COMMENT '审批时间',
  `F_RefundTime` DATETIME DEFAULT NULL COMMENT '退款时间',
  `F_MallBaseTemplateRespJson` TEXT COMMENT '商品模板配置JSON',
  PRIMARY KEY (`F_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='退款用户申请';
```





```python
alter table mall_order
    add F_RefundStatus int(9) null comment '退款状态';

--- 财务
alter table finance_refund_main
    add F_ErrorDesc varchar(128) null comment '订单异常信息';


```





```python
alter table mall_base_template
    add F_OnlineRefundTimeLimit int null comment '预订开始时间前多少分钟可线上退款';

alter table mall_base_template
    add F_AutoAcceptRefund int(10) null comment '是否自动受理';

alter table mall_base_template
    add F_AutoAuditProcess int(10) null comment '是否自动通过';

alter table mall_base_template
    add F_AutoInitiateRefund int(10) null comment '是否自动发起退款';

```











