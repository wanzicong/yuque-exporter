## 问题元数据
问题列表: 

[我的工作-TAPD平台](https://www.tapd.cn/tapd_fe/my/work)





[【优化】客户账单导出明细，导致对应服务挂了-智领平台-TAPD平台](https://www.tapd.cn/55357004/bugtrace/bugs/view/1155357004001018452)  【导出】

财务管理-应收账单-客户账单  
<font style="color:rgb(27, 27, 27);background-color:rgb(255, 251, 255);">https://test-saas.tiananhub.com/api/finance/orderBill/exportPageGroupByCustomer</font>

jnpf.base.controller.order.OrderBillApi#exportPageGroupByCustomer

jnpf.base.service.order.OrderBillService#exportPageGroupByCustomer

<font style="color:#080808;background-color:#ffffff;">base_organize 组织表</font>

<font style="color:#080808;background-color:#ffffff;">OrderBillGroupResp </font>

<font style="color:#080808;background-color:#ffffff;">jnpf.base.util.ExcelExportHelper 工具类</font>

jnpf.util.excel.ExcelUtils#<font style="color:#080808;background-color:#ffffff;">exportServiceExcel</font>  
jnpf-common-core-3.1.0-20240818.033159-5.jar  


[【后端】账单审核：推送速度需优化-智领平台-TAPD平台](https://www.tapd.cn/55357004/bugtrace/bugs/view/1155357004001018375) 【批量查询，批量审批】

物业管理-物业收费-周期费用审批

[周期费用审核 - 招商运营平台 (tiananhub.com)](https://test-saas.tiananhub.com/PropertyPage/expenses/cyclicCharge)  
<font style="color:rgb(27, 27, 27);background-color:rgb(255, 251, 255);">https://test-saas.tiananhub.com/api/property/expensePeriod/auditByIds</font>  
jnpf.controller.other.ExpensePeriodApi#auditByIds

jnpf.service.other.ExpensePeriodService#auditByIds

jnpf.service.other.ExpensePeriodService#auditData   
<font style="color:#080808;background-color:#ffffff;">expense_period  周期性费用表</font>

<font style="color:#080808;background-color:#ffffff;"></font>

<font style="color:#080808;background-color:#ffffff;">  
</font><font style="color:rgb(27, 27, 27);background-color:rgb(255, 251, 255);">https://test-saas.tiananhub.com/api/property/expensePeriod/auditByIds</font><font style="color:#080808;background-color:#ffffff;">  
</font><font style="color:#080808;background-color:#ffffff;">周期性审批</font>

<font style="color:#080808;background-color:#ffffff;">表:   expense_period  - property</font>

<font style="color:#080808;background-color:#ffffff;">表： expense_management</font>

<font style="color:#080808;background-color:#ffffff;">表： order_main</font>

<font style="color:#080808;background-color:#ffffff;">finance_plan_pay  
</font>

```plain
Affect(class count: 3 , method count: 3) cost in 333 ms, listenerId: 3
`---ts=2024-09-13 10:54:04;thread_name=http-nio-30302-exec-6;id=214;is_daemon=true;priority=5;TCCL=org.springframework.boot.web.embedded.tomcat.TomcatEmbeddedWebappClassLoader@2d58136
    `---[2931.264301ms] jnpf.base.service.property.OrderBillPropertyService$$EnhancerBySpringCGLIB$$5dcbd1fb:auditBatch()
        `---[99.99% 2931.011999ms ] org.springframework.cglib.proxy.MethodInterceptor:intercept()
            `---[99.99% 2930.714599ms ] jnpf.base.service.property.OrderBillPropertyService:auditBatch()
                +---[0.04% 1.1716ms ] org.slf4j.Logger:info() #249
                +---[0.00% 0.0134ms ] jnpf.util.ToolUtil:isEmpty() #250
                +---[0.00% 0.021601ms ] java.util.List:size() #253
                +---[0.01% 0.2116ms ] org.slf4j.Logger:info() #253
                +---[0.00% 0.0081ms ] java.util.ArrayList:<init>() #254
                +---[0.00% 0.027ms ] java.util.Collections:synchronizedList() #254
                +---[0.00% 0.004899ms ] java.util.ArrayList:<init>() #255
                +---[0.00% 0.018ms ] java.util.List:stream() #256
                +---[0.00% 0.0245ms ] java.util.stream.Stream:filter() #256
                +---[0.00% 0.0174ms ] java.util.stream.Stream:map() #257
                +---[0.00% 0.0212ms ] java.util.stream.Stream:distinct() #257
                +---[0.00% 0.018201ms ] java.util.stream.Collectors:toList() #257
                +---[0.00% 0.0998ms ] java.util.stream.Stream:collect() #257
                +---[0.00% 0.0075ms ] java.util.HashMap:<init>() #258
                +---[0.00% 0.005ms ] jnpf.util.ToolUtil:isNotEmpty() #259
                +---[0.01% 0.2158ms ] org.slf4j.Logger:info() #260
                +---[0.69% 20.2019ms ] jnpf.base.service.order.ExpenseManagementService:listByExpenseIds() #261
                +---[0.00% 0.010399ms ] jnpf.util.ToolUtil:isNotEmpty() #262
                +---[0.00% 0.0083ms ] java.util.List:stream() #263
                +---[0.00% 0.0411ms ] java.util.stream.Collectors:toMap() #263
                +---[0.00% 0.0617ms ] java.util.stream.Stream:collect() #263
                +---[0.00% 0.0052ms ] java.util.ArrayList:<init>() #267
                +---[0.00% 0.0074ms ] java.util.Collections:synchronizedList() #267
                +---[0.00% 0.004ms ] java.util.ArrayList:<init>() #268
                +---[0.00% 0.005101ms ] java.util.Collections:synchronizedList() #268
                +---[0.00% 0.0048ms ] java.util.List:stream() #272
                +---[0.00% 0.0073ms ] java.util.stream.Stream:map() #272
                +---[0.00% min=0.005201ms,max=0.009399ms,total=0.0146ms,count=2] java.util.stream.Collectors:toList() #302
                +---[9.29% min=0.5924ms,max=271.664901ms,total=272.257301ms,count=2] java.util.stream.Stream:collect() #302
                +---[0.00% 0.009ms ] java.util.List:stream() #302
                +---[0.00% 0.0102ms ] java.util.stream.Stream:map() #302
                +---[0.00% 0.0196ms ] jnpf.util.ToolUtil:isNotEmpty() #305
                +---[0.02% 0.4507ms ] jnpf.util.ToolUtil:isNotEmpty() #310
                +---[0.01% 0.3627ms ] org.slf4j.Logger:info() #311
                +---[2.13% 62.3503ms ] jnpf.base.service.order.OrderBillService:publishOrderBill() #313
                +---[0.01% 0.400601ms ] org.slf4j.Logger:info() #315
                +---[1.38% 40.359ms ] jnpf.base.service.order.OrderBillService:updateCorrectionAmount() #316
                +---[1.79% 52.4567ms ] jnpf.base.service.property.OrderBillPropertyService:dealOrderMainData() #319
                `---[0.02% 0.4438ms ] org.slf4j.Logger:info() #320




`---ts=2024-09-13 15:14:33;thread_name=http-nio-30302-exec-10;id=182;is_daemon=true;priority=5;TCCL=org.springframework.boot.web.embedded.tomcat.TomcatEmbeddedWebappClassLoader@522941b2
    `---[429.095ms] jnpf.base.service.property.OrderBillPropertyService$$EnhancerBySpringCGLIB$$3ba601ae:auditBatch()
        `---[99.97% 428.9513ms ] org.springframework.cglib.proxy.MethodInterceptor:intercept()
            `---[99.98% 428.8704ms ] jnpf.base.service.property.OrderBillPropertyService:auditBatch()
                +---[0.21% 0.8942ms ] org.slf4j.Logger:info() #249
                +---[0.00% 0.0141ms ] jnpf.util.ToolUtil:isEmpty() #250
                +---[0.00% 0.0193ms ] java.util.List:size() #253
                +---[0.05% 0.223ms ] org.slf4j.Logger:info() #253
                +---[0.00% 0.0096ms ] java.util.ArrayList:<init>() #254
                +---[0.01% 0.0252ms ] java.util.Collections:synchronizedList() #254
                +---[0.00% 0.0027ms ] java.util.ArrayList:<init>() #255
                +---[0.00% 0.0189ms ] java.util.List:stream() #256
                +---[0.00% 0.018ms ] java.util.stream.Stream:filter() #256
                +---[0.01% 0.0269ms ] java.util.stream.Stream:map() #257
                +---[0.00% 0.0162ms ] java.util.stream.Stream:distinct() #257
                +---[0.01% 0.0222ms ] java.util.stream.Collectors:toList() #257
                +---[0.02% 0.0907ms ] java.util.stream.Stream:collect() #257
                +---[0.00% 0.0043ms ] java.util.HashMap:<init>() #258
                +---[0.00% 0.0027ms ] jnpf.util.ToolUtil:isNotEmpty() #259
                +---[0.05% 0.2093ms ] org.slf4j.Logger:info() #260
                +---[3.48% 14.9413ms ] jnpf.base.service.order.ExpenseManagementService:listByExpenseIds() #261
                +---[0.00% 0.0026ms ] jnpf.util.ToolUtil:isNotEmpty() #262
                +---[0.00% 0.0024ms ] java.util.List:stream() #263
                +---[0.00% 0.0214ms ] java.util.stream.Collectors:toMap() #263
                +---[0.01% 0.0491ms ] java.util.stream.Stream:collect() #263
                +---[0.00% 0.0018ms ] java.util.ArrayList:<init>() #267
                +---[0.00% 0.005ms ] java.util.Collections:synchronizedList() #267
                +---[0.00% 0.0017ms ] java.util.ArrayList:<init>() #268
                +---[0.00% 0.0024ms ] java.util.Collections:synchronizedList() #268
                +---[60.57% 259.7615ms ] java.util.List:forEach() #304
                +---[0.01% 0.0217ms ] jnpf.util.ToolUtil:isNotEmpty() #340
                +---[0.00% 0.0051ms ] jnpf.util.ToolUtil:isNotEmpty() #345
                +---[0.12% 0.5029ms ] org.slf4j.Logger:info() #346
                +---[11.03% 47.3134ms ] jnpf.base.service.order.OrderBillService:publishOrderBill() #348
                +---[0.10% 0.4376ms ] org.slf4j.Logger:info() #350
                +---[11.82% 50.6786ms ] jnpf.base.service.order.OrderBillService:updateCorrectionAmount() #351
                +---[11.61% 49.802ms ] jnpf.base.service.property.OrderBillPropertyService:dealOrderMainData() #354
                `---[0.10% 0.4141ms ] org.slf4j.Logger:info() #355





```

<font style="color:#080808;background-color:#ffffff;"></font>

<font style="color:#080808;background-color:#ffffff;"></font>

```plain
public Boolean checkPlanPayUpdateState(Collection<Long> planPayIds) {
    if (ToolUtil.isEmpty(planPayIds)) {
        log.info("planPayIds为空");
        return false;
    }
    List<FinancePlanPayEntity> list = this.listByIds(planPayIds);
    if (ToolUtil.isEmpty(list)) {
        log.info("收款计划不存在");
        return false;
    }
    // 计算各账单状态的数量
    List<PayStateCountResp> countInfoList = orderBillService.listPayStateCountByPlanPayIds(planPayIds);
    Map<Long, PayStateCountResp> countInfoMap = countInfoList.stream().collect(Collectors.toMap(PayStateCountResp::getOrderId, a -> a, (k1, k2) -> k1));
    // 根据账单更新收款计划状态
    List<FinancePlanPayEntity> updateList = new ArrayList<>();
    list.forEach(x -> {
        PayStateCountResp countInfo = countInfoMap.get(x.getOrderId());
        if (countInfo == null) {
            log.info("订单[{}]无法统计账单数量", x.getOrderId());
            return;
        }
        int planPayState = getPlanPayState(countInfo);
        x.setState(planPayState);

        // 只更新状态 【优化更新】
        FinancePlanPayEntity planPayEntity = new FinancePlanPayEntity();
        planPayEntity.setState(planPayState);
        planPayEntity.setId(x.getId());
        updateList.add(planPayEntity);
    });
    if (ToolUtil.isNotEmpty(updateList)) {
        return this.updateBatchById(updateList, updateList.size());
    }
    return false;
}


create index bill_receivable_detail__bill_one
         on bill_receivable_detail (F_BillId, F_ReceivableType)
         comment '查询账单信息';
```

<font style="color:#080808;background-color:#ffffff;"></font>

<font style="color:#080808;background-color:#ffffff;"></font>

<font style="color:rgb(27, 27, 27);background-color:rgb(255, 251, 255);">/api/property/expenseMeter/auditByIds</font>

<font style="color:rgb(27, 27, 27);background-color:rgb(255, 251, 255);">走表费用</font>

<font style="color:rgb(27, 27, 27);background-color:rgb(255, 251, 255);"></font>

<font style="color:rgb(27, 27, 27);background-color:rgb(255, 251, 255);">https://test-saas.tiananhub.com/api/property/oneCostFee/auditByIds</font>

<font style="color:rgb(27, 27, 27);background-color:rgb(255, 251, 255);">一次性费用</font>

  
<font style="color:rgb(27, 27, 27);background-color:rgb(255, 251, 255);">https://test-saas.tiananhub.com/api/property/expenseTemporary/auditByIds</font>

<font style="color:rgb(27, 27, 27);background-color:rgb(255, 251, 255);">临时费用</font>



<font style="color:#080808;background-color:#ffffff;"></font>

<font style="color:#080808;background-color:#ffffff;"></font>

<font style="color:#080808;background-color:#ffffff;"></font>



[【优化】财务报表，连续导出，内存溢出，导致相关服务挂了-智领平台-TAPD平台](https://www.tapd.cn/55357004/bugtrace/bugs/view/1155357004001018358)  【ing】

财务报表连续导出





[【优化】批量设置收费计划，添加多个资源，响应时间优化-智领平台-TAPD平台](https://www.tapd.cn/55357004/bugtrace/bugs/view/1155357004001018322) 【ing】

[车位收费 - Saas招商运营 (tiananhub.com)](https://dev-saas.tiananhub.com/PropertyPage/chargePlan/carportChargePlan)

批量设置多个收费计划





[优化财务板块导出性能，减少等待时间-智领平台-TAPD平台](https://www.tapd.cn/55357004/prong/stories/view/1155357004001025811)





[实收明细表性能优化-智领平台-TAPD平台](https://www.tapd.cn/55357004/bugtrace/bugs/view/1155357004001017217) 【待确认】

财务管理-财务报表-实收明细  
[实收明细表 - Saas招商运营 (tiananhub.com)](https://dev-saas.tiananhub.com/FinancialPage/financialStatement/actualReceipts)  
<font style="color:rgb(27, 27, 27);background-color:rgb(255, 251, 255);">https://dev-saas.tiananhub.com/api/finance/detailsActualReceipts/page</font>  
jnpf.base.controller.financialstatements.DetailsActualReceiptsApi#getCollectionDailyPage  
jnpf.base.service.financialstatements.DetailsActualReceiptsService#getCollectionDailyPage  
<font style="color:#080808;background-color:#ffffff;">Collection_Daily</font>  
<font style="color:#080808;background-color:#ffffff;">finance_report_config 账单查询配置</font>  
  




[【后端】物业收缴率，导出表头、计算公式优化-智领平台-TAPD平台](https://www.tapd.cn/55357004/bugtrace/bugs/view/1155357004001017856)





## 方案大纲
### 问题分析
1. 导出一个excel oom
2. 多个请求同时并行 导致 oom
3. 一个excel 要包含指定的数据量



### 解决方向
![画板](https://cdn.nlark.com/yuque/0/2024/jpeg/21382055/1724741554576-e154d9b8-5ec1-4e89-8fcd-d506e6b552b9.jpeg)



异步处理（mq排队） ，多个excel 合并Zip ，分组处理 ， 分页处理



1. 每个模块定义一个消息队列 ,如 finance_queue
2. 发送消息，业务参数，查询参数 
3. 查询count ，根据业务要求的单个文件数据量进行分组，判断生成的excel 数量
4. 分页查询业务数据
5. 单个文件的数据量 会包含多个分页 使用流式写excel 写入excel
6. 查询数据逻辑， 涉及公用的数据，用来字段换取，将数据放到 redis 中



关键词： 分页查询业务数据， 分组处理excel ，rabbitmq 排队处理业务 （<font style="color:#DF2A3F;">一个业务可以配置多个queue ，hash 提高并发度</font>），<font style="color:#DF2A3F;">redis 缓存配置数据</font>



场景举例: 单个excel 1万数据 ， 单页查询1千 ，数据总量 10万 

分页个数:   10 万/ 1千  = 100 页 （100 次查询）

文件数量: 10 个 excel 文件 

文件1 ： 【1-10 页】 =  1万数据

文件2 ： 【11-20 页】=  1万数据

文件3 ： 【21-30 页】=  1万数据

文件4 ： 【31-40 页】=  1万数据

文件5 ： 【41-50 页】=  1万数据

文件6 ： 【51-60 页】=  1万数据

文件7 ： 【61-70 页】=  1万数据

文件8 ： 【71-80 页】=  1万数据

文件9 ： 【81-90 页】=  1万数据

文件10 ：【91-100 页】=  1万数据



**流式导入: jnpf.base.util.BigExcelExportHelper#****<font style="color:#080808;background-color:#ffffff;">start</font>**



## 动态配置
1. 分页数量
2. 业务对应的 消息队列列表
3. 提前预置好消息队列

## 扩展计划
导出进度 【数据处理进度，写入进度 】 线程池异步处理

1.  写入excel 的进度 【流式写入可以 ++ 操作】  
2. response 写入流的操作， response 处理字节byte ++ 操作



totalDataCount ， handleDataCount

totalByteLength ， handleByteLength

















