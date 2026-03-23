# 环境信息记录
<details class="lake-collapse"><summary id="u06c1b186"><span class="ne-text">shinemo 开发环境 token</span></summary><p id="ue19d1652" class="ne-p"><span class="ne-text">username,client_id,client_secret</span></p><p id="ud0e874a6" class="ne-p"><span class="ne-text">wangjie</span></p><p id="ua4e4fce9" class="ne-p"><span class="ne-text">6f364ed918b344909e054a3450ad3a6b</span></p><p id="u5f6b9ebe" class="ne-p"><span class="ne-text">62eea9b3855fcd5cb3071d5db76605bc913abfa121557688</span></p><p id="ucd77c4c7" class="ne-p"><span class="ne-text"></span></p><p id="u1d977f24" class="ne-p"><span class="ne-text">shinemo 开发子账号</span></p><p id="u1c4d653d" class="ne-p"><span class="ne-text">wanzicong</span></p><p id="u53be68dc" class="ne-p"><span class="ne-text">@Www19980818</span></p><p id="ucc5cb4b7" class="ne-p"><span class="ne-text"></span></p><p id="uccf1c34b" class="ne-p"><span class="ne-text">十堰堡垒机appcube 登录</span></p><p id="ue0411c61" class="ne-p" style="text-align: left"><span class="ne-text" style="color: #000000; font-size: 16px">zww_zhihuichengshi</span></p><p id="u80e3cc6e" class="ne-p" style="text-align: left"><span class="ne-text" style="color: #000000; font-size: 16px">APPCube</span></p><p id="u74008be8" class="ne-p" style="text-align: left"><span class="ne-text" style="color: #000000; font-size: 16px">Huawei@2wsx1</span></p><p id="u247550bd" class="ne-p" style="text-align: left"><span class="ne-text">Huawei@2wsx11</span></p><p id="u5e1e3820" class="ne-p" style="text-align: left"><span class="ne-text" style="color: #000000; font-size: 16px"></span></p><p id="u04859af3" class="ne-p" style="text-align: left"><img src="https://cdn.nlark.com/yuque/0/2022/png/21382055/1665627169559-9094bbd6-270e-48e2-9601-767c2e0de599.png" width="489" title="" crop="0,0,1,1" id="NHbOw" class="ne-image"></p><p id="u664db5d1" class="ne-p" style="text-align: left"><span class="ne-text" style="color: #000000; font-size: 16px"></span></p><p id="u975efc45" class="ne-p" style="text-align: left"><span class="ne-text" style="color: #000000; font-size: 16px">十堰现场测试环境 token</span></p><p id="u99033b3e" class="ne-p" style="text-align: left"><span class="ne-text">username,client_id,client_secret</span></p><p id="u7b9194d3" class="ne-p"><span class="ne-text">APPCube</span></p><p id="ub0e3a6ff" class="ne-p"><span class="ne-text">540d2828d20344b3bfaf706616e57adf</span></p><p id="u31fa967c" class="ne-p"><span class="ne-text">9a90abbfb47f95ee5af83f61a7d34cc30ca2993f2593b96e</span></p><p id="ue6df5f77" class="ne-p"><span class="ne-text"></span></p><p id="uf879ada7" class="ne-p"><span class="ne-text">荆门堡垒机登录appcube 账号和密码</span></p><p id="u2ea4ba54" class="ne-p"><a href="https://10.65.32.34/studio/index.html#/admin" data-href="https://10.65.32.34/studio/index.html#/admin" target="_blank" class="ne-link"><span class="ne-text">https://10.65.32.34/studio/index.html#/admin</span></a></p><p id="u7fe3f2e5" class="ne-p"><span class="ne-text">账号AppCube_admin </span></p><p id="u91a6cc42" class="ne-p"><span class="ne-text">密码： Huawei123#$%</span></p><p id="u8ad36389" class="ne-p"><span class="ne-text">AppCube_cyzt    密码 Jmcsdn&amp;013</span></p><p id="u5c4d5336" class="ne-p"><br></p><p id="u02b75837" class="ne-p"><span class="ne-text">appcube1 沙箱环境账号</span></p><p id="u6caa747f" class="ne-p"><span class="ne-text">username,client_id,client_secret</span></p><p id="u502ade3b" class="ne-p"><span class="ne-text">nieguochen_jj,</span></p><p id="u58b6a346" class="ne-p"><span class="ne-text">398418bcac2e43efa679241fca6c62e2</span></p><p id="u8496b3a6" class="ne-p"><span class="ne-text">e8a1ec700a18448f005c33b514806a40c1427b99d69d1556</span></p><p id="u7e9e9b0c" class="ne-p"><span class="ne-text"></span></p><p id="ubd506743" class="ne-p"><br></p><p id="ufb9b4351" class="ne-p"><br></p></details>




# Postman 小技巧
```javascript
var data = JSON.parse(responseBody);

pm.environment.set("access-token", data.access_token);
```





<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2022/png/21382055/1665978037879-21c399bf-9d62-45cf-8584-8d6f06576939.png)







# 十堰水库流程测试
```json
let taskDefineList = [
                // {
                //     "name": "任务定义英文名称",
                //     "taskType": "任务类型",
                //     "taskLabel": "任务定义中文名称",
                //     "description": "描述",
                //     "allowedActions": "支持的动作"
                // },
                {
                    "name": "report",
                    "taskType": "TASK_TYPE_REPORT",
                    "taskLabel": "上报",
                    "description": "事件进行上报",
                    "allowedActions": "report"
                },
                {
                    "name": "accept",
                    "taskType": "TASK_TYPE_ACCEPT",
                    "taskLabel": "受理",
                    "description": "核对事件是否符合受理标准。",
                    "allowedActions": "accept,disuse"
                },
                {
                    "name": "file",
                    "taskType": "TASK_TYPE_FILE",
                    "taskLabel": "立案",
                    "description": "核对事件是否符合立案标准。",
                    "allowedActions": "file,disuse,toVerify"
                },
                {
                    "name": "verify",
                    "taskType": "TASK_TYPE_VERIFY",
                    "taskLabel": "核实",
                    "description": "核实事件是否属实。",
                    "allowedActions": "verify"
                },
                {
                    "name": "dispatch",
                    "taskType": "TASK_TYPE_DISPATCH",
                    "taskLabel": "派遣",
                    "description": "派遣工单给处置部门进行处置。",
                    "allowedActions": "dispatch,recall,additionalDispatch,terminate"
                },
                {
                    "name": "treat",
                    "taskType": "TASK_TYPE_TREAT",
                    "taskLabel": "处置",
                    "description": "处置任务",
                    "allowedActions": "enforce,return,delay,toUpDispose,noVerify,transfer,notTransfer"
                },
                {
                    "name": "review",
                    "taskType": "TASK_TYPE_REVIEW",
                    "taskLabel": "结案审核",
                    "description": "审核事件是否可以结案。",
                    "allowedActions": "re-enforce,close,toCheck"
                },
                {
                    "name": "visit",
                    "taskType": "TASK_TYPE_VISIT",
                    "taskLabel": "回访",
                    "description": "回访",
                    "allowedActions": "visit,skipVisit"
                },
                {
                    "name": "check",
                    "taskType": "TASK_TYPE_CHECK",
                    "taskLabel": "核查",
                    "description": "核查事件处置结果。",
                    "allowedActions": "check"
                },
                {
                    "name": "audit",
                    "taskType": "TASK_TYPE_AUDIT",
                    "taskLabel": "审核",
                    "description": "对部门提交的处置结果进行审核。",
                    "allowedActions": "approve,reject"
                },
                {
                    "name": "reply",
                    "taskType": "TASK_TYPE_REPLY",
                    "taskLabel": "初步反馈",
                    "description": "对工单进行初步答复。",
                    "allowedActions": "initialReply"
                },
                {
                    "name": "feedback",
                    "taskType": "TASK_TYPE_FEEDBACK",
                    "taskLabel": "处置反馈",
                    "description": "对处置结果进行反馈。",
                    "allowedActions": "feedback"
                },

                // 930 审核需求加入
                {
                    "name": "audit",
                    "taskType": "TASK_TYPE_AUDIT",
                    "taskLabel": "处置部门审批",
                    "description": "处置部门审批。",
                    "allowedActions": "approve,reject"
                },
                {
                    "name": "audit",
                    "taskType": "TASK_TYPE_AUDIT",
                    "taskLabel": "分拨部门审批",
                    "description": "分拨部门审批。",
                    "allowedActions": "approve,reject"
                },
                {
                    "name": "audit",
                    "taskType": "TASK_TYPE_AUDIT",
                    "taskLabel": "第三方系统审批",
                    "description": "第三方系统审批。",
                    "allowedActions": "approve,reject"
                }
            ];
let taskQuoteList = [

                {
                    "taskType": "TASK_TYPE_REPORT",
                    "taskAliasLabel": "待上报",
                    "channelType": "000"
                },
                {
                    "taskType": "TASK_TYPE_REPORT",
                    "taskAliasLabel": "待上报",
                    "channelType": "001"
                },
                {
                    "taskType": "TASK_TYPE_REPORT",
                    "taskAliasLabel": "待上报",
                    "channelType": "002"
                },
                {
                    "taskType": "TASK_TYPE_REPORT",
                    "taskAliasLabel": "待上报",
                    "channelType": "003"
                },
                {
                    "taskType": "TASK_TYPE_REPORT",
                    "taskAliasLabel": "待上报",
                    "channelType": "004"
                },
                // {
                //     "taskType": "任务类型",
                //     "taskAliasLabel": "任务别名",
                // },

                // 930审核需求加入
                {
                    "taskType": "TASK_TYPE_AUDIT",
                    "taskAliasLabel": "处置部门审批",
                    "channelType": "000"
                },
                {
                    "taskType": "TASK_TYPE_AUDIT",
                    "taskAliasLabel": "处置部门审批",
                    "channelType": "001"
                },
                {
                    "taskType": "TASK_TYPE_AUDIT",
                    "taskAliasLabel": "处置部门审批",
                    "channelType": "002"
                },
                {
                    "taskType": "TASK_TYPE_AUDIT",
                    "taskAliasLabel": "处置部门审批",
                    "channelType": "003"
                },
                {
                    "taskType": "TASK_TYPE_AUDIT",
                    "taskAliasLabel": "处置部门审批",
                    "channelType": "004"
                },

                {
                    "taskType": "TASK_TYPE_AUDIT",
                    "taskAliasLabel": "分拨部门审批",
                    "channelType": "000"
                },
                {
                    "taskType": "TASK_TYPE_AUDIT",
                    "taskAliasLabel": "分拨部门审批",
                    "channelType": "001"
                },
                {
                    "taskType": "TASK_TYPE_AUDIT",
                    "taskAliasLabel": "分拨部门审批",
                    "channelType": "002"
                },
                {
                    "taskType": "TASK_TYPE_AUDIT",
                    "taskAliasLabel": "分拨部门审批",
                    "channelType": "003"
                },
                {
                    "taskType": "TASK_TYPE_AUDIT",
                    "taskAliasLabel": "分拨部门审批",
                    "channelType": "004"
                },


                {
                    "taskType": "TASK_TYPE_AUDIT",
                    "taskAliasLabel": "第三方系统审批",
                    "channelType": "000"
                },
                {
                    "taskType": "TASK_TYPE_AUDIT",
                    "taskAliasLabel": "第三方系统审批",
                    "channelType": "001"
                },
                {
                    "taskType": "TASK_TYPE_AUDIT",
                    "taskAliasLabel": "第三方系统审批",
                    "channelType": "002"
                },
                {
                    "taskType": "TASK_TYPE_AUDIT",
                    "taskAliasLabel": "第三方系统审批",
                    "channelType": "003"
                },
                {
                    "taskType": "TASK_TYPE_AUDIT",
                    "taskAliasLabel": "第三方系统审批",
                    "channelType": "004"
                },


                {
                    "taskType": "TASK_TYPE_REPORT",
                    "taskAliasLabel": "上报",
                    "channelType": "000"
                },
                {
                    "taskType": "TASK_TYPE_REPORT",
                    "taskAliasLabel": "上报",
                    "channelType": "001"
                },
                {
                    "taskType": "TASK_TYPE_REPORT",
                    "taskAliasLabel": "上报",
                    "channelType": "002"
                },
                {
                    "taskType": "TASK_TYPE_REPORT",
                    "taskAliasLabel": "上报",
                    "channelType": "003"
                },
                {
                    "taskType": "TASK_TYPE_VISIT",
                    "taskAliasLabel": "回访",
                    "channelType": "001"
                },
                {
                    "taskType": "TASK_TYPE_REVIEW",
                    "taskAliasLabel": "结果审核",
                    "channelType": "001"
                },
                {
                    "taskType": "TASK_TYPE_REPORT",
                    "taskAliasLabel": "上报",
                    "channelType": "004"
                },
                {
                    "taskType": "TASK_TYPE_TREAT",
                    "taskAliasLabel": "技术责任人",
                    "channelType": "001"
                }, {
                    "taskType": "TASK_TYPE_TREAT",
                    "taskAliasLabel": "主管责任人",
                    "channelType": "001"
                }, {
                    "taskType": "TASK_TYPE_TREAT",
                    "taskAliasLabel": "行政处置",
                    "channelType": "001"
                }, {
                    "taskType": "TASK_TYPE_TREAT",
                    "taskAliasLabel": "防汛副指挥长",
                    "channelType": "001"
                }, {
                    "taskType": "TASK_TYPE_TREAT",
                    "taskAliasLabel": "县自规局科股长",
                    "channelType": "001"
                },
                {
                    "taskType": "TASK_TYPE_TREAT",
                    "taskAliasLabel": "街道办主任",
                    "channelType": "001"
                },
                {
                    "taskType": "TASK_TYPE_TREAT",
                    "taskAliasLabel": "市政规局处置",
                    "channelType": "001"
                },
                {
                    "taskType": "TASK_TYPE_TREAT",
                    "taskAliasLabel": "会商",
                    "channelType": "001"
                },
                {
                    "taskType": "TASK_TYPE_TREAT",
                    "taskAliasLabel": "转移",
                    "channelType": "001"
                },
                {
                    "taskType": "TASK_TYPE_ACCEPT",
                    "taskAliasLabel": "受理",
                    "channelType": "000"
                },
                {
                    "taskType": "TASK_TYPE_ACCEPT",
                    "taskAliasLabel": "受理",
                    "channelType": "001"
                },
                {
                    "taskType": "TASK_TYPE_ACCEPT",
                    "taskAliasLabel": "受理",
                    "channelType": "002"
                },
                {
                    "taskType": "TASK_TYPE_ACCEPT",
                    "taskAliasLabel": "受理",
                    "channelType": "003"
                },
                {
                    "taskType": "TASK_TYPE_ACCEPT",
                    "taskAliasLabel": "受理",
                    "channelType": "004"
                },
                {
                    "taskType": "TASK_TYPE_FILE",
                    "taskAliasLabel": "立案",
                    "channelType": "000"
                },
                {
                    "taskType": "TASK_TYPE_FILE",
                    "taskAliasLabel": "立案",
                    "channelType": "001"
                },
                {
                    "taskType": "TASK_TYPE_FILE",
                    "taskAliasLabel": "立案",
                    "channelType": "002"
                },
                {
                    "taskType": "TASK_TYPE_FILE",
                    "taskAliasLabel": "立案",
                    "channelType": "003"
                },
                {
                    "taskType": "TASK_TYPE_FILE",
                    "taskAliasLabel": "立案",
                    "channelType": "004"
                },
                {
                    "taskType": "TASK_TYPE_VERIFY",
                    "taskAliasLabel": "核实",
                    "channelType": "000"
                },
                {
                    "taskType": "TASK_TYPE_VERIFY",
                    "taskAliasLabel": "核实",
                    "channelType": "001"
                },
                {
                    "taskType": "TASK_TYPE_VERIFY",
                    "taskAliasLabel": "核实",
                    "channelType": "002"
                },
                {
                    "taskType": "TASK_TYPE_VERIFY",
                    "taskAliasLabel": "核实",
                    "channelType": "003"
                },
                {
                    "taskType": "TASK_TYPE_VERIFY",
                    "taskAliasLabel": "核实",
                    "channelType": "004"
                },
                {
                    "taskType": "TASK_TYPE_DISPATCH",
                    "taskAliasLabel": "分拨",
                    "channelType": "000"
                },
                {
                    "taskType": "TASK_TYPE_DISPATCH",
                    "taskAliasLabel": "分拨",
                    "channelType": "001"
                },
                {
                    "taskType": "TASK_TYPE_DISPATCH",
                    "taskAliasLabel": "分拨",
                    "channelType": "002"
                },
                {
                    "taskType": "TASK_TYPE_DISPATCH",
                    "taskAliasLabel": "分拨",
                    "channelType": "003"
                },
                {
                    "taskType": "TASK_TYPE_DISPATCH",
                    "taskAliasLabel": "分拨",
                    "channelType": "004"
                },
                {
                    "taskType": "TASK_TYPE_TREAT",
                    "taskAliasLabel": "并行处置",
                    "channelType": "000"
                },
                {
                    "taskType": "TASK_TYPE_TREAT",
                    "taskAliasLabel": "并行处置",
                    "channelType": "001"
                },
                {
                    "taskType": "TASK_TYPE_TREAT",
                    "taskAliasLabel": "并行处置",
                    "channelType": "002"
                },
                {
                    "taskType": "TASK_TYPE_TREAT",
                    "taskAliasLabel": "并行处置",
                    "channelType": "003"
                },
                {
                    "taskType": "TASK_TYPE_TREAT",
                    "taskAliasLabel": "顺序处置",
                    "channelType": "000"
                },
                {
                    "taskType": "TASK_TYPE_TREAT",
                    "taskAliasLabel": "顺序处置",
                    "channelType": "001"
                },
                {
                    "taskType": "TASK_TYPE_TREAT",
                    "taskAliasLabel": "顺序处置",
                    "channelType": "002"
                },
                {
                    "taskType": "TASK_TYPE_TREAT",
                    "taskAliasLabel": "顺序处置",
                    "channelType": "003"
                },
                {
                    "taskType": "TASK_TYPE_REVIEW",
                    "taskAliasLabel": "结案",
                    "channelType": "000"
                },
                {
                    "taskType": "TASK_TYPE_REVIEW",
                    "taskAliasLabel": "结案",
                    "channelType": "001"
                },
                {
                    "taskType": "TASK_TYPE_REVIEW",
                    "taskAliasLabel": "结案",
                    "channelType": "002"
                },
                {
                    "taskType": "TASK_TYPE_REVIEW",
                    "taskAliasLabel": "结案",
                    "channelType": "003"
                },
                {
                    "taskType": "TASK_TYPE_REVIEW",
                    "taskAliasLabel": "判定核查结果",
                    "channelType": "000"
                },
                {
                    "taskType": "TASK_TYPE_REVIEW",
                    "taskAliasLabel": "判定核查结果",
                    "channelType": "001"
                },
                {
                    "taskType": "TASK_TYPE_REVIEW",
                    "taskAliasLabel": "判定核查结果",
                    "channelType": "002"
                },
                {
                    "taskType": "TASK_TYPE_REVIEW",
                    "taskAliasLabel": "判定核查结果",
                    "channelType": "003"
                },
                {
                    "taskType": "TASK_TYPE_CHECK",
                    "taskAliasLabel": "核查",
                    "channelType": "000"
                },
                {
                    "taskType": "TASK_TYPE_CHECK",
                    "taskAliasLabel": "核查",
                    "channelType": "001"
                },
                {
                    "taskType": "TASK_TYPE_CHECK",
                    "taskAliasLabel": "核查",
                    "channelType": "002"
                },
                {
                    "taskType": "TASK_TYPE_CHECK",
                    "taskAliasLabel": "核查",
                    "channelType": "003"
                },
                {
                    "taskType": "TASK_TYPE_CHECK",
                    "taskAliasLabel": "核查",
                    "channelType": "004"
                },
                {
                    "taskType": "TASK_TYPE_AUDIT",
                    "taskAliasLabel": "审核",
                    "channelType": "000"
                },
                {
                    "taskType": "TASK_TYPE_AUDIT",
                    "taskAliasLabel": "审核",
                    "channelType": "001"
                },
                {
                    "taskType": "TASK_TYPE_AUDIT",
                    "taskAliasLabel": "审核",
                    "channelType": "002"
                },
                {
                    "taskType": "TASK_TYPE_AUDIT",
                    "taskAliasLabel": "审核",
                    "channelType": "003"
                },
                {
                    "taskType": "TASK_TYPE_AUDIT",
                    "taskAliasLabel": "审核",
                    "channelType": "004"
                },
                {
                    "taskType": "TASK_TYPE_REPLY",
                    "taskAliasLabel": "初步反馈",
                    "channelType": "004"
                },
                {
                    "taskType": "TASK_TYPE_FEEDBACK",
                    "taskAliasLabel": "处置反馈",
                    "channelType": "004"
                }
            ];
```



<details class="lake-collapse"><summary id="ub57fe3d1"><span class="ne-text">山洪： 核实阶段去掉  </span></summary><p id="ue2e586e2" class="ne-p"><span class="ne-text">地灾： 会商人变成一个  会商节点需要配置   核实阶段没了</span></p></details>
## 水库流程
<details class="lake-collapse"><summary id="u038b8507"><span class="ne-text">配置：</span></summary><p id="u0fdc8dce" class="ne-p"><span class="ne-text">部门：十堰市, 郧西县，茅箭区，郧阳区</span></p><p id="ua11160d4" class="ne-p"><span class="ne-text">第一个测试： 水库巡查,   事项code ：skxc0052  不满足汛期值班、工程管护、物料储备的要求</span></p><p id="u7ce3faa5" class="ne-p"><span class="ne-text">select usrname,name from PortalUser where name = '用户名'</span></p><p id="u7a74379e" class="ne-p"><br></p><p id="uf5191a28" class="ne-p"><span class="ne-text">水库节点</span></p><p id="u6a9d3e54" class="ne-p"><span class="ne-text">上报---&gt; 处置 ----&gt; 初步处置 ---&gt; 上升处置 ---&gt; 疑难处置 ---&gt; 办结</span></p><p id="ubb79e4a5" class="ne-p"><img src="https://cdn.nlark.com/yuque/0/2022/png/21382055/1665477225946-6c472926-e8c2-4583-ac31-129b0ac4d8db.png" width="414" title="" crop="0,0,1,1" id="U5Ws7" class="ne-image"></p><p id="ub6e4dbcd" class="ne-p"><span class="ne-text"></span></p><p id="uff34bd2e" class="ne-p"><span class="ne-text">上报节点  casecode CY2022101100001</span></p><p id="u316e3af5" class="ne-p"><span class="ne-text"></span></p><p id="uccfe7087" class="ne-p"><span class="ne-text">   用户名称                              部门名称                 岗位名称</span></p><p id="u186c2f74" class="ne-p"><img src="https://cdn.nlark.com/yuque/0/2022/png/21382055/1665479549933-8c3ed83c-2b7a-4dd4-bcf4-5fdf2dbfb693.png" width="623" title="" crop="0,0,1,1" id="htRNA" class="ne-image"></p><p id="u28066e4e" class="ne-p"><span class="ne-text"></span></p><p id="u515488a4" class="ne-p"><span class="ne-text">部门 ： 11420300MB1934788X    市城管执法委     </span></p><p id="u83b5c5c8" class="ne-p"><span class="ne-text">岗位 ： SYSCGZFWCZRY   十堰市城管执法委处置人员  </span></p><p id="uae14a2d5" class="ne-p"><span class="ne-text">用户：  张性军  13872805560    {技术责任人编码  TechnicalPersonCode }    taskid  c60G000000xWFu1bY9Lc </span></p><p id="u1977499f" class="ne-p"><span class="ne-text"> |  余萍  18071950168   {主管责任人编码  SupervisorCode}     taskid  c60G000000xWFu6kssgC</span></p><p id="u81527e80" class="ne-p"><span class="ne-text"> |   万红  13886806330  {行政处置  AdministrativeCode }</span></p><p id="ufa720915" class="ne-p"><br></p></details>


<details class="lake-collapse"><summary id="u0f85abfb"><span class="ne-text">十堰市水库测试</span></summary><p id="uc7e1ab31" class="ne-p"><span class="ne-text">上报 reportcase </span></p><pre data-language="json" id="xTyLN" class="ne-codeblock language-json"><code>{ 
    &quot;caseName&quot;: &quot;aaaa&quot;,
    &quot;srcCaseId&quot;: &quot;string&quot;,
    &quot;itemCode&quot;: &quot;skxc0052&quot;,
    &quot;description&quot;: &quot;qqq&quot;,
    &quot;occurrenceDate&quot;: &quot;2022-08-04&quot;,
    &quot;address&quot;: &quot;杭州&quot;,
    &quot;longitude&quot;: &quot;120.999999&quot;,
    &quot;latitude&quot;: &quot;38.9999&quot;,
    
    &quot;gridCode&quot;: &quot;NANZHUANG001&quot;,
    &quot;channelType&quot;: &quot;000&quot;,
    &quot;channelId&quot;: &quot;string&quot;,
    &quot;subject&quot;:&quot;qqq&quot;,
    &quot;reportPersonalInfo&quot;: {
        &quot;contactName&quot;: &quot;123456&quot;,
        &quot;mobilePhone&quot;: &quot;123456&quot;,
        &quot;needReVisit&quot;: &quot;N&quot;
    },
    &quot;severityLevel&quot;: &quot;1&quot;,
    &quot;urgencyLevel&quot;: &quot;1&quot;,
    &quot;tagCodes&quot;: [
        &quot;string&quot;
    ],
    &quot;handlingUser&quot;: {
   &quot;orgCode&quot;: &quot;SYSDSJZX&quot;, 
    &quot;orgName&quot;: &quot;十堰市大数据中心&quot;, 
    &quot;postCode&quot;: &quot;SYSDSJZXCZY&quot;, 
    &quot;postName&quot;: &quot;十堰市大数据中心处置员&quot;, 
    &quot;userCode&quot;: &quot;19986509967&quot;, 
    &quot;userName&quot;: &quot;19986509967&quot; 
  },
    &quot;dutyOrgs&quot;: [],
    &quot;extFieldValues&quot;: [ 
     {
            &quot;fieldName&quot;: &quot;TechnicalPersonCode&quot;,
            &quot;fieldValue&quot;: &quot;13872805560&quot;
    },{
            &quot;fieldName&quot;: &quot;SupervisorCode&quot;,
            &quot;fieldValue&quot;: &quot;18071950168&quot;
    },{
            &quot;fieldName&quot;: &quot;AdministrativeCode&quot;,
            &quot;fieldValue&quot;: &quot;13886806330&quot;
    }
    ] 
}</code></pre><p id="u1e7b9fd7" class="ne-p"><br></p><p id="ud082cc4c" class="ne-p"><span class="ne-text">处置 | 初步处置  |  提及上报： enforce  | toUpDispose  FinishTask  </span></p><pre data-language="json" id="tX9FL" class="ne-codeblock language-json"><code>{
    &quot;extFieldValues&quot;: [
        {
            &quot;fieldName&quot;: &quot;1&quot;,
            &quot;fieldValue&quot;: &quot;Y&quot;
        }
    ],
    &quot;action&quot;: &quot;toUpDispose&quot;,
    &quot;comment&quot;: &quot;处置第一个节点&quot;,
    &quot;handlingUser&quot;: {
         &quot;orgCode&quot;: &quot;SYSDSJZX&quot;,
                    &quot;orgName&quot;: &quot;十堰市大数据中心&quot;,
                    &quot;postCode&quot;: &quot;SYSDSJZXCZY&quot;,
                    &quot;postName&quot;: &quot;十堰市大数据中心处置员&quot;,
                    &quot;userCode&quot;: &quot;13872805560&quot;,
                    &quot;userName&quot;: &quot;13872805560&quot;
  },
    &quot;taskId&quot;: &quot;10gg000000xgH9F80HYW&quot;
}


{
    &quot;extFieldValues&quot;: [
        {
            &quot;fieldName&quot;: &quot;1&quot;,
            &quot;fieldValue&quot;: &quot;Y&quot;
        }
    ],
    &quot;action&quot;: &quot;toUpDispose&quot;,
    &quot;comment&quot;: &quot;初步处置第二个节点&quot;,
    &quot;handlingUser&quot;: {
       &quot;orgCode&quot;: &quot;11420300MB1934788X&quot;, 
      &quot;orgName&quot;: &quot;市城管执法委&quot;, 
      &quot;postCode&quot;: &quot;SYSCGZFWCZRY&quot;, 
      &quot;postName&quot;: &quot;十堰市城管执法委处置人员&quot;, 
      &quot;userCode&quot;: &quot;18071950168&quot;, 
      &quot;userName&quot;: &quot;18071950168&quot; 
  },
    &quot;taskId&quot;: &quot;c60G000000xeKp8arKHw&quot;
}
</code></pre><p id="u8315fa36" class="ne-p"><br></p><p id="u10376977" class="ne-p"><span class="ne-text">结案 : ChangeCaseStatus </span></p><pre data-language="json" id="v3kkW" class="ne-codeblock language-json"><code>
{
    &quot;handlingUser&quot;: {
                    &quot;orgCode&quot;: &quot;syscyzx&quot;,
                    &quot;orgName&quot;: &quot;十堰市城运中心&quot;,
                    &quot;postCode&quot;: &quot;syscyzx&quot;,
                    &quot;postName&quot;: &quot;城运中心管理员&quot;,
                    &quot;userCode&quot;: &quot;10gg000000xCFieTJBGy&quot;,
                    &quot;userName&quot;: &quot;10gg000000xCFieTJBGy&quot;
    },
    &quot;caseCode&quot;: &quot;CY2022101100002&quot;,
    &quot;action&quot;: &quot;file&quot;,
    &quot;comment&quot;: &quot;水库结案&quot;
}

</code></pre><p id="ud61d51c3" class="ne-p"><br></p><p id="u448b7f40" class="ne-p"><br></p><p id="u4eb8750f" class="ne-p"><span class="ne-text">查询代办： QueryTodoTasks</span></p><pre data-language="javascript" id="uhkCm" class="ne-codeblock language-javascript"><code>{ 
	&quot;handlingUser&quot;:{ 
	   &quot;orgCode&quot;: &quot;SYSDSJZX&quot;,
      &quot;orgName&quot;: &quot;十堰市大数据中心&quot;,
        &quot;postCode&quot;: &quot;SYSDSJZXCZY&quot;,
        &quot;postName&quot;: &quot;十堰市大数据中心处置员&quot;,
      &quot;userCode&quot;: &quot;13872805560&quot;,
      &quot;userName&quot;: &quot;13872805560&quot;
	}, 
	&quot;caseCode&quot;:&quot;CY2022101700002&quot;,
     &quot;paging&quot;: {
    &quot;pageNum&quot;: 1,
    &quot;pageSize&quot;: 10
  }
}</code></pre><p id="uf3bc69af" class="ne-p"><br></p></details>


## 山洪流程
<details class="lake-collapse"><summary id="u518f1285"><span class="ne-text">配置： </span></summary><p id="uba021a4b" class="ne-p"><img src="https://cdn.nlark.com/yuque/0/2022/png/21382055/1665546896410-72f974a3-f0e3-47d2-8bcd-e83410131e87.png" width="419" title="" crop="0,0,1,1" id="olwKb" class="ne-image"></p><p id="ucf9b79d8" class="ne-p"><span class="ne-text">核实： 岗位 十堰市水利湖泊局处置人员</span></p><p id="ua901c079" class="ne-p"><span class="ne-text" style="font-size: 16px">山洪场景按照区县配置</span></p><p id="ufeb27db0" class="ne-p"><span class="ne-text" style="font-size: 16px">扩展字段</span><span class="ne-text" style="font-size: 16px">：</span><span class="ne-text" style="font-size: 16px">会商</span><span class="ne-text" style="font-size: 16px">1 </span><span class="ne-text" style="font-size: 16px">会商</span><span class="ne-text" style="font-size: 16px">2 </span><span class="ne-text" style="font-size: 16px">转移责任人</span></p><p id="uae82d3b0" class="ne-p"><span class="ne-text" style="font-size: 16px">核实阶段</span><span class="ne-text" style="font-size: 16px">：</span><span class="ne-text" style="font-size: 16px">配置岗位</span><span class="ne-text" style="font-size: 16px">   </span><span class="ne-text" style="font-size: 16px">区县水利局运维</span></p><p id="u645c2a3a" class="ne-p"><span class="ne-text" style="font-size: 16px">转移</span><span class="ne-text" style="font-size: 16px">：</span><span class="ne-text" style="font-size: 16px">配置人</span><span class="ne-text" style="font-size: 16px">  </span><span class="ne-text" style="font-size: 16px">转移责任人</span></p><p id="u13d24aa4" class="ne-p"><span class="ne-text" style="font-size: 16px">结案：配置区县城运中心</span></p><p id="u97642caf" class="ne-p"><br></p><p id="u606ee016" class="ne-p"><span class="ne-text" style="font-size: 16px">山洪上报扩展字段：</span></p><p id="u7fabcf84" class="ne-p"><span class="ne-text">会商责任人1  taskUserCode1   | usrcode 13872805560  taskid  c60G000000xXqyftH7fk</span></p><p id="u308cdff2" class="ne-p"><span class="ne-text">会商责任人2  taskUserCode2  | usrcode 18071950168   taskid   c60G000000xXqyl22ekC</span></p><p id="u60f0824c" class="ne-p"><span class="ne-text">转移责任人    transfer  | usrcode 13886806330 / syssljgly</span></p><p id="u070350c1" class="ne-p"><span class="ne-text"></span></p><p id="u492e52fa" class="ne-p"><span class="ne-text">变更信息 后：</span></p><p id="ua47ccf01" class="ne-p"><span class="ne-text">初步处置 ：配置人 会商扩展字段  User</span></p><p id="u3d3a7868" class="ne-p"><span class="ne-text">处置：配置人 转移责任人</span></p><p id="u86a48104" class="ne-p"><span class="ne-text">办结： 岗位  十堰市十堰市</span></p><p id="u3908fab8" class="ne-p"><span class="ne-text"></span></p></details>


<details class="lake-collapse"><summary id="ucdffa0a4"><span class="ne-text">十堰市山洪测试</span></summary><p id="u9efc6929" class="ne-p"><br></p><p id="ubf9f45c1" class="ne-p"><span class="ne-text">查询事件detail</span></p><p id="u5e13e963" class="ne-p"><span class="ne-text">querycasedetail</span></p><pre data-language="json" id="J9mah" class="ne-codeblock language-json"><code>{
    &quot;handlingUser&quot;: {
    &quot;orgCode&quot;: &quot;SYSDSJZX&quot;, 
    &quot;orgName&quot;: &quot;十堰市大数据中心&quot;, 
    &quot;postCode&quot;: &quot;SYSDSJZXCZY&quot;, 
    &quot;postName&quot;: &quot;十堰市大数据中心处置员&quot;, 
    &quot;userCode&quot;: &quot;19986509967&quot;, 
    &quot;userName&quot;: &quot;19986509967&quot; 
    },
    &quot;caseCode&quot;: &quot;2022102000022&quot;
}</code></pre><p id="ua1680da9" class="ne-p"><br></p><p id="u70a87847" class="ne-p"><span class="ne-text">casecode CY2022101200001</span></p><p id="uaafb39ee" class="ne-p"><span class="ne-text">reportcase 上报</span></p><pre data-language="json" id="NtOYs" class="ne-codeblock language-json"><code>{ 
    &quot;caseName&quot;: &quot;aaaa&quot;,
    &quot;srcCaseId&quot;: &quot;string&quot;,
    &quot;itemCode&quot;: &quot;shgl0001&quot;,
    &quot;description&quot;: &quot;qqq&quot;,
    &quot;occurrenceDate&quot;: &quot;2022-08-04&quot;,
    &quot;address&quot;: &quot;杭州&quot;,
    &quot;longitude&quot;: &quot;120.999999&quot;,
    &quot;latitude&quot;: &quot;38.9999&quot;,
    
    &quot;gridCode&quot;: &quot;NANZHUANG001&quot;,
    &quot;channelType&quot;: &quot;107&quot;,
    &quot;channelId&quot;: &quot;string&quot;,
    &quot;subject&quot;:&quot;qqq&quot;,
    &quot;reportPersonalInfo&quot;: {
        &quot;contactName&quot;: &quot;123456&quot;,
        &quot;mobilePhone&quot;: &quot;123456&quot;,
        &quot;needReVisit&quot;: &quot;N&quot;
    },
    &quot;severityLevel&quot;: &quot;1&quot;,
    &quot;urgencyLevel&quot;: &quot;1&quot;,
    &quot;tagCodes&quot;: [
        &quot;string&quot;
    ],
    &quot;handlingUser&quot;: {
   &quot;orgCode&quot;: &quot;SYSDSJZX&quot;, 
    &quot;orgName&quot;: &quot;十堰市大数据中心&quot;, 
    &quot;postCode&quot;: &quot;SYSDSJZXCZY&quot;, 
    &quot;postName&quot;: &quot;十堰市大数据中心处置员&quot;, 
    &quot;userCode&quot;: &quot;19986509967&quot;, 
    &quot;userName&quot;: &quot;19986509967&quot; 
  },
    &quot;dutyOrgs&quot;: [],
    &quot;extFieldValues&quot;: [ 
     {
            &quot;fieldName&quot;: &quot;taskUserCode1&quot;,
            &quot;fieldValue&quot;: &quot;13872805560&quot;
    },{
            &quot;fieldName&quot;: &quot;taskUserCode2&quot;,
            &quot;fieldValue&quot;: &quot;18071950168&quot;
    },{
            &quot;fieldName&quot;: &quot;transfer&quot;,
            &quot;fieldValue&quot;: &quot;13886806330&quot;
    }
    ] 
}


</code></pre><p id="u1e712736" class="ne-p"><br></p><p id="uae9844e1" class="ne-p"><span class="ne-text">核实： </span><span class="ne-text" style="color: #303030; font-size: 16px">调用FinishTask接口核实事件（action：</span><strong><span class="ne-text" style="color: #303030; font-size: 16px">verify</span></strong><span class="ne-text" style="color: #303030; font-size: 16px">）【同意】</span></p><p id="ubf677cf6" class="ne-p"><br></p><pre data-language="json" id="LydDD" class="ne-codeblock language-json"><code>{
    &quot;extFieldValues&quot;: [
        {
            &quot;fieldName&quot;: &quot;1&quot;,
            &quot;fieldValue&quot;: &quot;Y&quot;
        }
    ],
    &quot;action&quot;: &quot;verify&quot;,
    &quot;comment&quot;: &quot;山洪处置第一个节点&quot;,
    &quot;handlingUser&quot;: {
       &quot;orgCode&quot;: &quot;SZSHZRBM&quot;,
       &quot;orgName&quot;: &quot;市直山洪责任部门&quot;,
       &quot;postCode&quot;: &quot;SZSHZRBMCLY&quot;,
        &quot;postName&quot;: &quot;市直山洪责任部门处理员&quot;,
        &quot;userCode&quot;: &quot;sysshhs&quot;,  
        &quot;userName&quot;: &quot;sysshhs&quot;
  },
    &quot;taskId&quot;: &quot;c60G000000xY3NmMMRuK&quot;
}
</code></pre><p id="uaef02c95" class="ne-p"><br></p><p id="u732b7a71" class="ne-p"><span class="ne-text">处置： </span><span class="ne-text" style="color: #303030; font-size: 16px">调用FinishTask接口核实事件（action：</span><strong><span class="ne-text" style="color: #303030; font-size: 16px"> noTransfer</span></strong><span class="ne-text" style="color: #303030; font-size: 16px">）【不转移】</span></p><p id="ub8a8a76f" class="ne-p"><br></p><pre data-language="json" id="lxDHt" class="ne-codeblock language-json"><code>{
    &quot;extFieldValues&quot;: [
        {
            &quot;fieldName&quot;: &quot;1&quot;,
            &quot;fieldValue&quot;: &quot;Y&quot;
        }
    ],
    &quot;action&quot;: &quot;transfer&quot;,
    &quot;comment&quot;: &quot;山洪处置第二个节点&quot;,
    &quot;handlingUser&quot;: {
       &quot;orgCode&quot;: &quot;11420300MB1934788X&quot;, 
      &quot;orgName&quot;: &quot;市城管执法委&quot;, 
      &quot;postCode&quot;: &quot;SYSCGZFWCZRY&quot;, 
      &quot;postName&quot;: &quot;十堰市城管执法委处置人员&quot;, 
      &quot;userCode&quot;: &quot;13872805560&quot;, 
      &quot;userName&quot;: &quot;13872805560&quot; 
  },
    &quot;taskId&quot;: &quot;c60G000000xcuyjwSno0&quot;
}
</code></pre><p id="u05c3f873" class="ne-p"><br></p><p id="u97d7db73" class="ne-p"><span class="ne-text">结案： </span><span class="ne-text" style="color: #303030; font-size: 16px">调用 changeCaseStatus接口结案（changeCaseStatus：</span><strong><span class="ne-text" style="color: #303030; font-size: 16px"> </span></strong><span class="ne-text" style="color: #303030; font-size: 16px">enforce） </span></p><p id="u67aeef06" class="ne-p"><span class="ne-text" style="color: #303030; font-size: 16px"></span></p><pre data-language="json" id="N24vt" class="ne-codeblock language-json"><code>{
    &quot;handlingUser&quot;: {
                    &quot;orgCode&quot;: &quot;SYSXZQH&quot;,
                    &quot;orgName&quot;: &quot;十堰市&quot;,
                    &quot;postCode&quot;: &quot;SYS&quot;,
                    &quot;postName&quot;: &quot;十堰市&quot;,
                    &quot;userCode&quot;: &quot;sysshy&quot;,
                    &quot;userName&quot;: &quot;sysshy&quot;
    },
    &quot;caseCode&quot;: &quot;2022101500023&quot;,
    &quot;action&quot;: &quot;close&quot;,
    &quot;comment&quot;: &quot;山洪结案&quot;
}</code></pre><p id="udf70fb9a" class="ne-p"><br></p><p id="u0661c228" class="ne-p"><span class="ne-text">转移：</span></p><pre data-language="json" id="GBzNX" class="ne-codeblock language-json"><code>{
    &quot;extFieldValues&quot;: [
        {
            &quot;fieldName&quot;: &quot;1&quot;,
            &quot;fieldValue&quot;: &quot;Y&quot;
        }
    ],
    &quot;action&quot;: &quot;transfer&quot;,
    &quot;comment&quot;: &quot;山洪处置第二个节点&quot;,
    &quot;handlingUser&quot;: {
       &quot;orgCode&quot;: &quot;11420300MB1934788X&quot;, 
      &quot;orgName&quot;: &quot;市城管执法委&quot;, 
      &quot;postCode&quot;: &quot;SYSCGZFWCZRY&quot;, 
      &quot;postName&quot;: &quot;十堰市城管执法委处置人员&quot;, 
      &quot;userCode&quot;: &quot;13872805560&quot;, 
      &quot;userName&quot;: &quot;13872805560&quot; 
  },
    &quot;taskId&quot;: &quot;c60G000000xY3S9hSn8S&quot;
}
</code></pre><p id="udd6777bc" class="ne-p"><br></p><p id="uf3baee25" class="ne-p"><span class="ne-text">处置：finishtask  action enforce</span></p><p id="ua5a808e2" class="ne-p"><span class="ne-text">结案：changecasestatus</span></p><p id="uaeebdd45" class="ne-p"><br></p></details>




## 地灾流程
<details class="lake-collapse"><summary id="ude5eb272"><span class="ne-text">地灾流程配置</span></summary><p id="ufd08747b" class="ne-p"><img src="https://cdn.nlark.com/yuque/0/2022/png/21382055/1665627319353-90b044a8-2922-41c3-baed-da482dc884cb.png" width="551" title="" crop="0,0,1,1" id="EAFI0" class="ne-image"></p><p id="u137e909f" class="ne-p"><span class="ne-text"></span></p><p id="u560c1d4f" class="ne-p"><span class="ne-text" style="font-size: 16px">地灾场景按照街道配置</span></p><p id="u1073569c" class="ne-p"><span class="ne-text" style="font-size: 16px">核实</span><span class="ne-text" style="font-size: 16px">：</span><span class="ne-text" style="font-size: 16px">岗位街道国土所所长</span></p><p id="ua2bee64f" class="ne-p"><span class="ne-text" style="font-size: 16px">初步处置</span><span class="ne-text" style="font-size: 16px">：</span><span class="ne-text" style="font-size: 16px">岗位</span><span class="ne-text" style="font-size: 16px"> </span><span class="ne-text" style="font-size: 16px">县自规局科股长</span></p><p id="u12e29eb8" class="ne-p"><span class="ne-text" style="font-size: 16px">处置</span><span class="ne-text" style="font-size: 16px">：</span><span class="ne-text" style="font-size: 16px">岗位</span><span class="ne-text" style="font-size: 16px"> </span><span class="ne-text" style="font-size: 16px">街道办主任</span></p><p id="u0267d55d" class="ne-p"><span class="ne-text" style="font-size: 16px">疑难处置</span><span class="ne-text" style="font-size: 16px">：</span><span class="ne-text" style="font-size: 16px">岗位</span><span class="ne-text" style="font-size: 16px"> </span><span class="ne-text" style="font-size: 16px">市自规局处置</span></p><p id="ue0034324" class="ne-p"><span class="ne-text" style="font-size: 16px">结案：岗位 区县城运中心</span></p><p id="u4e3410f7" class="ne-p"><span class="ne-text"></span></p><p id="ua7f9ade8" class="ne-p"><span class="ne-text">测试部门  people {</span></p><p id="ueb1228c7" class="ne-p"><span class="ne-text">市城管执法委   十堰市公安局处置人员      十堰市发改委处置人员    十堰市政府办处置人员    十堰市</span></p><p id="ufddad8c2" class="ne-p"><span class="ne-text">张性军   市公安局管理员  市发改委处理员  市政府办管理员  十堰市审核员</span></p><p id="u1925d541" class="ne-p"><span class="ne-text">}</span></p><p id="ua0f4443c" class="ne-p"><span class="ne-text">流程 ： 核实  ----&gt; 初步处置  ----&gt; 处置  ----&gt; 疑难处置 ----&gt; 结案</span></p><p id="ude15e4f2" class="ne-p"><span class="ne-text"></span></p><p id="u03f3eae8" class="ne-p"><span class="ne-text">抄送扩展字段</span></p><p id="uc19743e1" class="ne-p"><span class="ne-text">抄送人  accessor</span></p><p id="u3e199d66" class="ne-p"><span class="ne-text"></span></p><p id="ueca2b386" class="ne-p"><span class="ne-text">配置：</span></p><p id="u0ed4da31" class="ne-p"><span class="ne-text">初步处置 ： 配置岗位   十堰市公安局处置人员</span></p><p id="u8e15b7cd" class="ne-p"><span class="ne-text">处置 ： 配置岗位  十堰市发改委处置人员</span></p><p id="u1a15287d" class="ne-p"><span class="ne-text">疑难处置： 配置岗位  十堰市政府办处置人员</span></p><p id="u3d33bd08" class="ne-p"><span class="ne-text">办结： 十堰市</span></p><p id="ue92293f6" class="ne-p"><span class="ne-text"></span></p><p id="u0a9a4f35" class="ne-p"><span class="ne-text"></span></p><p id="uff3998c1" class="ne-p"><span class="ne-text"></span></p><p id="u7b1f9cbc" class="ne-p"><br></p></details>


<details class="lake-collapse"><summary id="u9510178c"><span class="ne-text">十堰市 山洪</span></summary><p id="u8d26a4cb" class="ne-p"><span class="ne-text">上报节点：itemcode：  zhdizhizaihai00001</span></p><pre data-language="json" id="UOTxL" class="ne-codeblock language-json"><code>{ 
    &quot;caseName&quot;: &quot;aaaa&quot;,
    &quot;srcCaseId&quot;: &quot;string&quot;,
    &quot;itemCode&quot;: &quot;zhdizhizaihai00001&quot;,
    &quot;description&quot;: &quot;qqq&quot;,
    &quot;occurrenceDate&quot;: &quot;2022-08-04&quot;,
    &quot;address&quot;: &quot;杭州&quot;,
    &quot;longitude&quot;: &quot;120.999999&quot;,
    &quot;latitude&quot;: &quot;38.9999&quot;,
    
    &quot;gridCode&quot;: &quot;NANZHUANG001&quot;,
    &quot;channelType&quot;: &quot;107&quot;,
    &quot;channelId&quot;: &quot;string&quot;,
    &quot;subject&quot;:&quot;qqq&quot;,
    &quot;reportPersonalInfo&quot;: {
        &quot;contactName&quot;: &quot;123456&quot;,
        &quot;mobilePhone&quot;: &quot;123456&quot;,
        &quot;needReVisit&quot;: &quot;N&quot;
    },
    &quot;severityLevel&quot;: &quot;1&quot;,
    &quot;urgencyLevel&quot;: &quot;1&quot;,
    &quot;tagCodes&quot;: [
        &quot;string&quot;
    ],
    &quot;handlingUser&quot;: {
   &quot;orgCode&quot;: &quot;SYSDSJZX&quot;, 
    &quot;orgName&quot;: &quot;十堰市大数据中心&quot;, 
    &quot;postCode&quot;: &quot;SYSDSJZXCZY&quot;, 
    &quot;postName&quot;: &quot;十堰市大数据中心处置员&quot;, 
    &quot;userCode&quot;: &quot;19986509967&quot;, 
    &quot;userName&quot;: &quot;19986509967&quot; 
  },
    &quot;dutyOrgs&quot;: [],
    &quot;extFieldValues&quot;: [ 
     {
            &quot;fieldName&quot;: &quot;accessors&quot;,
            &quot;fieldValue&quot;: &quot;13872805560&quot;
    }
    ] 
}


</code></pre><p id="u99c23a83" class="ne-p"><br></p><p id="u45bed44c" class="ne-p"><span class="ne-text">核实处置：张性军  action ：</span><span class="ne-text" style="color: #303030; font-size: 16px">verify</span></p><pre data-language="json" id="ofic0" class="ne-codeblock language-json"><code>{
    &quot;extFieldValues&quot;: [
        {
            &quot;fieldName&quot;: &quot;1&quot;,
            &quot;fieldValue&quot;: &quot;Y&quot;
        }
    ],
    &quot;action&quot;: &quot;verify&quot;,
    &quot;comment&quot;: &quot;地灾处置第一个节点&quot;,
    &quot;handlingUser&quot;: {
        &quot;orgCode&quot;: &quot;11420300MB1934788X&quot;,
                    &quot;orgName&quot;: &quot;市城管执法委&quot;,
                    &quot;postCode&quot;: &quot;SYSCGZFWCZRY&quot;,
                    &quot;postName&quot;: &quot;十堰市城管执法委处置人员&quot;,
                    &quot;userCode&quot;: &quot;13872805560&quot;,
                    &quot;userName&quot;: &quot;13872805560&quot;
  },
    &quot;taskId&quot;: &quot;c60G000000xZU0HySv5c&quot;
}
</code></pre><p id="u8ff6efba" class="ne-p"><br></p><p id="ued9a85d2" class="ne-p"><span class="ne-text">处置 | 初步处置 enforce | 提及上报 toUpDispose </span></p><pre data-language="json" id="JGReg" class="ne-codeblock language-json"><code>{
    &quot;extFieldValues&quot;: [
        {
            &quot;fieldName&quot;: &quot;1&quot;,
            &quot;fieldValue&quot;: &quot;Y&quot;
        }
    ],
    &quot;action&quot;: &quot;toUpDispose&quot;,
    &quot;comment&quot;: &quot;地灾处置第二个节点&quot;,
    &quot;handlingUser&quot;: {
        &quot;orgCode&quot;: &quot;11420300011080827R&quot;,
         &quot;orgName&quot;: &quot;市公安局&quot;,
        &quot;postCode&quot;: &quot;SYSGAJCZRY&quot;,
      &quot;postName&quot;: &quot;十堰市公安局处置人员&quot;,
       &quot;userCode&quot;: &quot;sysgajgly&quot;,
      &quot;userName&quot;: &quot;sysgajgly&quot;
  },
    &quot;taskId&quot;: &quot;c60G000000xgZmeDzMwq&quot;
}


{
    &quot;extFieldValues&quot;: [
        {
            &quot;fieldName&quot;: &quot;1&quot;,
            &quot;fieldValue&quot;: &quot;Y&quot;
        }
    ],
    &quot;action&quot;: &quot;toUpDispose&quot;,
    &quot;comment&quot;: &quot;地灾处置第三个节点&quot;,
    &quot;handlingUser&quot;: {
           &quot;orgCode&quot;: &quot;1142030001108115XG&quot;,
         &quot;orgName&quot;: &quot;市发改委&quot;,
          &quot;postCode&quot;: &quot;SYSFGWCZRY&quot;,
          &quot;postName&quot;: &quot;十堰市发改委处置人员&quot;,
          &quot;userCode&quot;: &quot;sfgwcly&quot;,
          &quot;userName&quot;: &quot;sfgwcly&quot; 
  },
    &quot;taskId&quot;: &quot;c60G000000xgZmjQjHqC&quot;
}


</code></pre><p id="u2a617773" class="ne-p"><br></p><p id="u68a7c0a3" class="ne-p"><span class="ne-text">阶段处置 enforce </span></p><pre data-language="json" id="zi7SG" class="ne-codeblock language-json"><code>
{
    &quot;extFieldValues&quot;: [
        {
            &quot;fieldName&quot;: &quot;1&quot;,
            &quot;fieldValue&quot;: &quot;Y&quot;
        }
    ],
    &quot;action&quot;: &quot;enforce&quot;,
    &quot;comment&quot;: &quot;地灾处置第4个节点&quot;,
    &quot;handlingUser&quot;: {
         &quot;orgCode&quot;: &quot;1142030001108078XE&quot;,
           &quot;orgName&quot;: &quot;市政府办&quot;,
            &quot;postCode&quot;: &quot;SYSZFBCZRY&quot;,
            &quot;postName&quot;: &quot;十堰市政府办处置人员&quot;,
           &quot;userCode&quot;: &quot;syszfbgly&quot;,
         &quot;userName&quot;: &quot;syszfbgly&quot;
  },
    &quot;taskId&quot;: &quot;c60G000000xgZsgiIIiW&quot;
}
</code></pre><p id="uba47a53b" class="ne-p"><br></p><p id="u8866054f" class="ne-p"><span class="ne-text">结案 close </span></p><pre data-language="json" id="vwkHk" class="ne-codeblock language-json"><code>{
    &quot;handlingUser&quot;: {
                    &quot;orgCode&quot;: &quot;SYSXZQH&quot;,
                    &quot;orgName&quot;: &quot;十堰市&quot;,
                    &quot;postCode&quot;: &quot;SYS&quot;,
                    &quot;postName&quot;: &quot;十堰市&quot;,
                    &quot;userCode&quot;: &quot;sysshy&quot;,
                    &quot;userName&quot;: &quot;sysshy&quot;
    },
    &quot;caseCode&quot;: &quot;SH2022101700003&quot;,
    &quot;action&quot;: &quot;close&quot;,
    &quot;comment&quot;: &quot;地灾结案&quot;
}</code></pre><p id="uf372eb6d" class="ne-p"><br></p><p id="ud5ac2450" class="ne-p"><span class="ne-text">查询抄送任务  querycases</span></p><pre data-language="json" id="WR15d" class="ne-codeblock language-json"><code>{
    &quot;handlingUser&quot;: {
        &quot;orgCode&quot;: &quot;11420300MB1934788X&quot;,
        &quot;orgName&quot;: &quot;市城管执法委&quot;,
        &quot;postCode&quot;: &quot;SYSCGZFWCZRY&quot;,
        &quot;postName&quot;: &quot;十堰市城管执法委处置人员&quot;,
        &quot;userName&quot;: &quot;13872805560&quot;
    },
    &quot;queryCaseCond&quot;: {
    },
    &quot;paging&quot;: {
        &quot;pageSize&quot;: 10,
        &quot;pageNum&quot;: 1,
        &quot;total&quot;: 10
    }
}</code></pre></details>


<details class="lake-collapse"><summary id="uc8eccbf0"><span class="ne-text">二堰街道   420302002</span></summary><p id="u1d76ef13" class="ne-p"><span class="ne-text">茅箭区二堰街道分拨人员  MJQEYJDFBRY</span></p><p id="u620f2d4d" class="ne-p"><span class="ne-text"> 刘勇   13972455176</span></p><p id="u0fe3b738" class="ne-p"><span class="ne-text"></span></p><p id="u08eb0fff" class="ne-p"><span class="ne-text">itemcode    预警点发生地面隆起  dzxc0002</span></p><p id="udfa2613f" class="ne-p"><br></p><pre data-language="javascript" id="rt4C0" class="ne-codeblock language-javascript"><code>    &quot;handlingUser&quot;: {
     &quot;orgCode&quot;: &quot;420302002&quot;, 
      &quot;orgName&quot;: &quot;二堰街道&quot;, 
      &quot;postCode&quot;: &quot;MJQEYJDFBRY&quot;, 
      &quot;postName&quot;: &quot;茅箭区二堰街道分拨人员&quot;, 
      &quot;userCode&quot;: &quot;13972455176&quot;, 
      &quot;userName&quot;: &quot;13972455176&quot; 
  }</code></pre><p id="u9d7e71f0" class="ne-p"><br></p><p id="u97d28e48" class="ne-p"><span class="ne-text">上报</span></p><pre data-language="javascript" id="GUTKH" class="ne-codeblock language-javascript"><code>{ 
    &quot;caseName&quot;: &quot;aaaa&quot;,
    &quot;srcCaseId&quot;: &quot;string&quot;,
    &quot;itemCode&quot;: &quot;dzxc0002&quot;,
    &quot;description&quot;: &quot;qqq&quot;,
    &quot;occurrenceDate&quot;: &quot;2022-08-04&quot;,
    &quot;address&quot;: &quot;杭州&quot;,
    &quot;longitude&quot;: &quot;120.999999&quot;,
    &quot;latitude&quot;: &quot;38.9999&quot;,
    
    &quot;gridCode&quot;: &quot;NANZHUANG001&quot;,
    &quot;channelType&quot;: &quot;107&quot;,
    &quot;channelId&quot;: &quot;string&quot;,
    &quot;subject&quot;:&quot;qqq&quot;,
    &quot;reportPersonalInfo&quot;: {
        &quot;contactName&quot;: &quot;123456&quot;,
        &quot;mobilePhone&quot;: &quot;123456&quot;,
        &quot;needReVisit&quot;: &quot;N&quot;
    },
    &quot;severityLevel&quot;: &quot;1&quot;,
    &quot;urgencyLevel&quot;: &quot;1&quot;,
    &quot;tagCodes&quot;: [
        &quot;string&quot;
    ],
    &quot;handlingUser&quot;: {
     &quot;orgCode&quot;: &quot;420302002&quot;, 
      &quot;orgName&quot;: &quot;二堰街道&quot;, 
      &quot;postCode&quot;: &quot;MJQEYJDCLRY&quot;, 
      &quot;postName&quot;: &quot;茅箭区二堰街道处置人员&quot;, 
      &quot;userCode&quot;: &quot;13972455176&quot;, 
      &quot;userName&quot;: &quot;13972455176&quot; 
  },
    &quot;dutyOrgs&quot;: [],
    &quot;extFieldValues&quot;: [ 
      
    ] 
}
</code></pre><p id="uc03a6335" class="ne-p"><br></p><p id="ubcbbd66c" class="ne-p"><span class="ne-text">初步处置 提及上报</span></p><pre data-language="javascript" id="pkf9I" class="ne-codeblock language-javascript"><code>{
    &quot;extFieldValues&quot;: [
        {
            &quot;fieldName&quot;: &quot;1&quot;,
            &quot;fieldValue&quot;: &quot;Y&quot;
        }
    ],
    &quot;action&quot;: &quot;toUpDispose&quot;,
    &quot;comment&quot;: &quot;地灾处置第二个节点&quot;,
    &quot;handlingUser&quot;: {
       &quot;orgCode&quot;: &quot;11420300420141731N&quot;,
         &quot;orgName&quot;: &quot;市自然资源和规划局茅箭分局&quot;,
       &quot;postCode&quot;: &quot;MJQZGDZKGZ&quot;,
       &quot;postName&quot;: &quot;茅箭区自规地灾科股长&quot;,
        &quot;userCode&quot;: &quot;13636240777&quot;,
         &quot;userName&quot;: &quot;13636240777&quot;
  },
    &quot;taskId&quot;: &quot;c60G000000xhMJTrUwN6&quot;
}


{
    &quot;extFieldValues&quot;: [
        {
            &quot;fieldName&quot;: &quot;1&quot;,
            &quot;fieldValue&quot;: &quot;Y&quot;
        }
    ],
    &quot;action&quot;: &quot;toUpDispose&quot;,
    &quot;comment&quot;: &quot;地灾处置第三个节点&quot;,
    &quot;handlingUser&quot;: {
        &quot;orgCode&quot;: &quot;420302002&quot;,
         &quot;orgName&quot;: &quot;二堰街道&quot;,
         &quot;postCode&quot;: &quot;MJQEYJDCLRY&quot;,
          &quot;postName&quot;: &quot;茅箭区二堰街道处置人员&quot;,
           &quot;userCode&quot;: &quot;13972455176&quot;,
          &quot;userName&quot;: &quot;13972455176&quot;
  },
    &quot;taskId&quot;: &quot;c60G000000xhMJZ0pfhg&quot;
}

</code></pre><p id="ud1542306" class="ne-p"><br></p><p id="u17b9822d" class="ne-p"><span class="ne-text">处置</span></p><pre data-language="javascript" id="fekT6" class="ne-codeblock language-javascript"><code>
{
    &quot;extFieldValues&quot;: [
        {
            &quot;fieldName&quot;: &quot;1&quot;,
            &quot;fieldValue&quot;: &quot;Y&quot;
        }
    ],
    &quot;action&quot;: &quot;enforce&quot;,
    &quot;comment&quot;: &quot;地灾处置第4个节点&quot;,
    &quot;handlingUser&quot;: {
          &quot;orgCode&quot;: &quot;1142030001108086X2&quot;,
                    &quot;orgName&quot;: &quot;市自然资源和规划局&quot;,
                    &quot;postCode&quot;: &quot;SYSZRZYHGHJCZRY&quot;,
                    &quot;postName&quot;: &quot;十堰市自然资源和规划局处置人员&quot;,
                    &quot;userCode&quot;: &quot;13545013288&quot;,
                    &quot;userName&quot;: &quot;13545013288&quot;
  },
    &quot;taskId&quot;: &quot;c60G000000xeX4fbWrdA&quot;
}
</code></pre><p id="u66006dcf" class="ne-p"><br></p><p id="u81fd5fea" class="ne-p"><br></p></details>




# 解决bug 信息


<details class="lake-collapse"><summary id="ud1a9185a"><span class="ne-text">水库上报 提及上报可以查到</span></summary><p id="udd8501e2" class="ne-p"><span class="ne-text">c60G000000xeM322DLA8 【find 提及上报】</span></p><p id="ufe5b0165" class="ne-p"><span class="ne-text">c60G000000xeNDYfbzfs 【no find  处置 error】</span></p><p id="u06124baf" class="ne-p"><br></p></details>


<details class="lake-collapse"><summary id="u821f8277"><span class="ne-text">荆门bug stage 字段必填</span></summary><p id="u2270e648" class="ne-p"><span class="ne-text" style="color: #000000; background-color: #fffffe; font-size: 14px">where name  =  'ShineMo1__UOC001_C_TLD01__ItemSituation__CST'</span></p><p id="uc18d00a1" class="ne-p"><span class="ne-text" style="color: #000000; background-color: #fffffe; font-size: 14px">or  name  =  'ShineMo1__UOC002_C_TLD01__ItemSituation__CST'</span></p><p id="ubfa33e6c" class="ne-p"><span class="ne-text" style="color: #000000; background-color: #fffffe; font-size: 14px">or  name   = 'ShineMo1__UOC004_C_TLD01__ItemSituation__CST'</span></p><p id="u21c85260" class="ne-p"><span class="ne-text" style="color: #000000; background-color: #fffffe; font-size: 14px">or  name  =  'ShineMo1__UOC007_C_TLD01__ItemSituation__CST'</span></p><p id="u126574cf" class="ne-p"><span class="ne-text" style="color: #000000; background-color: #fffffe; font-size: 14px">or  name  = 'ShineMo1__UOC009_C_TLD01__ItemSituation__CST'</span></p><p id="u98d8211d" class="ne-p"><span class="ne-text" style="color: #000000; background-color: #fffffe; font-size: 14px">or  name  = 'ShineMo1__UOC011_C_TLD01__ItemSituation__CST'</span></p><p id="u9e8f0fe2" class="ne-p"><span class="ne-text" style="color: #000000; background-color: #fffffe; font-size: 14px">or  name  = 'ShineMo1__UOC016_C_TLD01__ItemSituation__CST'</span></p><p id="u03962b28" class="ne-p"><span class="ne-text" style="color: #000000; background-color: #fffffe; font-size: 14px">or  name  = 'ShineMo1__UOC018_C_TLD01__ItemSituation__CST'</span></p><p id="u7ac1c3c3" class="ne-p"><span class="ne-text" style="color: #000000; background-color: #fffffe; font-size: 14px">or  name  = 'ShineMo1__UOC029_C_TLD01__ItemSituation__CST'</span></p><p id="u9617e509" class="ne-p"><span class="ne-text" style="color: #000000; background-color: #fffffe; font-size: 14px">or  name  = 'ShineMo1__UOC039_C_TLD01__ItemSituation__CST'</span></p><p id="u07e9ebb2" class="ne-p"><span class="ne-text" style="color: #000000; background-color: #fffffe; font-size: 14px">or  name  = 'ShineMo1__UOC051_C_TLD01__ItemSituation__CST'</span></p><p id="ued130c30" class="ne-p"><span class="ne-text" style="color: #000000; background-color: #fffffe; font-size: 14px">or  name  = 'ShineMo1__UOC064_C_TLD01__ItemSituation__CST'</span></p><p id="ub8c551d6" class="ne-p"><span class="ne-text" style="color: #000000; background-color: #fffffe; font-size: 14px">or  name  = 'ShineMo1__UOC078_C_TLD01__ItemSituation__CST'</span></p><p id="u143d91d6" class="ne-p"><span class="ne-text" style="color: #000000; background-color: #fffffe; font-size: 14px">or  name  = 'ShineMo1__UOC095_C_TLD01__ItemSituation__CST'</span></p><p id="u3c80c84b" class="ne-p"><span class="ne-text" style="color: #000000; background-color: #fffffe; font-size: 14px">or  name  = 'ShineMo1__UOC113_C_TLD01__ItemSituation__CST'</span></p><p id="ufd6a7332" class="ne-p"><br></p><p id="u25cf5b15" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">cust000000x5R4gQHfjU  cust000000x5R4gQHfkW</span></p><p id="u2c8df2b7" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">ShineMo1__UOC001_C_TLD01__ItemSituation__CST</span></p><p id="ud3a8332c" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">cust000000x5R4itHSqG   </span><span class="ne-text" style="color: rgb(0, 0, 0); background-color: rgb(245, 247, 250); font-size: 12px">cust000000x5R4itHSrI</span></p><p id="u53b12362" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">ShineMo1__UOC002_C_TLD01__ItemSituation__CST</span></p><p id="u6da1fa05" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">cust000000x5R4l0Q9Ca  </span><span class="ne-text" style="color: rgb(0, 0, 0); background-color: rgb(245, 247, 250); font-size: 12px">cust000000x5R4l0Q9Dc</span></p><p id="u6d1fd4ce" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">ShineMo1__UOC004_C_TLD01__ItemSituation__CST</span></p><p id="uf252fbfc" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">cust000000x5R4niB54i     </span><span class="ne-text" style="color: rgb(0, 0, 0); background-color: rgb(245, 247, 250); font-size: 12px">cust000000x5R4niB55k</span></p><p id="u60398379" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">ShineMo1__UOC007_C_TLD01__ItemSituation__CST</span></p><p id="u5f05655f" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">cust000000x5jwKzcig4  </span><span class="ne-text" style="color: rgb(0, 0, 0); background-color: rgb(245, 247, 250); font-size: 12px">cust000000x5jwKzcih6</span></p><p id="ue8c31130" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">ShineMo1__UOC009_C_TLD01__ItemSituation__CST</span></p><p id="u90e635c8" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">cust000000x5R4qC1fJA  </span><span class="ne-text" style="color: rgb(0, 0, 0); background-color: rgb(245, 247, 250); font-size: 12px">cust000000x5R4qC1fKC</span></p><p id="ue1758c66" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">ShineMo1__UOC011_C_TLD01__ItemSituation__CST</span></p><p id="uc9cca567" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">cust000000x5R4seAf1k  </span><span class="ne-text" style="color: rgb(0, 0, 0); background-color: rgb(245, 247, 250); font-size: 12px">cust000000x5R4seAf2m</span></p><p id="ue765fe61" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">ShineMo1__UOC016_C_TLD01__ItemSituation__CST</span></p><p id="u81ccab78" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">cust000000x5jwNzGNkG  </span><span class="ne-text" style="color: rgb(0, 0, 0); background-color: rgb(245, 247, 250); font-size: 12px">cust000000x5jwNzGNlI</span></p><p id="uf9d58d3c" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">ShineMo1__UOC018_C_TLD01__ItemSituation__CST</span></p><p id="ue1cc08ef" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">cust000000x5R4xzzk5A   </span><span class="ne-text" style="color: rgb(0, 0, 0); background-color: rgb(245, 247, 250); font-size: 12px">cust000000x5R4xzzk6C</span></p><p id="udd51f125" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">ShineMo1__UOC029_C_TLD01__ItemSituation__CST</span></p><p id="ud25b701a" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">cust000000x5jwU4VHc0  </span><span class="ne-text" style="color: rgb(0, 0, 0); background-color: rgb(245, 247, 250); font-size: 12px">cust000000x5jwU4VHd2</span></p><p id="u551cd344" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">ShineMo1__UOC039_C_TLD01__ItemSituation__CST</span></p><p id="u46f2e1db" class="ne-p"><br></p><p id="u763c46ce" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">cust000000x5jwWLrW7c   </span><span class="ne-text" style="color: rgb(0, 0, 0); background-color: rgb(245, 247, 250); font-size: 12px">cust000000x5jwWLrW8e</span></p><p id="u64d208c3" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">ShineMo1__UOC051_C_TLD01__ItemSituation__CST</span></p><p id="u71c53751" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">cust000000x5jwZ1LexE  </span><span class="ne-text" style="color: rgb(0, 0, 0); background-color: rgb(245, 247, 250); font-size: 12px">cust000000x5jwZ1LeyG</span></p><p id="u870720b3" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">ShineMo1__UOC064_C_TLD01__ItemSituation__CST</span></p><p id="u92eef625" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">cust000000x5jwbZSEPA  </span><span class="ne-text" style="color: rgb(0, 0, 0); background-color: rgb(245, 247, 250); font-size: 12px">cust000000x5jwbZSEQC</span></p><p id="ufa0cff76" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">ShineMo1__UOC078_C_TLD01__ItemSituation__CST</span></p><p id="u605e093b" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">cust000000xA7F53Q384  </span><span class="ne-text" style="color: rgb(0, 0, 0); background-color: rgb(245, 247, 250); font-size: 12px">cust000000xA7F53Q396</span></p><p id="ud22dfdef" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">ShineMo1__UOC095_C_TLD01__ItemSituation__CST</span></p><p id="udc3d96dc" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">cust000000xA7F7ZFpXU  cust000000xA7F7ZFpYW</span></p><p id="u9bf1a7a2" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px">ShineMo1__UOC113_C_TLD01__ItemSituation__CST</span></p><p id="u1dfab79d" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px"></span></p><p id="u64bb5def" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px"></span></p><pre data-language="javascript" id="luwhP" class="ne-codeblock language-javascript"><code>https://10.65.32.34/u-route/baas/metadata/v1.0/object/cust000000x5jwR1Apqy/field/cust000000x5jwR1Aprx
PUT 请求
{
    &quot;isRequired&quot;: false
}
</code></pre><p id="u6db2862e" class="ne-p" style="text-align: left"><span class="ne-text" style="color: rgb(0, 0, 0); font-size: 12px"></span></p></details>


<details class="lake-collapse"><summary id="ua9eab989"><span class="ne-text">bug验证 10 .17号 截图</span></summary><p id="u7bdc643a" class="ne-p"><br></p><p id="u41d44b7a" class="ne-p"><span class="ne-text">验证查询代办 可以查到</span></p><p id="uc22d0188" class="ne-p"><img src="https://cdn.nlark.com/yuque/0/2022/png/21382055/1666017484742-373b125f-172a-47f0-93b3-c5d6b0093b8c.png" width="967" title="" crop="0,0,1,1" id="u40e85bf5" class="ne-image"></p><p id="uf3748afd" class="ne-p"><br></p><p id="u29879fc0" class="ne-p"><img src="https://cdn.nlark.com/yuque/0/2022/png/21382055/1666017582017-3aeb08fe-6b6b-466e-986b-079b729542ec.png" width="955" title="" crop="0,0,1,1" id="ub3bbe792" class="ne-image"></p><p id="u42a85a4c" class="ne-p"><br></p><p id="uee71ded6" class="ne-p"><br></p><p id="u699ecb4f" class="ne-p"><span class="ne-text">地灾没有抄送人</span></p><p id="u9384ed7b" class="ne-p"><img src="https://cdn.nlark.com/yuque/0/2022/png/21382055/1666017862430-5bd32826-878c-4b30-922a-35bec0cb0c1e.png" width="967" title="" crop="0,0,1,1" id="u6bb596ae" class="ne-image"></p><p id="ua1cb6fc2" class="ne-p"><br></p><p id="u80fd467e" class="ne-p"><br></p></details>
 

# 开发环境测试流程




```javascript
{ 
    "caseName": "aaaa",
    "srcCaseId": "string",
    "itemCode": "ceshi1",
    "description": "qqq",
    "occurrenceDate": "2022-08-04",
    "address": "杭州",
    "longitude": "120.999999",
    "latitude": "38.9999",
    
    "gridCode": "sds",
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
      "orgCode": "ff8080817bf823fb017c15b79e630116",
     "orgName": "禅城区城市管理和综合执法局",
     "postCode": "ff8080817bdd6084017bdf3b776100411",
      "postName": "城管局坐席员",
                    "userCode": "por_shi01",
                    "userName": "por_shi01"
  },
    "dutyOrgs": [],
    "extFieldValues": [ 
    ] 
}

{
    "extFieldValues": [
        {
            "fieldName": "1",
            "fieldValue": "Y"
        }
    ],
    "action": "verify",
    "comment": "处置第一个节点",
    "handlingUser": {
      "orgCode": "wanggebumeng",
        "orgName": "网格部门",
        "postCode": "gangweiceshi",
        "postName": "岗位测试",
          "userCode": "yipeng123",
          "userName": "yipeng123"
  },
    "taskId": "c60G000000xl7Y1SiUU4"
}


{
    "handlingUser": {
        "orgCode": "chanchengqufenbozhongxin",
        "orgName": "禅城区分拨中心",
       "postCode": "chanchengqufenbozhongxinzuoxiyuan",
        "postName": "禅城区分拨中心坐席员",
        "userCode": "zhangmengqing",
       "userName": "zhangmengqing"
    },
    "caseCode": "2022102000041",
     "attachments": [
        
    ],
    "taskType": "TASK_TYPE_VERIFY",
    "comment": "受理任务",
    "executorType": "Organization",
    "isCompulsive": "N",
    "cooperationType": "Serial",
    "executors": [
        
    ],
    "grid":{ 
        "gridType":"BaseGrid", 
        "gridCode":"sds" 
	} 
}


{
    "handlingUser": {
         "orgCode": "chanchengqufenbozhongxin",
        "orgName": "禅城区分拨中心",
       "postCode": "chanchengqufenbozhongxinzuoxiyuan",
        "postName": "禅城区分拨中心坐席员",
        "userCode": "zhangmengqing",
       "userName": "zhangmengqing"
    },
    "caseCode": "",
    "taskType": "TASK_TYPE_VERIFY",
    "comment": "转网格核实",
    "attachments": [
        {
            "attachmentName": "bdlogo.png",
            "attachmentUrl": "http://www.baidu.com/img/bdlogo.png"
        }
    ],
    "executorType": "Grid",
    "isCompulsive": "N",
    "grid": {
        "gridCode": "ceshijichu",
        "gridType": "BaseGrid"
    }
} 








```





```javascript
select * from ShineMo1__UOC001_C_TLD01__ItemDef__CST where ShineMo1__status__CST = 'open' 
and  ShineMo1__innerDistrict__CST = 'UOC001'
and  ShineMo1__innerSubDistrict__CST = 'UOC002'
and  ShineMo1__customCode__CST = 'CS_1'
 ShineMo1__status__CST ,ShineMo1__innerDistrict__CST,ShineMo1__innerSubDistrict__CST,ShineMo1__customCode__CST
conditions: [ {
             field: 'ShineMo1__status__CST', 
             operator: 'eq', 
             value: 'open'
         }, {
             field: 'ShineMo1__innerDistrict__CST', 
             operator: 'eq', 
             value: 'UOC001'
         }, {
             field: 'ShineMo1__innerSubDistrict__CST', 
             operator: 'eq', 
             value: 'UOC002'
         }, {
             field: 'ShineMo1__customCode__CST', 
             operator: 'eq', 
             value: 'CS_1'
         } ], 
```







```javascript
{
    "attachments": [
        {
            "attachmentName": "bdlogo.png",
            "attachmentUrl": "http://www.baidu.com/img/bdlogo.png"
        }
    ],
    "handlingUser": {
         "orgCode": "wanggebumeng",
         "orgName": "网格部门",
          "postCode": "gangweiceshi",
                    "postName": "岗位测试",
                    "userCode": "por_shi01",
                    "userName": "por_shi01"
    },
    "taskId": "c60G000000xl7Y1SiUU4",
    "taskProgresses": [],
    "comment": "核实成功",
    "reason": "网格进行核实",
    "extFieldValues": [
        {
            "fieldName": "TASK_TYPE_VERIFY",
            "fieldValue": "Y",
            "childFieldValues": [
                {
                    "fieldName": "tastype",
                    "fieldValue": "核实"
                },
                {
                    "fieldName": "result",
                    "fieldValue": "通过"
                }
            ]
        }
    ]
} 





{
    "handlingUser": {
       "orgCode": "ff8080817bf823fb017c15b79e630116",
     "orgName": "禅城区城市管理和综合执法局",
       "postCode": "ff8080817bdd6084017bdf3b776100411",
                    "postName": "城管局坐席员",
                    "userCode": "por_shi01",
                    "userName": "por_shi01"
    },
    "caseCode": "2022102000054",
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
              "orgCode": "ff8080817bf823fb017c15b79e630116",
     "orgName": "禅城区城市管理和综合执法局",
       "postCode": "ff8080817bdd6084017bdf3b776100411",
                    "postName": "城管局坐席员",
                    "userCode": "por_shi01",
                    "userName": "por_shi01"
        }
    ]
} 




{
    "attachments": [
        {
            "attachmentName": "bdlogo.png",
            "attachmentUrl": "http://www.baidu.com/img/bdlogo.png"
        }
    ],
    "handlingUser": {
        "orgCode": "chanchengqufenbozhongxin",
                    "orgName": "禅城区分拨中心",
                    "postCode": "chanchengqufenbozhongxinzuoxiyuan",
                    "postName": "禅城区分拨中心坐席员",
                    "userCode": "chanchengqu_shangbao",
                    "userName": "chanchengqu_shangbao"
    },
    "taskId": "c60G000000xlAszRqgE4",
    "taskProgresses": [],
    "comment": "进行处置",
    "reason": "处置",
    "extFieldValues": [
        {
            "fieldName": "TASK_TYPE_TREAT",
            "fieldValue": "N",
            "childFieldValues": [
                {
                    "fieldName": "tastype",
                    "fieldValue": "处置"
                },
                {
                    "fieldName": "result",
                    "fieldValue": "通过"
                }
            ]
        }
    ]
} 

{
    "handlingUser": {
         "orgCode": "chanchengqufenbozhongxin",
                    "orgName": "禅城区分拨中心",
                    "postCode": "chanchengqufenbozhongxinzuoxiyuan",
                    "postName": "禅城区分拨中心坐席员",
                    "userCode": "chanchengqu_shangbao",
                    "userName": "chanchengqu_shangbao"
    },
    "caseCode": "2022102000054",
    "taskType": "TASK_TYPE_CHECK",
    "comment": "转部门核查",
    "attachments": [
        {
            "attachmentName": "bdlogo.png",
            "attachmentUrl": "http://www.baidu.com/img/bdlogo.png"
        }
    ],
    "executorType": "Grid",
    "isCompulsive": "N",
    "grid": {
        
      "gridCode": "ceshijichu",
        "gridType": "BaseGrid"
    }
} 



{
    "attachments": [
        {
            "attachmentName": "bdlogo.png",
            "attachmentUrl": "http://www.baidu.com/img/bdlogo.png"
        }
    ],
    "handlingUser": {
"orgCode": "chanchengqufenbozhongxin",
                    "orgName": "禅城区分拨中心",
                    "postCode": "chanchengqufenbozhongxinzuoxiyuan",
                    "postName": "禅城区分拨中心坐席员",
                    "userCode": "chanchengqu_shangbao",
                    "userName": "chanchengqu_shangbao"
    },
    "taskId": "c60G000000xlBN99uogS",
    "taskProgresses": [],
    "comment": "核查",
    "reason": "需要核查",
    "extFieldValues": [
        {
            "fieldName": "TASK_TYPE_CHECK",
            "fieldValue": "Y",
            "childFieldValues": [
                {
                    "fieldName": "tastype",
                    "fieldValue": "核查"
                },
                {
                    "fieldName": "result",
                    "fieldValue": "不通过"
                }
            ]
        }
    ]
} 









```







# 瞎几把记录




十堰市 - 观音镇 茅箭区 不点

马鞍镇 - 三观东陵



caseservice

esindexing2

taskservice

ticketing









































































































































































































































































































































































































































































































































































































































































