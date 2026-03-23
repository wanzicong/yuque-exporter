



```sql
表名字：
ks_trade_order
ks_cps_order


```

not_order

<!-- 这是一张图片，ocr 内容为：+一个四个 平 大 DDL 14  ROWS TX:AUTO SCOPE_EXTEND 1 <LLNU> 2 3 MERCHANT_DISTRIBUTION,MERCHANT_FUNDS,MERCHANT-VIDEO 4 MERCHANT_DISTRIBUTION 5 MERCHANT_DISTRIBUTION,MERCHANT_FUNDS 6 MERCHANT_FUNDS 7 LOCALLIFE_ORDER MERCHANT_FUNDS,MERCHANT_DISTRIBUTION,MERCHANT_VIDEO MERCHANT_FUNDS,MERCHANT-DISTRIBUTION,MERCHANT-VIDEO 10 MERCHANT_FUNDS,MERCHANT_DISTRIBUTION 11 MERCHANT_FUNDS,MERCHANT-VIDEO,MERCHANT-DISTRIBUTION MERCHANT_DISTRIBUTION,MERCHANT_VIDEO 12 MERCHANT_DISTRIBUTION,MERCHANT_VIDEO 13 MERCHANT_VIDEO,MERCHANT_VIDEO 14 -->
![](https://cdn.nlark.com/yuque/0/2023/png/21382055/1688697477545-c91563f6-13c0-4df7-b26a-d75b72790122.png)



<!-- 这是一张图片，ocr 内容为：13 ROWS SCOPE_EXTEND 1 NOT_ORDER 2 MERCHANT.DISTRIBUTION,MERCHANT-FUNDS,MERCHANT_VIDEO,NOT_ORDER 3 MERCHANT_DISTRIBUTION,NOT_ORDER MERCHANT_DISTRIBUTION,MERCHANT_FUNDS,NOT_ORDER 4 MERCHANT_FUNDS,NOT_ORDER 5 LOCALLIFE_ORDER,NOT_ORDER 7 MERCHANT_FUNDS,MERCHANT_DISTRIBUTION,MERCHANT-VIDEO,NOT-ORDER MERCHANT-FUNDS, MERCHANT-DISTRIBUTION,MERCHANT-VIDEO,NOT-ORDER 8 MERCHANT_FUNDS,MERCHANT_DISTRIBUTION,NOT_ORDER 10 MERCHANT-FUNDS, MERCHANT-VIDEO,MERCHANT-DISTRIBUTION,NOT-ORDER MERCHANT_DISTRIBUTION,MERCHANT_VIDEO,NOT_ORDER 11 12 MERCHANT_DISTRIBUTION,MERCHANT_VIDEO,NOT_ORDER MERCHANT_VIDEO,MERCHANT_VIDEO,NOT_ORDER 13 -->
![](https://cdn.nlark.com/yuque/0/2023/png/21382055/1688699408207-e87ae328-c254-45a1-bc7b-be3c1809feab.png)

<!-- 这是一张图片，ocr 内容为：四 OUTWAY.KS_INFO2 M OUTWAY.KS_TRADE_ORDER M OUTWAY.KS_APP_INFO 3 M OUTWAY.KS_APP_INFO SOU OUTPUT 十一6 文 公个 DDL K TX:AUTO 1ROW SCOPE_EXTEND <LLNU> -->
![](https://cdn.nlark.com/yuque/0/2023/png/21382055/1688699317423-4d3d5fd1-e005-44ba-950c-fdf0b52c22da.png)





ks666532748413990941  xinc科技 服务市场

ks702843016929144485  xinc科技  后台

ks698339420529519905  辛选网络  后台







生成任务: 

1. batchCrateMainTask 创建主任务

2. 生成对应批次的子主任  batchGenerate

3. 手动触发  /batch/run





```java
package com.vip8.outway.web.controller.task;

import com.alibaba.fastjson.JSON;
import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.vip8.common.log.TraceIdUtil;
import com.vip8.outway.common.enums.KsScopeEnum;
import com.vip8.outway.common.enums.TaskStatusEnum;
import com.vip8.outway.context.SyncJobContext;
import com.vip8.outway.dao.entity.KuaishouAppInfoEntity;
import com.vip8.outway.dao.entity.job.ItemSyncTaskEntity;
import com.vip8.outway.dao.entity.job.SyncDataTaskEntity;
import com.vip8.outway.dao.entity.job.SyncTaskJobEntity;
import com.vip8.outway.dao.entity.kuaishou.KsLiveRecordingEntity;
import com.vip8.outway.inner.common.uitil.StringUtils;
import com.vip8.outway.inner.common.uitil.date.DateUtil;
import com.vip8.outway.dao.service.job.ItemSyncTaskService;
import com.vip8.outway.job.task.ItemTaskRunJob;
import com.vip8.outway.job.task.TaskRunJob;
import com.vip8.outway.service.repos.KuaishouAppInfoService;
import com.vip8.outway.service.repos.SyncDataTaskReposService;
import com.vip8.outway.service.repos.SyncTaskJobReposService;
import com.vip8.outway.service.sync.task.SyncDataSubTaskService;
import io.swagger.annotations.Api;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.collections4.CollectionUtils;
import org.apache.commons.lang3.time.DateUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;
import java.text.ParseException;
import java.time.LocalDateTime;
import java.util.*;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;


/**
 * @author jinlu
 */
@RestController
@RequestMapping("/task")
@Slf4j
@Api(tags = {"执行任务"})
public class TaskController {

    @Autowired
    private SyncTaskJobReposService syncTaskJobReposService;

    @Resource
    private SyncDataTaskReposService syncDataTaskReposService;

    @Resource
    private SyncDataSubTaskService syncDataSubTaskService;

    @Autowired
    private TaskRunJob taskRunJob;

    @Autowired
    private ItemSyncTaskService itemSyncTaskService;

    @Resource
    private ThreadPoolTaskExecutor executorItemTask;

    @Resource
    private ItemTaskRunJob itemTaskRunJob;

    @Resource
    private KuaishouAppInfoService kuaishouAppInfoService;


    @PostMapping("/retry/failed")
    public void runFailTask() {
        log.info("部分成功任务手动执行开始");
        ExecutorService threadPool = Executors.newFixedThreadPool(4);
        QueryWrapper<SyncDataTaskEntity> queryWrapper = new QueryWrapper<>();
        queryWrapper.lambda()
                .in(SyncDataTaskEntity::getStatus, TaskStatusEnum.PARTIAL_SUCCESS.getCode())
                .eq(SyncDataTaskEntity::getType, 0)
        ;
        List<SyncDataTaskEntity> syncTaskJobEntities = syncDataTaskReposService.list(queryWrapper);
        List<Long> taskId = syncTaskJobEntities.stream().map(SyncDataTaskEntity::getId).collect(Collectors.toList());
        QueryWrapper<SyncTaskJobEntity> subListQuery = new QueryWrapper<>();
        subListQuery.lambda()
                .in(CollectionUtils.isNotEmpty(taskId), SyncTaskJobEntity::getTaskId, taskId)
                .eq(SyncTaskJobEntity::getStatus, TaskStatusEnum.FAILED.getCode())
                .ge(SyncTaskJobEntity::getJobBeginTime, "2023-02-10 16:50:00")
        ;
        List<SyncTaskJobEntity> subList = syncTaskJobReposService.list(subListQuery);
        List<CompletableFuture> futureList = subList.stream().map(taskEntity -> {
            return CompletableFuture.runAsync(() -> {
                Long sellerId = taskEntity.getSellerId();
                KuaishouAppInfoEntity entity = kuaishouAppInfoService.getAuthAppInfoOrderLatest(sellerId);
                if (Objects.nonNull(entity)) {
                    if (taskEntity.getTaskType().contains("refund") && !entity.getScope().contains(KsScopeEnum.KS_SHOU_HOU.getCode())) {
                        log.info("当前任务不包含作用域取消");
                        return;
                    }
                    //店铺授权状态才执行
                    syncDataSubTaskService.processSubTask(taskEntity);
                }
            }, threadPool);
        }).collect(Collectors.toList());
        // 使用join()方法使得主线程阻塞，并等待所有并行线程完成
        CompletableFuture.allOf(futureList.toArray(new CompletableFuture[]{})).join();
        log.info("部分成功任务手动执行完成");
    }


    @PostMapping("/batch/run")
    public void runTask(String type, Integer threadCore,String remark,String taskStartTime) {
        ExecutorService threadPool = Executors.newFixedThreadPool(threadCore);
        QueryWrapper<SyncDataTaskEntity> queryWrapper = new QueryWrapper<>();
        queryWrapper.lambda()
                .in(SyncDataTaskEntity::getStatus, TaskStatusEnum.PROCESSING.getCode(), TaskStatusEnum.FAILED.getCode())
                .eq(StringUtils.isNotEmpty(type),SyncDataTaskEntity::getTaskType, type)
                .eq(StringUtils.isNotEmpty(remark),SyncDataTaskEntity::getRemark,remark)
                .gt(StringUtils.isNotEmpty(taskStartTime),SyncDataTaskEntity::getTaskStartTime,taskStartTime)
        ;
        List<SyncDataTaskEntity> syncTaskJobEntities = syncDataTaskReposService.list(queryWrapper);
        for (SyncDataTaskEntity processTask : syncTaskJobEntities) {
            List<SyncTaskJobEntity> jobList = syncTaskJobReposService.queryNoSuccessJobByTaskId(processTask.getId());
            //多线程执行任务
            List<CompletableFuture> futureList = jobList.stream().map(jobEntity -> {
                return CompletableFuture.runAsync(() -> {
                    syncDataSubTaskService.processSubTask(jobEntity);
                }, threadPool);
            }).collect(Collectors.toList());
            // 使用join()方法使得主线程阻塞，并等待所有并行线程完成
            CompletableFuture.allOf(futureList.toArray(new CompletableFuture[]{})).join();
        }
    }


    @PostMapping("/run")
    public void runTask(Long taskId) {
        log.info("手动执行主任务开始,任务参数:{}", taskId);
        List<SyncTaskJobEntity> jobList = syncTaskJobReposService.queryNoSuccessJobByTaskId(taskId);
        for (SyncTaskJobEntity syncTaskJobEntity : jobList) {
            syncDataSubTaskService.processSubTask(syncTaskJobEntity);
        }
        log.info("手动执行主任务开始,任务参数:{}", taskId);
    }


    @PostMapping("/run/task/future")
    public void runTaskFuture(Long taskId) throws InterruptedException {
        SyncDataTaskEntity taskEntity = syncDataTaskReposService.getById(taskId);
        List<SyncTaskJobEntity> list = syncTaskJobReposService.queryNoSuccessJobByNow(taskId);
        SyncTaskJobEntity entity = new SyncTaskJobEntity();
        do {
            log.info("循序开始");
            entity = syncTaskJobReposService.getLastProcessJobByTaskId(taskId);
            if (CollectionUtils.isNotEmpty(list)) {
                //多线程执行任务
                List<CompletableFuture> futureList = list.stream().map(jobEntity -> {
                    return CompletableFuture.runAsync(() -> {
                        syncDataSubTaskService.processSubTask(jobEntity);
                    }, executorItemTask);
                }).collect(Collectors.toList());
                // 使用join()方法使得主线程阻塞，并等待所有并行线程完成
                CompletableFuture.allOf(futureList.toArray(new CompletableFuture[]{})).join();
            } else {
                log.info("未查询到数据线程休眠");
                Thread.sleep(1050 * 60);
            }

            list = syncTaskJobReposService.queryNoSuccessJobByNow(taskId);
            log.info("循环结束，本次循环共处理{}个任务", list.size());
            //查询最后一个未执行的任务是否存在
        } while (Objects.nonNull(entity));
        log.info("task-任务结束");
    }

    @PostMapping("/generate")
    public void testGenerate(Long taskId) {
        SyncDataTaskEntity taskEntity = syncDataTaskReposService.getById(taskId);
        do {
            SyncTaskJobEntity latestTaskJob = syncTaskJobReposService.getLastJobByTaskId(taskEntity.getId());
            if (Objects.isNull(latestTaskJob)) {
                syncDataSubTaskService.generateSubTask(taskEntity);
            } else {
                if (latestTaskJob.getJobEndTime().compareTo(taskEntity.getTaskEndTime()) <= 0) {
                    syncDataSubTaskService.generateSubTask(latestTaskJob);
                } else {
                    log.info("执行到最新了");
                    break;
                }
            }
        } while (true);
    }

    @PostMapping("/create/task")
    public void batchCrateMainTask(String sellerIds, String type, String remark) throws ParseException {
        String[] idLIst = sellerIds.split(",");
        for (String id : idLIst) {
            try {
                KuaishouAppInfoEntity appInfo = kuaishouAppInfoService.getBySellerIdAndAppId(Long.parseLong(id), "ks698339420529519905");
                if (Objects.nonNull(appInfo)) {
                    SyncDataTaskEntity entity = createMainTask(type, appInfo, remark);
                    syncDataTaskReposService.save(entity);
                }
            } catch (Exception e) {
                log.info("住任务生成失败", e);
            }
        }
    }

    @PostMapping("/create/task/wanzicong")
    public void batchCrateMainTask4wanzicong(String sellerIds, String type, String remark , String start, String end) throws ParseException {
        String[] idLIst = sellerIds.split(",");
        ArrayList<SyncDataTaskEntity> result = new ArrayList<>();
        for (String id : idLIst) {
            try {
                LambdaQueryWrapper<KuaishouAppInfoEntity> queryWrapper = new LambdaQueryWrapper<>();
                queryWrapper.eq(KuaishouAppInfoEntity::getSellerId,Long.parseLong(id));
                List<KuaishouAppInfoEntity> list = kuaishouAppInfoService.list(queryWrapper);
                log.info(" the id is :{} and list is [{}]",id,list);
                if (CollectionUtils.isNotEmpty(list)) {
                    for (KuaishouAppInfoEntity appInfo : list) {
                        SyncDataTaskEntity entity = createMainTaskWanzicong(type, appInfo, remark,new Date(),new Date());
                        result.add(entity);
                        log.info("batchCrateMainTask4wanzicong  entity is {}",JSON.toJSONString(entity));
                        syncDataTaskReposService.save(entity);
                    }
                }
            } catch (Exception e) {
                log.info("住任务生成失败", e);
            }
        }
        log.info("batchCrateMainTask4wanzicong result size is {}",result.size());
    }

    private SyncDataTaskEntity createMainTaskWanzicong(String type,
                                                       KuaishouAppInfoEntity kuaishouAppInfoEntity,
                                                       String remark,Date start,Date end) throws ParseException {
        SyncDataTaskEntity entity = new SyncDataTaskEntity();
        if ("cps".equals(type)) {
            entity.setAppId(kuaishouAppInfoEntity.getAppId());
        }
        entity.setStatus(0);
        entity.setType(0);
        entity.setPlatformType(3);
        entity.setTaskType(type);
        entity.setTaskStartTime(start);
        entity.setTaskEndTime(end);
        entity.setRemark(remark);
        entity.setTaskName(remark + "_" + type + "_" + kuaishouAppInfoEntity.getSellerId());
        entity.setCreator(TraceIdUtil.getTraceId());
        entity.setModifier(TraceIdUtil.getTraceId());
        entity.setSellerId(kuaishouAppInfoEntity.getSellerId());
        entity.setSellerName(kuaishouAppInfoEntity.getMemo());
        entity.setGmtCreate(new Date());
        entity.setGmtModified(new Date());
        entity.setJobInterval(3600);
        return entity;
    }


    private SyncDataTaskEntity createMainTask(String type, KuaishouAppInfoEntity kuaishouAppInfoEntity, String remark) throws ParseException {
        SyncDataTaskEntity entity = new SyncDataTaskEntity();
//        entity.setAppId("ks698339420529519905");
        entity.setStatus(0);
        entity.setType(0);
        entity.setPlatformType(3);
        entity.setTaskType(type);
        Date taskEndTime = DateUtils.addDays(new Date(), -1);
        entity.setTaskEndTime(taskEndTime);
        entity.setTaskStartTime(DateUtils.addDays(new Date(), -89));
        entity.setRemark(remark);
        entity.setTaskName(remark + "_" + type + "_" + kuaishouAppInfoEntity.getSellerId());
        entity.setCreator(TraceIdUtil.getTraceId());
        entity.setModifier(TraceIdUtil.getTraceId());
        entity.setSellerId(kuaishouAppInfoEntity.getSellerId());
        entity.setSellerName(kuaishouAppInfoEntity.getMemo());
        entity.setGmtCreate(new Date());
        entity.setGmtModified(new Date());
        entity.setJobInterval(3600);
        return entity;
    }

    @PostMapping("/batch/generate")
    public void batchGenerate(String remark) throws ParseException {
        QueryWrapper<SyncDataTaskEntity> queryWrapper = new QueryWrapper<>();
        queryWrapper.lambda()
                .eq(SyncDataTaskEntity::getRemark, remark);

        List<SyncDataTaskEntity> list = syncDataTaskReposService.list(queryWrapper);
        for (SyncDataTaskEntity entity : list) {
            do {
                SyncTaskJobEntity latestTaskJob = syncTaskJobReposService.getLastJobByTaskId(entity.getId());
                if (Objects.isNull(latestTaskJob)) {
                    syncDataSubTaskService.generateSubTask(entity);
                } else {
                    if (latestTaskJob.getJobEndTime().compareTo(entity.getTaskEndTime()) <= 0) {
                        syncDataSubTaskService.generateSubTask(latestTaskJob);
                    } else {
                        log.info("执行到最新了");
                        break;
                    }

                }
            } while (true);
        }
    }


    private SyncJobContext createContext(KsLiveRecordingEntity liveRecordingEntity) throws ParseException {
        SyncJobContext syncJobContext = new SyncJobContext();
        syncJobContext.setShopId(liveRecordingEntity.getSellerId());
        syncJobContext.setSellerId(liveRecordingEntity.getDistributorId());
        syncJobContext.setItemId(liveRecordingEntity.getItemId());
        if (Objects.nonNull(liveRecordingEntity.getLiveDate())) {
            Date liveDate = DateUtils.parseDate(liveRecordingEntity.getLiveDate(), DateUtil.YMD);
            //查询范围直播当日零点到次日凌晨1点
            syncJobContext.setSyncStartTime(liveDate);
        }
        return syncJobContext;
    }

    @PostMapping("/tag/tradeOrder")
    public void tagTradeOrder(Long taskId) {
        // 给交易订单打标 not order
        LambdaQueryWrapper<KuaishouAppInfoEntity> queryWrapper = new LambdaQueryWrapper<>();
        queryWrapper.ne(KuaishouAppInfoEntity::getAppId,"ks698339420529519905");
        List<KuaishouAppInfoEntity> list = kuaishouAppInfoService.list(queryWrapper);
        log.info("刷新数据打标: not_order list is [{}]",JSON.toJSONString(list));
        handleTagList(list,"not_order");
        kuaishouAppInfoService.updateBatchById(list);
    }

    @PostMapping("/tag/cpsOrder")
    public void tagCpsOrder(Long taskId) {
        // 给分销订单打标 merchant_distribution
        LambdaQueryWrapper<KuaishouAppInfoEntity> queryWrapper = new LambdaQueryWrapper<>();
        queryWrapper.eq(KuaishouAppInfoEntity::getAppId,"ks698339420529519905");
        List<KuaishouAppInfoEntity> list = kuaishouAppInfoService.list(queryWrapper);
        log.info("刷新数据打标: merchant_distribution list is [{}]",JSON.toJSONString(list));
        handleTagList(list,"merchant_distribution");
        kuaishouAppInfoService.updateBatchById(list);
    }

    @PostMapping("/tag/cpsOrder/cancel")
    public void cancelTagCpsOrder(Long taskId) {
        // 给交易订单打标 not order
        LambdaQueryWrapper<KuaishouAppInfoEntity> queryWrapper = new LambdaQueryWrapper<>();
        queryWrapper.ne(KuaishouAppInfoEntity::getAppId,"ks698339420529519905");
        List<KuaishouAppInfoEntity> list = kuaishouAppInfoService.list(queryWrapper);
        log.info("刷新数据打标: cpsOrder cancel list is [{}]",JSON.toJSONString(list));
        // 给打过标的cps 订单取消打标
        handleCancelTag(list,"merchant_distribution");
        kuaishouAppInfoService.updateBatchById(list);
    }

    /**
     * 取消打标
     * @param list
     * @param tag
     */
    private static void handleCancelTag(List<KuaishouAppInfoEntity> list,String tag) {
        for (KuaishouAppInfoEntity entity : list) {
            String scopeExtend = entity.getScopeExtend();
            log.info("刷新数据打标 handleCancelTag  before: {}",scopeExtend);
            if (StringUtils.isNotEmpty(scopeExtend) && scopeExtend.contains(tag)) {
                String[] split = scopeExtend.split(",");
                List<String> tags = Arrays.asList(split);
                if (CollectionUtils.isNotEmpty(tags)) {
                    tags = tags.stream().filter(e-> !StringUtils.isNotEmpty(tag) || !StringUtils.isNotEmpty(e) || !tag.equals(e.trim())).collect(Collectors.toList());
                }
                String result = String.join(",", tags);
                entity.setScopeExtend(result);
            }
            log.info("刷新数据打标 handleCancelTag  after: {}",entity.getScopeExtend());
        }
    }


    /**
     * 进行打标
     * @param list
     * @param tag
     */
    private static void handleTagList(List<KuaishouAppInfoEntity> list,String tag) {
        for (KuaishouAppInfoEntity entity : list) {
            String scopeExtend = entity.getScopeExtend();
            log.info("刷新数据打标 handleTagList  before: {}",scopeExtend);
            if (StringUtils.isEmpty(scopeExtend)) {
                entity.setScopeExtend(tag);
            } else if (StringUtils.isNotEmpty(scopeExtend) && !scopeExtend.contains(tag)) {
                entity.setScopeExtend(scopeExtend + "," + tag);
            }
            log.info("刷新数据打标 handleTagList  after: {}",entity.getScopeExtend());
        }
    }

}


```



<font style="color:rgb(33, 33, 33);">交易订单历史三个月数据刷新用户openId</font>

<font style="color:rgb(33, 33, 33);">cps订单历史三个月数据刷新用户openId</font>







历史订单根据详情数据刷新历史数据



创建新的service 类

<font style="color:#000000;background-color:#ffffff;">PlatformApiTypeEnum</font>

 <font style="color:#000000;background-color:#ffffff;">KsOrderSyncServiceImpl</font>

 



```plain
create index idx_create_time_seller_id
    on ks_cps_order (gmt_create asc, seller_id asc)
    comment '创建时间和卖家id索引';
```

 

