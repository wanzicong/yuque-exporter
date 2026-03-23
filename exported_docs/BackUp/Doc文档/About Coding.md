# 发现隐藏bug
com/vip8/customermanage/service/impl/CashBackBizServiceImpl.java:542 【因该是update 不是save】





# 辛喜对接dubbo
【辛喜查询返款计划】com.vip8.customermanage.service.impl.feedback.OrderCashBackServiceImpl#queryCashBackInfo 





# 程序对应的入口/HTTP/Dubbo
OrderItemService.java

OrderCashBackService.java

AppealBackService.java

FeedBackPlanController.java

FeedBackOrderController.java

FeedBackLogController.java

FeedCashBackImportController.java

FeedBackCashBackController.java

FeedBackAppealController.java



## <font style="color:#DF2A3F;">返款申请单</font>
<font style="color:#080808;background-color:#ffffff;">FeedBackCashBackController</font>

1. <font style="color:#080808;background-color:#ffffff;">【创建返款申请】com.vip8.customermanage.web.controller.feedback.cash.back.FeedBackCashBackController#create</font>
2. <font style="color:#080808;background-color:#ffffff;">【关闭返款计划】com.vip8.customermanage.web.controller.feedback.cash.back.FeedBackCashBackController#close</font>
3. <font style="color:#080808;background-color:#ffffff;">【风控同意】com.vip8.customermanage.web.controller.feedback.cash.back.FeedBackCashBackController#examine</font>
4. <font style="color:#080808;background-color:#ffffff;">【校验是否用户信息】com.vip8.customermanage.web.controller.feedback.cash.back.FeedBackCashBackController#checkMobile</font>

<font style="color:#080808;background-color:#ffffff;">FeedCashBackImportController【导入返款计划】</font>

1. <font style="color:#080808;background-color:#ffffff;">【批量创建/导入】com.vip8.customermanage.web.controller.feedback.cash.back.FeedCashBackImportController#batchImport</font>
2. <font style="color:#080808;background-color:#ffffff;">【批量关单/导入】com.vip8.customermanage.web.controller.feedback.cash.back.FeedCashBackImportController#batchOfflinePayment</font>

<font style="color:#080808;background-color:#ffffff;">OrderCashBackService 【返款api】</font>

1. <font style="color:#080808;background-color:#ffffff;">【申请返款/辛喜用户】com.vip8.customermanage.api.service.feedback.OrderCashBackService#applyCashBack</font>
2. <font style="color:#080808;background-color:#ffffff;">【校验返款申请】com.vip8.customermanage.service.impl.feedback.OrderCashBackServiceImpl#checkCashBackApply</font>



## <font style="color:#DF2A3F;">返款申诉单</font>
<font style="color:#080808;background-color:#ffffff;">AppealBackService【申述api】</font>

1. <font style="color:#080808;background-color:#ffffff;">【创建申诉单】com.vip8.customermanage.api.service.feedback.AppealBackService#applyAppealBack</font>

<font style="color:#080808;background-color:#ffffff;">FeedBackAppealController【申诉单据客服】</font>

2. <font style="color:#080808;background-color:#ffffff;">【关闭申诉单据】com.vip8.customermanage.web.controller.feedback.appeal.FeedBackAppealController#create</font>



## 关键信息-处理申请单据
<font style="color:#080808;background-color:#ffffff;">liveCashBackRecordService.update</font>



# 返款单据核心日志记录Log


## 日志类型梳理
| 1、申请单 | **<font style="color:#117CEE;">用户提交返款/客服创建线上返款/客服创建线下返款/批量创建线下返款</font>** | |
| --- | :--- | --- |
| | **<font style="color:#117CEE;">直接关单-系统</font>** | |
| | **<font style="color:#117CEE;">直接关单-人工</font>** | |
| <br/>2、申诉<br/> | **<font style="color:#DF2A3F;">发起申诉</font>** | |
| | **<font style="color:#DF2A3F;">申诉处理-通过</font>** | |
| | **<font style="color:#DF2A3F;">申诉处理-拒绝</font>** | |
| 3、分控 | **<font style="color:rgb(23, 43, 77);">线上返款单过风控策略-风控通过</font>** | |
| | **<font style="color:rgb(23, 43, 77);">线上返款单过风控策略-风控不通过</font>** | |
| <br/>4、打款<br/> | <font style="color:#1DC0C9;">系统打款</font> | |
| | <font style="color:#1DC0C9;">打款失败</font> | |
| | <font style="color:#1DC0C9;">打款成功</font> | |
| | <font style="color:#1DC0C9;">线下打款</font> | |
| 5、售后 | <font style="color:rgb(255, 102, 0);">退款触发更新返款数量&金额</font> | |




## 原始产品日志场景
| **<font style="color:rgb(23, 43, 77);">场景</font>** | **<font style="color:rgb(23, 43, 77);">操作时间</font>** | **<font style="color:rgb(23, 43, 77);">操作人</font>** | **<font style="color:rgb(23, 43, 77);">操作类型</font>** | **<font style="color:rgb(23, 43, 77);">内容</font>** |
| :--- | :--- | :--- | :--- | :--- |
| <font style="color:rgb(23, 43, 77);">用户提交返款/客服创建线上返款/客服创建线下返款/批量创建线下返款</font> | <font style="color:rgb(23, 43, 77);">返款单创建时间</font> | <font style="color:rgb(23, 43, 77);">操作人</font> | <font style="color:rgb(23, 43, 77);">创建返款</font> | <font style="color:rgb(23, 43, 77);">   </font> |
| <font style="color:rgb(23, 43, 77);">线上返款单过风控策略-风控通过</font> | <font style="color:rgb(23, 43, 77);">风控校验时间</font> | <font style="color:rgb(23, 43, 77);">系统</font> | <font style="color:rgb(23, 43, 77);">风控通过</font> | <font style="color:rgb(23, 43, 77);">   </font> |
| <font style="color:rgb(23, 43, 77);">线上返款单过风控策略-风控不通过</font> | <font style="color:rgb(23, 43, 77);">风控校验时间</font> | <font style="color:rgb(23, 43, 77);">系统</font> | <font style="color:rgb(23, 43, 77);">风控不通过</font> | <font style="color:rgb(23, 43, 77);">不通过原因：xxx</font> |
| <font style="color:rgb(23, 43, 77);">系统打款</font> | <font style="color:rgb(23, 43, 77);">打款时间</font> | <font style="color:rgb(23, 43, 77);">系统</font> | <font style="color:rgb(23, 43, 77);">发起打款</font> | <font style="color:rgb(23, 43, 77);">   </font> |
| <font style="color:rgb(23, 43, 77);">打款失败</font> | <font style="color:rgb(23, 43, 77);">失败时间</font> | <font style="color:rgb(23, 43, 77);">系统</font> | <font style="color:rgb(23, 43, 77);">打款失败</font> | <font style="color:rgb(23, 43, 77);">打款失败原因：xxx</font> |
| <font style="color:rgb(23, 43, 77);">打款成功</font> | <font style="color:rgb(23, 43, 77);">成功时间</font> | <font style="color:rgb(23, 43, 77);">系统</font> | <font style="color:rgb(23, 43, 77);">打款成功</font> | <font style="color:rgb(23, 43, 77);">   </font> |
| <font style="color:rgb(23, 43, 77);">直接关单-人工</font> | <font style="color:rgb(23, 43, 77);">关单时间</font> | <font style="color:rgb(23, 43, 77);">操作人</font> | <font style="color:rgb(23, 43, 77);">直接关单</font> | <font style="color:rgb(23, 43, 77);">用户可见备注：xxx</font><br/><font style="color:rgb(23, 43, 77);">用户不可见备注：xxx</font> |
| <font style="color:rgb(23, 43, 77);">直接关单-系统</font> | <font style="color:rgb(23, 43, 77);">关单时间</font> | <font style="color:rgb(23, 43, 77);">系统</font> | <font style="color:rgb(23, 43, 77);">直接关单</font> | <font style="color:rgb(23, 43, 77);">用户可见备注：xxx</font><br/><font style="color:rgb(23, 43, 77);">用户不可见备注：xxx</font> |
| <font style="color:rgb(255, 102, 0);">退款触发更新返款数量&金额</font> | <font style="color:rgb(255, 102, 0);">触发时间</font> | <font style="color:rgb(255, 102, 0);">系统</font> | <font style="color:rgb(255, 102, 0);">更新返款</font> | <font style="color:rgb(255, 102, 0);">返款数量由a更新为b；</font><br/><font style="color:rgb(255, 102, 0);">返款金额由a更新为b；</font> |
| <font style="color:rgb(23, 43, 77);">线下打款</font> | <font style="color:rgb(23, 43, 77);">打款时间</font> | <font style="color:rgb(23, 43, 77);">操作人</font> | <font style="color:rgb(23, 43, 77);">线下打款</font> | <font style="color:rgb(23, 43, 77);">   </font> |
| <font style="color:rgb(23, 43, 77);">发起申诉</font> | <font style="color:rgb(23, 43, 77);">发起申诉</font> | <font style="color:rgb(23, 43, 77);">用户</font> | <font style="color:rgb(23, 43, 77);">发起申诉</font> | <font style="color:rgb(23, 43, 77);">   </font> |
| <font style="color:rgb(23, 43, 77);">申诉处理-通过</font> | <font style="color:rgb(23, 43, 77);">处理时间</font> | <font style="color:rgb(23, 43, 77);">操作人</font> | <font style="color:rgb(23, 43, 77);">申诉通过</font> | <font style="color:rgb(23, 43, 77);">用户可见备注：xxx</font><br/><font style="color:rgb(23, 43, 77);">用户不可见备注：xxx</font> |
| <font style="color:rgb(23, 43, 77);">申诉处理-拒绝</font> | <font style="color:rgb(23, 43, 77);">处理时间</font> | <font style="color:rgb(23, 43, 77);">操作人</font> | <font style="color:rgb(23, 43, 77);">申诉拒绝</font> | <font style="color:rgb(23, 43, 77);">用户可见备注：xxx</font><br/><font style="color:rgb(23, 43, 77);">用户不可见备注：xxx</font> |








## 操作保存日志
com.vip8.customermanage.service.business.cashback.CashBackBusinessService#createCashBackLog



# 临时记录
**<font style="color:#601BDE;">创建返款单据 core method</font>**

com.vip8.customermanage.service.impl.CashBackBizServiceImpl#createLiveCashEntity



**<font style="color:#601BDE;">校验订单 和 对应的返款计划 校验 core method</font>**

com.vip8.customermanage.service.impl.CashBackBizServiceImpl#itemPlanCheck







```plain
CashBackItemInfoBO cashBackItemInfoBO = cashBackBusinessService.getItemCashBackInfo(itemPlan,skuDTO,refundDetailDTOS,tradeOrderDTO);
```

CashBackItemInfoBO



```java
@Data
public class CashBackItemInfoBO {

    /**
     * 订单编号
     */
    private String orderNo;

    /**
     * 商品ID
     */
    private Long itemId;


    /**
     * 退款中的退款单信息
     */
    private List<RefundDetailDTO> refundingList;

    /**
     * 返款商品数量
     * 为-1时，无法计算出退款的商品数量
     */
    private Integer itemBackNum;

    /**
     * 商品单个返款金额(单位分)
     */
    private Long itemBackAmount;

    /**
     * 返款总金额(单位分)
     */
    private Long totalCashBackAmount;

}

```





获取返款数量

com.vip8.customermanage.service.impl.CashBackBizServiceImpl#getCashBackOrderInfo

```java

    @ApiOperation("查询指定订单返款进度")
    @GetMapping("/order/schedule")
    public CashBackInfoVo getOrderCashBackInfo(String orderNo, Integer channel) {
        CashBackScheduleDto cashBackScheduleDto = cashBackBizService.getCashBackScheduleInfo(orderNo, channel);
        return CashBackConvert.INSTANCE.convert(cashBackScheduleDto);

    }

```





```java
// 包含了计算特殊返款计划的逻辑
CashBackItemInfoBO cashBackItemInfoBO = cashBackBusinessService.getItemCashBackInfo(itemPlan,skuDTO,refundDetailDTOS,tradeOrderDTO);
```



```java
CashBackItemInfoBO bo = matchItemPrice(itemDTO,itemPlan); 【匹配特殊返款的金额】
```



```java
    /**
     * 匹配返款计划金额
     * @param itemDTO
     * @param itemPlan
     */
    public CashBackItemInfoBO matchItemPrice(OrderDTO.OrderItemDTO itemDTO,FeedBackPlanItemBO itemPlan){
        CashBackItemInfoBO bo = new CashBackItemInfoBO();
        bo.setItemBackAmount(itemPlan.getCashBackAmount().multiply(new BigDecimal(100)).longValue());
        bo.setItemBackNum(itemDTO.getNum());
        //规则不为空
        //获取符合该订单的价格规则
        //并根据价格差排序，价格差最小的排在前面
        List<FeedBackPlanItemPriceRuleBO> planItemPriceRuleBOS = CollectionUtils.isNotEmpty(itemPlan.getItemPriceRuleBOList()) ? itemPlan.getItemPriceRuleBOList().stream()
                .filter(e-> (e.getPrice().multiply(new BigDecimal(100)).longValue()) < itemDTO.getItemPrice())
                .sorted(Comparator.comparing(e->{
                    return itemDTO.getItemPrice() - e.getPrice().multiply(new BigDecimal(100)).longValue();
                })).collect(Collectors.toList()) : null;
        if(CollectionUtils.isNotEmpty(planItemPriceRuleBOS)){
            FeedBackPlanItemPriceRuleBO ruleBO = planItemPriceRuleBOS.get(0);
            bo.setItemBackAmount(ruleBO.getBackAmount().multiply(new BigDecimal(100)).longValue());
        }
        Long total = bo.getItemBackAmount() * bo.getItemBackNum();
        bo.setTotalCashBackAmount(total);
        return bo;
    }
```





```sql
-- 【新增表】
CREATE TABLE `live_cash_back_record_log` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `gmt_create` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',
  `gmt_modified` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `creator` varchar(32) NOT NULL COMMENT '创建人',
  `is_deleted` tinyint(4) NOT NULL DEFAULT '0' COMMENT '是否删除：1(删除) 0(未删除)',
  `modifier` varchar(32) NOT NULL COMMENT '修改人',
  `cash_back_no` varchar(60) DEFAULT NULL COMMENT '返款申请单号',
  `cash_back_id` bigint(20) DEFAULT NULL COMMENT '返款申请单id',
  `content` varchar(1024) DEFAULT NULL COMMENT '操作内容',
  `operate_type` tinyint(4) DEFAULT NULL COMMENT '操作类型',
  `operator_type` tinyint(2) DEFAULT NULL COMMENT '操作人类型：1：系统；2：用户；3：客服人员',
  `operator_id` varchar(32)  DEFAULT NULL COMMENT '操作人id',
  `operator_name` varchar(32)  DEFAULT NULL COMMENT '操作人名称',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=150 DEFAULT CHARSET=utf8mb4 COMMENT='返款申请单日志表';

```















