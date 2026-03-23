



# 1030需求开发


| <font style="color:rgb(23, 43, 77);">重新处置  【more】</font> | <font style="color:rgb(23, 43, 77);">曹仁红</font> | <font style="color:rgb(23, 43, 77);">曹仁红，万子聪</font> | <font style="color:rgb(23, 43, 77);">SDV1:</font><br/><font style="color:rgb(23, 43, 77);">SDV2:</font><br/><font style="color:rgb(23, 43, 77);">SDV3:</font> |
| :--- | :--- | :--- | :--- |
| <font style="color:rgb(23, 43, 77);">支持上报渠道打回，将原事件重新打开继续处理。【先做 less】</font> | <font style="color:rgb(23, 43, 77);">万子聪</font> | <font style="color:rgb(23, 43, 77);">   </font> | <font style="color:rgb(23, 43, 77);">SDV1:</font><br/><font style="color:rgb(23, 43, 77);">SDV2:</font><br/><font style="color:rgb(23, 43, 77);">SDV3:</font> |




杜恒： 上报打回呢个不需要开发，到时候测试配置下就行，你到时候跟下就行，重新重置易鹏会把方案放到这个链接，你关注下、

需求开发环境： shinemo

设计文档： [https://www.kdocs.cn/l/cnpG33OnqsjX](https://www.kdocs.cn/l/cnpG33OnqsjX)

需求概览： [https://docs.qq.com/sheet/DSHFQeGFSUmxOWWd0?tab=nns4am&_t=1665287977209](https://docs.qq.com/sheet/DSHFQeGFSUmxOWWd0?tab=nns4am&_t=1665287977209)

wiki信息： 





| [RR2022081000982](https://clouddevops.huawei.com/) | <font style="color:#000000;">重新处置</font> | <font style="color:#000000;">需求背景   </font><font style="color:#000000;">湖北荆门城市大脑项目中，城运中台与软通智慧城运一体化平台在苏州openlab实验室进行预集成验证   </font><font style="color:#000000;">需求价值      </font><font style="color:#000000;">客户价值   </font><font style="color:#000000;">完成项目城运中台与城运一体化平台预集成验证，降低项目交付风险      </font><font style="color:#000000;">产品价值   </font><font style="color:#000000;">完善产品功能，增强产品竞争力      </font><font style="color:#000000;">需求描述   </font><font style="color:#000000;">重新处置场景，建议是原批次分拨处置对象，重新处理</font> | <font style="color:#000000;">荆门项目,解决方案框招</font> | <font style="color:#000000;">30</font> | | <font style="color:#000000;">22.10.0</font> | <font style="color:#000000;">跟版本走</font> | <font style="color:#000000;">明确退回审核流程   </font><font style="color:#000000;">荆门有明确方案</font> | <font style="color:#000000;">潘峰</font> | <font style="color:#000000;">曹仁红,万子聪</font> | | | <font style="color:#000000;">已评审</font> | <font style="color:#000000;">已澄清</font> | <font style="color:#000000;">讯盟</font> |
| :--- | :--- | :--- | :--- | :--- | --- | :--- | :--- | :--- | :--- | :--- | --- | --- | :--- | :--- | :--- |
| [RR2022062100649](https://clouddevops.huawei.com/) | <font style="color:#000000;">支持上报渠道打回，将原事件重新打开继续处理。</font> | <font style="color:#000000;">#### 需求背景   </font><font style="color:#000000;">当前基础表有个字段rowGuid，用于存放源系统（上报系统的id），当事件在业务中台闭环后，源系统打回，如处置不通过需要重新处置，这时在业务中台会产生两个事件，但对于源系统来说，它是同一个事件。      </font><font style="color:#000000;">#### 需求描述   </font><font style="color:#000000;">当外部上报渠道上报的事件，对在业务中台中闭环后的事件打回后，需要重新打开原事件，继续处理。      </font><font style="color:#000000;">举例：12345派单给区，区处置完成后反馈给12345，12345审核不通过，要求重新处置，这时在业务中台会有两个事件，在实际业务中希望它是1个单；      </font><font style="color:#000000;">盐城还有抽查，即在市一级也办结了，当抽查不合格也需要退回重新处置。   </font><font style="color:#000000;">这种情况，事件需要归一、重新打开，重新处理。流程上，可以重新再走一遍流程。</font> | <font style="color:#000000;">盐城项目,解决方案框招</font> | <font style="color:#000000;">0</font> | | <font style="color:#000000;">22.10.0</font> | <font style="color:#000000;">跟版本走</font> | <font style="color:#000000;">退回流程添加渠道确认环节   </font><font style="color:#000000;">通过审核流程实现</font> | <font style="color:#000000;">林国钱</font> | | <font style="color:#000000;">同夏波总讨论后，抽查场景需要对已经办结了的事件能够继续处理，秀伟哥说当前先不支持抽查场景。目前按照配置渠道审核环节已满足该需求</font> | | <font style="color:#000000;">已评审</font> | <font style="color:#000000;">待澄清</font> | <font style="color:#000000;">讯盟</font> |




国钱给的

[城市治理aPaaS业务特性设计说明书-开放能力+-+1030.docx](https://www.yuque.com/attachments/yuque/0/2024/docx/21382055/1715921134516-3ac41b14-e561-4026-8580-be7713def212.docx)



[城市治理aPaaS业务特性设计说明书-开放能力+-+1030(2).docx](https://www.yuque.com/attachments/yuque/0/2024/docx/21382055/1715921134608-3666035a-7dfd-4e99-a3cf-da17c5a5385a.docx)



开会讨论：

[重新处置方案.pptx](https://www.yuque.com/attachments/yuque/0/2024/pptx/21382055/1715921134707-c2e37d0a-3ccf-47d1-b1d8-8897a3579c55.pptx)







代码定位：

```javascript
实例运行BO
SmartCity3__TaskService  
开启审批流程
91 行
if (approvalFalg) {	
}

SmartCity3__CompleteTaskV2
是否是新流程逻辑 198
if (isNewBusinessProcess) {
  
}

SmartCity3__ApprovalTaskAction
层级节点审批
163 行

 





```



新流程支持：审批拒绝后  支持重新处置

不同级别处置



<font style="color:rgb(51, 51, 51);">新分拨流程带回访</font>

<font style="color:rgb(44, 48, 61);">CloseApproveTemp</font>

<font style="color:rgb(51, 51, 51);">PresetDispatchProcess10</font>





```json
上报
{ 
    "caseName": "回访",
    "srcCaseId": "string",
    "itemCode": "ceshixiapai",
    "description": "回访",
    "occurrenceDate": "2022-08-04",
    "address": "杭州",
    "longitude": "120.999999",
    "latitude": "38.9999",
    "gridCode": "NANZHUANG001",
    "channelType": "000",
    "channelId": "string",
    "subject":"qqq",
    "reportPersonalInfo": {
        "contactName": "123456",
        "mobilePhone": "123456",
        "needReVisit": "N"
    },
    "severityLevel": "1",
    "urgencyLevel": "1",
    "tagCodes": [
        "string"
    ],
    "handlingUser": {
        "orgCode": "dyzd", 
        "orgName": "第一中队", 
        "postCode": "dyczy", 
        "postName": "第一中队处置员", 
        "userCode": "por_shi01", 
        "userName": "por_shi01" 
  },
    "dutyOrgs": [],
    "extFieldValues": [ 
    ] 
}

立案
{
    "extFieldValues": [
        {
            "fieldName": "TASK_TYPE_CHECK",
            "fieldValue": "Y"
        }
    ],
    "action": "file",
    "comment": "好",
    "handlingUser": {
         "orgCode": "chanchengqufenbozhongxin",
         "orgName": "禅城区分拨中心",
         "postCode": "chanchengqufenbozhongxinzuoxiyuan",
         "postName": "禅城区分拨中心坐席员",
          "userCode": "wangminjie",
         "userName": "wangminjie"
    },
    "taskId": "c60G000000xy1acrp4EK"
}

分拨
{
    "handlingUser": {
         "orgCode": "chanchengqufenbozhongxin",
                    "orgName": "禅城区分拨中心",
                    "postCode": "chanchengqufenbozhongxinzuoxiyuan",
                    "postName": "禅城区分拨中心坐席员",
                    "userCode": "wangminjie",
                    "userName": "wangminjie"
    },
    "caseCode": "2022102700075",
    "taskType": "TASK_TYPE_DISPATCH",
    "comment": "分拨",
    "attachments": [
        {
            "attachmentName": "bdlogo.png",
            "attachmentUrl": "http://www.baidu.com/img/bdlogo.png"
        }
    ],
    "executorType": "Organization",
    "isCompulsive": "N",
    "cooperationType": "MainCo",
    "executors": [
        {
            "isMaster": "Y",
            "orderNo": 1,
              "orgCode": "ccqgaj",
                    "orgName": "禅城区公安局",
                    "postCode": "0571",
                    "postName": "处置员",
                    "userCode": "sync001",
                    "userName": "sync001"
        }
    ]
} 



处置反馈
{
    "extFieldValues": [
        {
            "fieldName": "TASK_TYPE_CHECK",
            "fieldValue": "Y"
        }
    ],
    "action": "enforce",
    "comment": "处置反馈",
    "handlingUser": {
        "orgCode": "ccqgaj",
                    "orgName": "禅城区公安局",
                    "postCode": "0571",
                    "postName": "处置员",
                    "userCode": "sync001",
                    "userName": "sync001"
    },
    "taskId": "c60G000000xy3vbXd2Om"
}


结案
{
    "extFieldValues": [
        {
            "fieldName": "TASK_TYPE_CHECK",
            "fieldValue": "Y"
        }
    ],
    "action": "close",
    "comment": "结案",
    "handlingUser": {
         "orgCode": "chanchengqufenbozhongxin",
                    "orgName": "禅城区分拨中心",
                    "postCode": "chanchengqufenbozhongxinzuoxiyuan",
                    "postName": "禅城区分拨中心坐席员",
                    "userCode": "chanchengqu_chuzhi2",
                    "userName": "chanchengqu_chuzhi2"
    },
    "taskId": "c60G000000xy34WrbhmC"
}


审核通过
{
    "extFieldValues": [
        {
            "fieldName": "TASK_TYPE_CHECK",
            "fieldValue": "Y"
        }
    ],
    "action": "approve",
    "comment": "审核通过",
    "handlingUser": {
          "orgCode": "chanchengqufenbozhongxin",
                    "orgName": "禅城区分拨中心",
                    "postCode": "chanchengqufenbozhongxinzuoxiyuan",
                    "postName": "禅城区分拨中心坐席员",
                    "userCode": "chanchengqu_shangbao",
                    "userName": "chanchengqu_shangbao"
    },
    "taskId": "c60G000000xy11eLX7iq"
}

审核不通过
{
    "extFieldValues": [
        {
            "fieldName": "TASK_TYPE_CHECK",
            "fieldValue": "Y"
        }
    ],
    "action": "reject",
    "comment": "审核不通过",
    "handlingUser": {
          "orgCode": "chanchengqufenbozhongxin",
                    "orgName": "禅城区分拨中心",
                    "postCode": "chanchengqufenbozhongxinzuoxiyuan",
                    "postName": "禅城区分拨中心坐席员",
                    "userCode": "chanchengqu_shangbao",
                    "userName": "chanchengqu_shangbao"
    },
    "taskId": "c60G000000xy36kMqHa4"
}
```





<font style="color:#a31515;background-color:#fffffe;">"handlingUser"</font><font style="color:#000000;background-color:#fffffe;">: {</font>

<font style="color:#000000;background-color:#fffffe;">        </font><font style="color:#a31515;background-color:#fffffe;">"orgCode"</font><font style="color:#000000;background-color:#fffffe;">: </font><font style="color:#0451a5;background-color:#fffffe;">"zumiaojiedaochengguan"</font><font style="color:#000000;background-color:#fffffe;">, </font>

<font style="color:#000000;background-color:#fffffe;">        </font><font style="color:#a31515;background-color:#fffffe;">"orgName"</font><font style="color:#000000;background-color:#fffffe;">: </font><font style="color:#0451a5;background-color:#fffffe;">"祖庙街道城管"</font><font style="color:#000000;background-color:#fffffe;">, </font>

<font style="color:#000000;background-color:#fffffe;">        </font><font style="color:#a31515;background-color:#fffffe;">"postCode"</font><font style="color:#000000;background-color:#fffffe;">: </font><font style="color:#0451a5;background-color:#fffffe;">"zumiaochengguanzhifagang"</font><font style="color:#000000;background-color:#fffffe;">, </font>

<font style="color:#000000;background-color:#fffffe;">        </font><font style="color:#a31515;background-color:#fffffe;">"postName"</font><font style="color:#000000;background-color:#fffffe;">: </font><font style="color:#0451a5;background-color:#fffffe;">"城管执法岗"</font><font style="color:#000000;background-color:#fffffe;">, </font>

<font style="color:#000000;background-color:#fffffe;">        </font><font style="color:#a31515;background-color:#fffffe;">"userCode"</font><font style="color:#000000;background-color:#fffffe;">: </font><font style="color:#0451a5;background-color:#fffffe;">"nieguochen_yewu"</font><font style="color:#000000;background-color:#fffffe;">, </font>

<font style="color:#000000;background-color:#fffffe;">        </font><font style="color:#a31515;background-color:#fffffe;">"userName"</font><font style="color:#000000;background-color:#fffffe;">: </font><font style="color:#0451a5;background-color:#fffffe;">"nieguochen_yewu"</font><font style="color:#000000;background-color:#fffffe;"> </font>

<font style="color:#000000;background-color:#fffffe;">  },</font>



结案 街道

<font style="color:#000000;background-color:#fffffe;"> </font><font style="color:#a31515;background-color:#fffffe;">"orgCode"</font><font style="color:#000000;background-color:#fffffe;">: </font><font style="color:#0451a5;background-color:#fffffe;">"zumiaojiedaopaichusuo"</font><font style="color:#000000;background-color:#fffffe;">,</font>

<font style="color:#000000;background-color:#fffffe;">                    </font><font style="color:#a31515;background-color:#fffffe;">"orgName"</font><font style="color:#000000;background-color:#fffffe;">: </font><font style="color:#0451a5;background-color:#fffffe;">"祖庙街道派出所"</font><font style="color:#000000;background-color:#fffffe;">,</font>

<font style="color:#000000;background-color:#fffffe;">                    </font><font style="color:#a31515;background-color:#fffffe;">"postCode"</font><font style="color:#000000;background-color:#fffffe;">: </font><font style="color:#0451a5;background-color:#fffffe;">"zumiaopaichusuowaiqingang"</font><font style="color:#000000;background-color:#fffffe;">,</font>

<font style="color:#000000;background-color:#fffffe;">                    </font><font style="color:#a31515;background-color:#fffffe;">"postName"</font><font style="color:#000000;background-color:#fffffe;">: </font><font style="color:#0451a5;background-color:#fffffe;">"外勤岗"</font><font style="color:#000000;background-color:#fffffe;">,</font>

<font style="color:#000000;background-color:#fffffe;">                    </font><font style="color:#a31515;background-color:#fffffe;">"userCode"</font><font style="color:#000000;background-color:#fffffe;">: </font><font style="color:#0451a5;background-color:#fffffe;">"nieguochen_chuzhi"</font><font style="color:#000000;background-color:#fffffe;">,</font>

<font style="color:#000000;background-color:#fffffe;">                    </font><font style="color:#a31515;background-color:#fffffe;">"userName"</font><font style="color:#000000;background-color:#fffffe;">: </font><font style="color:#0451a5;background-color:#fffffe;">"nieguochen_chuzhi"</font>



审核 街道：

<font style="color:#000000;background-color:#fffffe;">  </font><font style="color:#a31515;background-color:#fffffe;">"orgCode"</font><font style="color:#000000;background-color:#fffffe;">: </font><font style="color:#0451a5;background-color:#fffffe;">"zumiaojiedaopaichusuo"</font><font style="color:#000000;background-color:#fffffe;">,</font>

<font style="color:#000000;background-color:#fffffe;">                    </font><font style="color:#a31515;background-color:#fffffe;">"orgName"</font><font style="color:#000000;background-color:#fffffe;">: </font><font style="color:#0451a5;background-color:#fffffe;">"祖庙街道派出所"</font><font style="color:#000000;background-color:#fffffe;">,</font>

<font style="color:#000000;background-color:#fffffe;">                    </font><font style="color:#a31515;background-color:#fffffe;">"postCode"</font><font style="color:#000000;background-color:#fffffe;">: </font><font style="color:#0451a5;background-color:#fffffe;">"zumiaopaichusuowaiqingang"</font><font style="color:#000000;background-color:#fffffe;">,</font>

<font style="color:#000000;background-color:#fffffe;">                    </font><font style="color:#a31515;background-color:#fffffe;">"postName"</font><font style="color:#000000;background-color:#fffffe;">: </font><font style="color:#0451a5;background-color:#fffffe;">"外勤岗"</font><font style="color:#000000;background-color:#fffffe;">,</font>

<font style="color:#000000;background-color:#fffffe;">                    </font><font style="color:#a31515;background-color:#fffffe;">"userCode"</font><font style="color:#000000;background-color:#fffffe;">: </font><font style="color:#0451a5;background-color:#fffffe;">"nieguochen_yewu"</font><font style="color:#000000;background-color:#fffffe;">,</font>

<font style="color:#000000;background-color:#fffffe;">                    </font><font style="color:#a31515;background-color:#fffffe;">"userName"</font><font style="color:#000000;background-color:#fffffe;">: </font><font style="color:#0451a5;background-color:#fffffe;">"nieguochen_yewu"</font>





<font style="color:#000000;background-color:#fffffe;"> 		    </font><font style="color:#a31515;background-color:#fffffe;">"orgCode"</font><font style="color:#000000;background-color:#fffffe;">: </font><font style="color:#0451a5;background-color:#fffffe;">"ceshibumen3"</font><font style="color:#000000;background-color:#fffffe;">,</font>

<font style="color:#000000;background-color:#fffffe;">                    </font><font style="color:#a31515;background-color:#fffffe;">"orgName"</font><font style="color:#000000;background-color:#fffffe;">: </font><font style="color:#0451a5;background-color:#fffffe;">"测试部门3"</font><font style="color:#000000;background-color:#fffffe;">,</font>

<font style="color:#000000;background-color:#fffffe;">                    </font><font style="color:#a31515;background-color:#fffffe;">"postCode"</font><font style="color:#000000;background-color:#fffffe;">: </font><font style="color:#0451a5;background-color:#fffffe;">"ceshigangwei3"</font><font style="color:#000000;background-color:#fffffe;">,</font>

<font style="color:#000000;background-color:#fffffe;">                    </font><font style="color:#a31515;background-color:#fffffe;">"postName"</font><font style="color:#000000;background-color:#fffffe;">: </font><font style="color:#0451a5;background-color:#fffffe;">"测试岗位3"</font><font style="color:#000000;background-color:#fffffe;">,</font>

<font style="color:#000000;background-color:#fffffe;">                    </font><font style="color:#a31515;background-color:#fffffe;">"userCode"</font><font style="color:#000000;background-color:#fffffe;">: </font>**<font style="color:#0451a5;background-color:#fffffe;">"</font>**<font style="color:rgb(0, 0, 0);background-color:rgb(245, 247, 250);">wanzicong1</font>**<font style="color:#0451a5;background-color:#fffffe;">"</font>**<font style="color:#000000;background-color:#fffffe;">,</font>

<font style="color:#000000;background-color:#fffffe;">                    </font><font style="color:#a31515;background-color:#fffffe;">"userName"</font><font style="color:#000000;background-color:#fffffe;">: </font>**<font style="color:#0451a5;background-color:#fffffe;">"</font>**<font style="color:rgb(0, 0, 0);background-color:rgb(245, 247, 250);">wanzicong1</font>**<font style="color:#0451a5;background-color:#fffffe;">"</font>**







39 环境

[https://wiki.shinemo.com/pages/viewpage.action?pageId=88762022](https://wiki.shinemo.com/pages/viewpage.action?pageId=88762022)



















































































































































