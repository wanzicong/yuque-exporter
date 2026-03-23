

```vue
select
  value,
  pageUrl,
  urlRouter
from
  (
    select
      sum(pv) as value,
      url as pageUrl,
      url_router as urlRouter
    from
      te_analysis_group
      where app_id = 'CUSTOMER_MANAGE'
      and trigger_date between '2023-11-27'
      and '2023-12-27'
      and url = '/workbench'
    group by
      url
  ) a
order by
  a.value desc
limit
  10

-- 数据
select count(1) from te_analysis_pageview where app_id = 'CUSTOMER_MANAGE'
      and trigger_date between '2023-11-27'
      and '2023-12-27'
      and url = '/workbench'   

-- 查询聚合的数据
select
      * 
    from
      te_analysis_group
      where app_id = 'CUSTOMER_MANAGE'
      and trigger_date between '2023-11-27'
      and '2023-12-27'
      and url = '/workbench'

-- 查询 当前的pv
  select count(1) from te_analysis_pageview where app_id = 'CUSTOMER_MANAGE'
      and trigger_date = '2023-11-27'
      and url = '/workbench'   


select
      * 
    from
      te_analysis_group
      where app_id = 'CUSTOMER_MANAGE'
      and trigger_date between '2023-11-27'
      and '2023-12-27'
      and url = '/workbench'

-- 聚合统计 pv = 8 uv = 8
select count(1) , count(distinct fid) from te_analysis_pageview where app_id = 'CUSTOMER_MANAGE'
      and trigger_date = '2023-11-27'
      and url = '/workbench'   

```





初步排查只有添加 group 更新 group 

```sql
select
      * 
    from
      te_analysis_group

```





```java
package com.vip8.fuxi.biz.trackevent.task;

import cn.hutool.core.date.DateUtil;
import com.vip8.base.common.vo.PagedVO;
import com.vip8.fuxi.biz.trackevent.enums.TrackAppIdEnum;
import com.vip8.fuxi.biz.trackevent.service.TrackDashboardService;
import com.vip8.fuxi.biz.trackevent.service.TrackMenuService;
import com.vip8.fuxi.biz.trackevent.service.TrackPageviewGroupService;
import com.vip8.fuxi.dao.trackevent.dos.DashboardDO;
import com.xxl.job.core.context.XxlJobHelper;
import com.xxl.job.core.handler.annotation.XxlJob;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;

import javax.annotation.Resource;
import java.util.Date;
import java.util.List;

@Slf4j
@Component
public class PageviewTask {
    @Resource
    private TrackPageviewGroupService trackPageviewGroupService;

    /**
     * 定时刷新缓存菜单数据
     */
    @XxlJob("refreshAllPageviewGroupInfo")
    public void refreshAllPageviewGroupInfo()  {
        XxlJobHelper.log("定时pv/uv分组统计数据[全表] refreshAllPageviewGroupInfo ");
        try {
            trackPageviewGroupService.refreshPageViewGroup();
            XxlJobHelper.handleSuccess();
        } catch (Exception e) {
            XxlJobHelper.handleFail(e.getMessage());
            XxlJobHelper.log("定时pv/uv分组统计数据[全表] refreshAllPageviewGroupInfo 失败", e);
        }
        XxlJobHelper.log("定时pv/uv分组统计数据[全表] refreshAllPageviewGroupInfo 结束");
    }

    @XxlJob("refreshTheDayPageviewGroupInfo")
    public void refreshTheDayPageviewGroupInfo()  {
        XxlJobHelper.log("定时pv/uv分组统计数据 [当天] refreshTheDayPageviewGroupInfo ");
        try {
            trackPageviewGroupService.refreshPageViewGroupByDateRange(DateUtil.beginOfDay(new Date()),DateUtil.endOfDay(new Date()));
            XxlJobHelper.handleSuccess();
        } catch (Exception e) {
            XxlJobHelper.handleFail(e.getMessage());
            XxlJobHelper.log("定时pv/uv分组统计数据[当天] refreshTheDayPageviewGroupInfo 失败", e);
        }
        XxlJobHelper.log("定时pv/uv分组统计数据[当天] refreshTheDayPageviewGroupInfo 结束");
    }
    @XxlJob("refreshPageViewGroupByAppId")
    public void refreshPageViewGroupByAppId()  {
        // 获取参数
        String appId = XxlJobHelper.getJobParam();
        XxlJobHelper.log("根据appId: {} 刷新数据 refreshPageViewGroupByAppId",appId);
        try {
            trackPageviewGroupService.refreshPageViewGroupByAppId(appId);
            XxlJobHelper.handleSuccess();
        } catch (Exception e) {
            XxlJobHelper.handleFail(e.getMessage());
            XxlJobHelper.log("根据appId: {} 刷新数据 refreshPageViewGroupByAppId 失败",appId, e);
        }
        XxlJobHelper.log("根据appId: {} 刷新数据 refreshPageViewGroupByAppId 结束",appId);
    }
}




    /**
     * 根据appId 刷新数据
     * @param appId appId
     */
    void refreshPageViewGroupByAppId(String appId);













```







```java
    @Override
    public void refreshPageViewGroupByAppId(String appId) {
        List<TrackAppIdEnum> appIdEnums = Arrays.stream(TrackAppIdEnum.values()).filter(v -> v.getAppId().equals(appId)).collect(Collectors.toList());
        if (CollectionUtils.isNotEmpty(appIdEnums)) {
            TrackAppIdEnum trackAppIdEnum = appIdEnums.get(0);
            doRefreshPageViewGroup(trackAppIdEnum.getAppId(),null,null,false);
            doRefreshPageviewGroupRel(trackAppIdEnum.getAppId(),null,null,false);
        }
    }

```



































